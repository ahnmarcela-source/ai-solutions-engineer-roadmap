"""POC educacional: dados sinteticos, sem automacao de sistemas reais."""
from stages_loader import load_stage
retrieve_context = load_stage(3).retrieve_context

def propose_action(event):
    result = retrieve_context(event)
    action = "CHECK_CONNECTIVITY" if result["category"] == "TIMEOUT" else "CHECK_ACCESS" if result["category"] == "AUTH" else "ESCALATE_TO_HUMAN"
    return {**result, "proposed_action": action, "requires_human_approval": True, "executed": False}
