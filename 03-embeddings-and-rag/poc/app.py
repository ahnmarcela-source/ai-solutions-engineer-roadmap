"""POC educacional: dados sinteticos, sem automacao de sistemas reais."""
from stages_loader import load_stage
classify_incident = load_stage(2).classify_incident
DOCS = [
    {"id": "runbook-timeout", "text": "TIMEOUT: verificar latencia, retries e conectividade; escalar se persistir."},
    {"id": "runbook-auth", "text": "AUTH: conferir credenciais em cofre e permissoes sem expor segredos."},
]

def retrieve_context(event):
    classified = classify_incident(event)
    key = "TIMEOUT" if classified["category"] == "TIMEOUT" else "AUTH" if classified["category"] == "AUTH" else ""
    matches = [d for d in DOCS if key and key in d["text"]]
    return {**classified, "sources": matches}
