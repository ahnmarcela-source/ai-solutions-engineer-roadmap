"""POC educacional: dados sinteticos, sem automacao de sistemas reais."""
from stages_loader import load_stage
normalize_event = load_stage(1).normalize_event

def classify_incident(event):
    event = normalize_event(event)
    message = event["message"].lower()
    category = "TIMEOUT" if "timeout" in message else "AUTH" if "unauthorized" in message else "UNKNOWN"
    return {**event, "category": category, "confidence": 1.0 if category != "UNKNOWN" else 0.0}
