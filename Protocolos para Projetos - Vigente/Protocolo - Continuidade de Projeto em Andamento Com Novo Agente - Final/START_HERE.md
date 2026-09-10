# Protocolo — Continuidade de Projeto em Andamento Com Novo Agente

DOCUMENT_TYPE = OPERATIONAL_ENTRYPOINT
UNIVERSAL_STANDARD = Agent-Continuity-Standard-v1.0/AGENT_CONTINUITY_STANDARD.md
BOOTSTRAP = Agent-Continuity-Standard-v1.0/continuity/NEW_CHAT_BOOTSTRAP_PROMPT.md
PROJECT_SPECIFIC_PAYLOAD = PROJECT_SPECIFIC_PAYLOAD/
PROJECT_SPECIFIC_PAYLOAD_REQUIRED_FOR_REAL_HANDOFF = YES

Este pacote é universal. Ele não contém identidade, state ou documentos ativos
de um projeto. `UNIVERSAL_STANDARD != PROJECT_INSTANCE`.

## Parte A — chat/agente atual

Antes da troca, reconciliar `PROJECT_STATE`, mapear documentos ativos,
registrar blockers, divergências e `NEXT_REQUIRED_ACTIVITY`. Quando aplicável,
fechar `HANDOFF_PREPARATION_GATE = PASS` somente com:

```text
PROJECT_STATE_UPDATE = PASS
HANDOFF_ARTIFACTS_READY = YES
ACTIVE_DOCUMENT_MAP_READY = YES
KNOWN_BLOCKERS_RECORDED = YES
KNOWN_DIVERGENCES_RECORDED = YES
NEXT_REQUIRED_ACTIVITY_RECORDED = YES
```

## Parte B — novo chat/agente

Carregar o payload específico, recuperar identidade, governança e state,
verificar facts e produzir a primeira resposta em `READ_ONLY_RECOVERY`.
Apresentar divergências e itens `UNVERIFIED`, aguardar validação humana e só
então promover `CONTINUITY_RECOVERY_GATE`.

```text
NEXT_REQUIRED_ACTIVITY != EXECUTION_AUTHORIZATION
CONTINUITY_RECOVERY_GATE = PASS != IMPLEMENTATION_PREFLIGHT = PASS
```

## Projeto existente sem continuidade formal

Definir `CONTINUITY_ADOPTION_MODE = RETROFIT_REQUIRED` e manter
`CONTINUITY_RETROFIT_GATE = NOT_PASSED`. Antes do handoff normal, materializar
ou reconciliar os artifacts aplicáveis. Não inventar histórico inexistente.
