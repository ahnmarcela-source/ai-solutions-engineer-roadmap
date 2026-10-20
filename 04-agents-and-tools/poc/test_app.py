import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from stages_loader import load_stage

class StageTest(unittest.TestCase):
    def setUp(self):
        self.mod = load_stage(4)
        self.event = {"source":"ACE", "message":"timeout in downstream", "correlation_id":"trace-001"}

    def test_happy_path(self):
        self.assertFalse(self.mod.propose_action(self.event)["executed"])

    def test_boundary_case(self):
        self.assertTrue(self.mod.propose_action(self.event)["requires_human_approval"])

if __name__ == "__main__":
    unittest.main()
