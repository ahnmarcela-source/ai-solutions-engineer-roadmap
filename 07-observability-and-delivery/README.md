# Etapa 07 — Observabilidade e entrega

> **Pre-requisito:** Concluir e testar **06-evaluation-and-security**.

**Objetivo:** Criar trace e metricas de processamento com biblioteca padrao.

**Conteudos:** logs estruturados, latencia, tracing conceitual, custo e deploy.

## Artefatos
- [Exploracao tecnica](EXPLORATORIO.md): conceitos, trade-offs, fontes e atividades.
- [Avaliacao](AVALIACAO.md): testes funcionais, criterios de aprovacao e desafio.
- [`poc/app.py`](poc/app.py): POC de referencia executavel em Python puro.
- [`poc/test_app.py`](poc/test_app.py): testes automatizados.

## Executar
Na raiz do repositorio:

```bash
python -m unittest discover -s 07-observability-and-delivery/poc -p 'test_*.py' -v
```

## Gate de progressao
1. Executar testes com sucesso.
2. Responder as perguntas do documento de avaliacao.
3. Registrar um ADR ou breve justificativa arquitetural.
4. Concluir o desafio e documentar evidencias.

**Proxima etapa:** Continua em **08-enterprise-ai-copilot**.
