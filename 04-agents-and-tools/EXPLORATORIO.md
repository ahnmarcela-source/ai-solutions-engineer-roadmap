# Exploratorio tecnico — Agentes e ferramentas

## Contexto do problema
O Enterprise Integration AI Copilot ira processar incidentes sinteticos de ambientes SAP CPI, IBM ACE e IBM MQ. Nesta etapa: **criar agente rule-based que chama ferramentas de diagnostico**.

## Conceitos fundamentais
- Tool calling, autorizacao, estados e limites operacionais.
- Separar entrada nao confiavel, regras de negocio e saida contratual.
- Medir resultado por testes repetiveis, nao apenas por uma demonstracao visual.
- Projetar comportamentos de falha seguros e inspecionaveis.

## Experimento guiado
1. Leia `poc/app.py` e desenhe o fluxo entrada → validacao → saida.
2. Execute a suite de testes e identifique condicoes de contorno.
3. Modifique uma entrada sintetica e observe o comportamento.
4. Registre resultado, limites, riscos e como integraria um provedor real.

## Limites da POC
O agente apenas recomenda e nao executa alteracoes em sistemas. Aprovacao humana e obrigatoria para qualquer acao.

## Decisoes de arquitetura para registrar
- Por que escolher este contrato?
- Como falhar de forma segura?
- Qual observabilidade e custo seriam necessarios em producao?

## Leituras de referencia (consulte licencas antes de reutilizar codigo)
- [Microsoft — Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Microsoft — AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
- [DataTalksClub](https://github.com/DataTalksClub)
