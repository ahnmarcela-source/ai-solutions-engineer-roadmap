# Etapa 06 — Avaliacoes, seguranca e governanca

> **Pre-requisito:** Concluir e testar **05-enterprise-integrations**.

**Objetivo:** Criar gate de avaliacao e bloqueio de resposta sem evidencia.

**Conteudos:** testes de regressao, metricas, prompt injection e PII.

## Artefatos
- [Exploracao tecnica](EXPLORATORIO.md): conceitos, trade-offs, fontes e atividades.
- [Avaliacao](AVALIACAO.md): testes funcionais, criterios de aprovacao e desafio.
- [`poc/app.py`](poc/app.py): POC de referencia executavel em Python puro.
- [`poc/test_app.py`](poc/test_app.py): testes automatizados.

## Executar
Na raiz do repositorio:

```bash
python -m unittest discover -s 06-evaluation-and-security/poc -p 'test_*.py' -v
```

## Gate de progressao
1. Executar testes com sucesso.
2. Responder as perguntas do documento de avaliacao.
3. Registrar um ADR ou breve justificativa arquitetural.
4. Concluir o desafio e documentar evidencias.

**Proxima etapa:** Continua em **07-observability-and-delivery**.
