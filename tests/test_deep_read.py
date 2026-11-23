import json
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from deep_read import finish_note, make_reading


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
