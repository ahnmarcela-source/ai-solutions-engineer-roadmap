"""POC educacional: dados sinteticos, sem automacao de sistemas reais."""
from stages_loader import load_stage
propose_action = load_stage(4).propose_action

def correlate_events(events):
    if not isinstance(events, list) or not events:
        raise ValueError("events must be a nonempty list")
    records = [propose_action(event) for event in events]
    ids = {r["correlation_id"] for r in records}
    return {"events": records, "same_transaction": len(ids) == 1, "correlation_ids": sorted(ids)}
