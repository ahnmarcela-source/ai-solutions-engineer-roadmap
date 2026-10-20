# AI Solutions Engineer — Enterprise Integration Learning Path

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Training](https://img.shields.io/badge/track-progressive-green) ![POC](https://img.shields.io/badge/POCs-offline-orange)

**Objetivo:** desenvolver um portfólio verificável de engenharia de IA, aproveitando experiência com SAP CPI, IBM ACE/MQ, APIs e observabilidade.

## Como estudar
Percorra as etapas numeradas na ordem. Cada pasta contém `README.md`, `EXPLORATORIO.md`, `AVALIACAO.md` e `poc/` com código e testes. Uma etapa usa funções da anterior. O capstone integra todas.

| Etapa | Tema | Entrega |
| --- | --- | --- |
| 01 | [Python, APIs e contratos](01-python-api-foundations/README.md) | Construir normalizador de eventos de integracao em Python |
| 02 | [LLMs, prompts e saidas estruturadas](02-llm-and-prompting/README.md) | Criar classificador deterministico de incidentes com contrato estruturado |
| 03 | [Busca, embeddings e RAG](03-embeddings-and-rag/README.md) | Criar recuperador lexical de documentos para incidentes |
| 04 | [Agentes e ferramentas](04-agents-and-tools/README.md) | Criar agente rule-based que chama ferramentas de diagnostico |
| 05 | [Integracao SAP / IBM / APIs](05-enterprise-integrations/README.md) | Criar adaptador de eventos ACE/MQ/SAP com payloads ficticios |
| 06 | [Avaliacoes, seguranca e governanca](06-evaluation-and-security/README.md) | Criar gate de avaliacao e bloqueio de resposta sem evidencia |
| 07 | [Observabilidade e entrega](07-observability-and-delivery/README.md) | Criar trace e metricas de processamento com biblioteca padrao |
| 08 | [Capstone: Enterprise Integration AI Copilot](08-enterprise-ai-copilot/README.md) | Integrar todas as etapas em um copilot local demonstravel |

## Início rápido (Windows PowerShell)
```powershell
py -3 --version
py -3 run_tests.py
py -3 08-enterprise-ai-copilot/poc/demo.py
```

## Modelo de evolução
`eventos sinteticos → normalizacao → classificacao → retrieval → agentes seguros → correlacao → evaluacao → telemetria → copilot`

## Estado de maturidade
Todas as POCs iniciais são **offline e determinísticas**, sem chamadas de LLM real. Isso é deliberado para permitir testes e isolamento de dependências. Integrações com modelos, embeddings vetoriais, RAG semântico, provedores SAP/IBM e OpenTelemetry reais são exercícios de extensão e não devem ser alegadas como implementadas.

## Segurança e ética
Não versionar credenciais, dados empresariais reais, logs sensíveis ou informações de clientes. Sem automação de remediação sem aprovação humana.

## Referências e atribuição
A organização didática foi inspirada por obras públicas, mas todo o texto e POCs aqui são originais. Consulte [REFERENCIAS.md](REFERENCIAS.md).
