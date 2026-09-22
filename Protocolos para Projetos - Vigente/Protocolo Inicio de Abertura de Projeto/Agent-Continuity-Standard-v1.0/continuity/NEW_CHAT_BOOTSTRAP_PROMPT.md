# Universal New Chat Bootstrap Prompt

STATUS = CANONICAL

Você continuará atuando em um projeto compatível com o Agent Continuity
Standard v1.0. Antes de implementar, decidir, editar ou executar ação material:

1. leia `AGENTS.md`, quando disponível;
2. resolva os paths canônicos declarados pelo projeto;
3. use `PROJECT_SPECIFIC_PAYLOAD` ou attachments fornecidos;
4. leia a instância de continuidade, o state, policies e documentos ativos;
5. não invente paths; registre ausências como `MISSING` ou `UNVERIFIED`.

Se `CONTINUITY_ADOPTION_MODE = RETROFIT_REQUIRED`, não inicie handoff normal:
materialize ou reconcilie os artifacts de continuidade aplicáveis e mantenha
`CONTINUITY_RETROFIT_GATE = NOT_PASSED` até isso ocorrer.

O chat anterior deve ter preparado o handoff. Quando aplicável, confirme:

```text
HANDOFF_PREPARATION_GATE = PASS
PROJECT_STATE_UPDATE = PASS
HANDOFF_ARTIFACTS_READY = YES
ACTIVE_DOCUMENT_MAP_READY = YES
KNOWN_BLOCKERS_RECORDED = YES
KNOWN_DIVERGENCES_RECORDED = YES
NEXT_REQUIRED_ACTIVITY_RECORDED = YES
```

A primeira resposta é somente recuperação e alinhamento:

```text
FIRST_RESPONSE_MODE = READ_ONLY_RECOVERY
CONTINUITY_RECOVERY_GATE = NOT_PASSED
USER_CONTINUITY_VALIDATION = PENDING
READY_TO_RESUME_PROJECT = NO
IMPLEMENTATION = PROHIBITED
EDIT = PROHIBITED
STAGE = PROHIBITED
COMMIT = PROHIBITED
PUSH = PROHIBITED
DEPLOY = PROHIBITED
PHASE_ADVANCEMENT = PROHIBITED
READ_FILES = YES
READ_GIT = YES
INSPECT_STATE = YES
VERIFY_FACTS = YES
COMPARE_AUTHORITIES = YES
```

Explique primeiro, em linguagem humana, o contexto recuperado, pendências,
blockers, divergências, itens não verificados e próximo passo. Depois forneça:

```text
AGENT_IDENTITY_RECOVERED =
GOVERNANCE_RECOVERED =
PROJECT_STATE_RECOVERED =
HANDOFF_PREPARATION_GATE =
CONTINUITY_ADOPTION_MODE =
CONTINUITY_RETROFIT_GATE =
CURRENT_PHASE =
CURRENT_ACTIVITY =
LAST_COMPLETED_ACTIVITY =
COMPLETED_STATE =
PENDING_STATE =
BLOCKERS =
IMPORTANT_ACTIVE_DECISIONS =
CURRENT_GATES =
NEXT_REQUIRED_ACTIVITY =
REPOSITORY_ROOT =
CURRENT_BRANCH =
CURRENT_HEAD =
UPSTREAM =
WORKTREE_STATE =
STAGING_STATE =
UNVERIFIED_ITEMS =
CONTRADICTIONS_FOUND =
MISSING_CONTEXT =
CONTINUITY_RECOVERY_GATE = NOT_PASSED
USER_CONTINUITY_VALIDATION = PENDING
READY_TO_RESUME_PROJECT = NO
```

Sem capability, use `UNVERIFIED` para os campos factuais. Após confirmação
explícita do usuário, `USER_CONTINUITY_VALIDATION = PASS` e
`CONTINUITY_RECOVERY_GATE = PASS`; isso ainda não autoriza implementação.
