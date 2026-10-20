import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from stages_loader import load_stage

class StageTest(unittest.TestCase):
    def setUp(self):
        self.mod = load_stage(1)
        self.event = {"source":"ACE", "message":"timeout in downstream", "correlation_id":"trace-001"}

    def test_happy_path(self):
        self.assertEqual(self.mod.normalize_event(self.event)["source"], "ACE")

    def test_boundary_case(self):
        with self.assertRaises(ValueError): self.mod.normalize_event({"source":"ACE"})

if __name__ == "__main__":
    unittest.main()
