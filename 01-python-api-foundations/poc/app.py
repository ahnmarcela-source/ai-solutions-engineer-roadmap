"""POC educacional: dados sinteticos, sem automacao de sistemas reais."""
def normalize_event(event):
    if not isinstance(event, dict):
        raise ValueError("event must be an object")
    for key in ("source", "message", "correlation_id"):
        if not isinstance(event.get(key), str) or not event[key].strip():
            raise ValueError(f"missing or invalid {key}")
    return {"source": event["source"].strip().upper(), "message": event["message"].strip(), "correlation_id": event["correlation_id"].strip()}
