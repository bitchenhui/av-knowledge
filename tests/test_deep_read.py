import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from deep_read import finish_note


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
