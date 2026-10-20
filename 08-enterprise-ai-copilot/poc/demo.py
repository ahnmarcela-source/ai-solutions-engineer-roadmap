import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from stages_loader import load_stage
run_copilot = load_stage(8).run_copilot
print(json.dumps(run_copilot([{"source":"ACE","message":"timeout in downstream","correlation_id":"trace-001"}]), indent=2, ensure_ascii=False))
