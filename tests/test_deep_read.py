import json
from datetime import date, timedelta
import tempfile
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from deep_read import EvidenceRejected, finish_note, make_reading, record_rejection, select_due


class EvidenceTests(unittest.TestCase):
    def test_finish_note_with_source_pages(self):
        card = dict(method="method [p.2]", findings=["one finding [p.3]"], limitation="three clips")
        def reply():
            return "a note [p.2]\n\n```paper-evidence\n" + json.dumps(card) + "\n```"
        note, output = finish_note(reply(), "https://arxiv.org/pdf/1234.0000v1", 4, "a"*64)
        self.assertEqual(len(output["source_locations"]), 2)
        self.assertEqual(output["review_status"], "model_extracted")
        self.assertIn("#page=2", note)
        self.assertNotIn("paper-evidence", note)
        card["findings"] = ["invalid [p.5]"]
        with self.assertRaises(ValueError):
            finish_note(reply(), "https://arxiv.org/pdf/1234.0000v1", 4, "a"*64)

    def test_existing_note_keeps_prose_and_gains_card(self):
        raw = dict(method="方法 [p.1]", findings=["结果 [p.2]"], limitation="仅限论文实验")
        llm = Mock()
        llm.chat.return_value = "```json\n" + json.dumps(raw) + "\n```"
        note, card = make_reading(llm, {"summaries": {"deep_dive": "docs/curated.md"}}, "PDF text",
                                  "https://arxiv.org/pdf/1234.0000v1", 2, "a"*64, [])
        self.assertIsNone(note)
        self.assertEqual(card["source_locations"][-1], "https://arxiv.org/pdf/1234.0000v1#page=2")
        llm.chat.assert_called_once()

    def test_source_version_backoff_preserves_capacity_and_old_receipts(self):
        day = date(2026, 1, 1)
        papers = [dict(id=f"paper:arxiv:2601.0000{i}", source={"external_id": f"2601.0000{i}v1"})
                  for i in range(6)]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for item in papers[:3]:
                record_rejection(root, item, day, "a"*64, "missing page")
            record_rejection(root, papers[0], day, "a"*64, "not a second day")
            self.assertEqual(len(list(root.glob("*/*.json"))), 3)
            self.assertEqual(select_due(papers, 3, root, day + timedelta(days=1)), papers[3:])
            self.assertEqual(select_due(papers, 3, root, day + timedelta(days=2)), [*papers[3:5], papers[0]])
            self.assertEqual(select_due(papers[:3], 3, root, day + timedelta(days=2)), papers[:3])
            self.assertEqual(select_due(papers, 0, root, day), [])
            record_rejection(root, papers[0], day + timedelta(days=2), "a"*64, "missing page again")
            self.assertEqual(select_due(papers[:1], 1, root, day + timedelta(days=5)), [])
            self.assertEqual(select_due(papers[:1], 1, root, day + timedelta(days=6)), papers[:1])
            papers[0]["source"]["external_id"] = "2601.00000v2"
            self.assertEqual(select_due(papers[:1], 1, root, day), papers[:1])

    def test_model_or_network_errors_are_not_recordable_paper_rejections(self):
        item = {"summaries": {"deep_dive": "docs/old.md"}}
        model = Mock()
        model.chat.side_effect = RuntimeError("service unavailable")
        with self.assertRaises(RuntimeError):
            make_reading(model, item, "", "", 2, "", [])
        model.chat.side_effect = None
        model.chat.return_value = "not JSON"
        with self.assertRaises(EvidenceRejected):
            make_reading(model, item, "", "", 2, "", [])
