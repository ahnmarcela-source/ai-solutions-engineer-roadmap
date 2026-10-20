# Etapa 02 — LLMs, prompts e saidas estruturadas

> **Pre-requisito:** Concluir e testar **01-python-api-foundations**.

**Objetivo:** Criar classificador deterministico de incidentes com contrato estruturado.

**Conteudos:** schemas, delimitacao entre dados e instrucoes, validacao e testabilidade.

## Artefatos
- [Exploracao tecnica](EXPLORATORIO.md): conceitos, trade-offs, fontes e atividades.
- [Avaliacao](AVALIACAO.md): testes funcionais, criterios de aprovacao e desafio.
- [`poc/app.py`](poc/app.py): POC de referencia executavel em Python puro.
- [`poc/test_app.py`](poc/test_app.py): testes automatizados.

## Executar
Na raiz do repositorio:

```bash
python -m unittest discover -s 02-llm-and-prompting/poc -p 'test_*.py' -v
```

## Gate de progressao
1. Executar testes com sucesso.
2. Responder as perguntas do documento de avaliacao.
3. Registrar um ADR ou breve justificativa arquitetural.
4. Concluir o desafio e documentar evidencias.

**Proxima etapa:** Continua em **03-embeddings-and-rag**.
