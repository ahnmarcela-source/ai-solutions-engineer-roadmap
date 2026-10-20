import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from stages_loader import load_stage

class StageTest(unittest.TestCase):
    def setUp(self):
        self.mod = load_stage(5)
        self.event = {"source":"ACE", "message":"timeout in downstream", "correlation_id":"trace-001"}

    def test_happy_path(self):
        self.assertTrue(self.mod.correlate_events([self.event, self.event])["same_transaction"])

    def test_boundary_case(self):
        self.assertFalse(self.mod.correlate_events([self.event,{**self.event,"correlation_id":"other"}])["same_transaction"])

if __name__ == "__main__":
    unittest.main()
