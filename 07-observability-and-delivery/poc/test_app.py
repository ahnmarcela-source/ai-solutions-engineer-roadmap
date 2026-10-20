import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from stages_loader import load_stage

class StageTest(unittest.TestCase):
    def setUp(self):
        self.mod = load_stage(7)
        self.event = {"source":"ACE", "message":"timeout in downstream", "correlation_id":"trace-001"}

    def test_happy_path(self):
        self.assertGreaterEqual(self.mod.record_telemetry([self.event])["telemetry"]["latency_ms"], 0)

    def test_boundary_case(self):
        self.assertEqual(self.mod.record_telemetry([{**self.event,"message":"unknown"}])["status"], "INSUFFICIENT_EVIDENCE")

if __name__ == "__main__":
    unittest.main()
