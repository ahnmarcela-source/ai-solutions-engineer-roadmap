# Avaliacao — Etapa 08

## Criterios obrigatorios
- [ ] Executa POC sem dependencia de servicos pagos.
- [ ] Suite automatizada passa com `python -m unittest discover`.
- [ ] Explica as interfaces com a etapa anterior.
- [ ] Apresenta uma entrada valida e outra invalida / inconclusiva.
- [ ] Documenta riscos de privacidade, seguranca e limite de producao.

## Testes avaliativos
**T1 — caminho feliz:** executar com eventos sinteticos e conferir os campos esperados.

**T2 — caminho de falha:** enviar campo ausente, dado invalido ou incidente desconhecido e observar a falha segura.

**T3 — regressao:** rodar todos os testes das etapas anteriores.

## Perguntas para entrevista
1. Qual decisao de arquitetura foi tomada e qual alternativa voce descartou?
2. Como voce demonstraria a confiabilidade desta etapa para um cliente enterprise?
3. Como evitaria vazamento de dados e alteracao nao autorizada?

## Desafio pratico
Amplie a POC com um caso adicional, teste automatizado e evidencias no README.

**Aprovacao:** todos os testes verdes + desafio implementado + explicacao tecnica escrita.
