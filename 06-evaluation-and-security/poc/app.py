"""POC educacional: dados sinteticos, sem automacao de sistemas reais."""
from stages_loader import load_stage
correlate_events = load_stage(5).correlate_events

def evaluate_answer(events):
    result = correlate_events(events)
    has_evidence = all(bool(r["sources"]) for r in result["events"])
    return {**result, "grounded": has_evidence, "status": "READY_FOR_REVIEW" if has_evidence else "INSUFFICIENT_EVIDENCE"}
