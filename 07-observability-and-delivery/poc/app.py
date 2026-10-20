"""POC educacional: dados sinteticos, sem automacao de sistemas reais."""
import time
from stages_loader import load_stage
evaluate_answer = load_stage(6).evaluate_answer

def record_telemetry(events):
    start = time.perf_counter()
    result = evaluate_answer(events)
    elapsed_ms = round((time.perf_counter() - start) * 1000, 3)
    return {**result, "telemetry": {"event_count": len(events), "latency_ms": elapsed_ms, "status": result["status"]}}
