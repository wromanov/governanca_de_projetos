# Agent Continuity Standard v1.0

STATUS = STRUCTURALLY_RECONCILED
DOCUMENT_TYPE = UNIVERSAL_OPERATIONAL_STANDARD
DOMAIN_SPECIFIC_CONTENT = PROHIBITED
PROJECT_SPECIFIC_STATE = EXTERNAL_TO_THIS_DOCUMENT
READY_FOR_CONTINUITY_AUTHORITY_REREAUDIT = YES
USER_FINAL_APPROVAL_FOR_REVISED_CONTINUITY_AUTHORITIES = PENDING
PROTOCOL_PACKAGE_STATE = READY_FOR_USER_APPROVAL

## 1. Finalidade e limites

Este Standard define como um agente recupera, reconcilia e retoma um projeto
em andamento após troca de chat, agente, máquina ou sessão. Ele é transversal:
não define identidade de projeto, domínio, tecnologia, fase, prioridade ou
resultado. Cada projeto materializa seus próprios artifacts a partir deste
contrato e das authorities locais.

```text
UNIVERSAL_STANDARD != PROJECT_INSTANCE
STANDARD_PROJECT_STATE != PROJECT_SPECIFIC_PROJECT_STATE
PROJECT_SPECIFIC_PAYLOAD_REQUIRED_FOR_REAL_HANDOFF = YES
NEXT_REQUIRED_ACTIVITY != EXECUTION_AUTHORIZATION
CONTINUITY_RECOVERY_GATE = PASS != IMPLEMENTATION_PREFLIGHT = PASS
```

## 2. Artifacts e resolução de paths

Uma continuidade real requer, quando existirem e forem aplicáveis:

- `AGENTS.md` como entrypoint e mapa de authorities;
- `AGENT_CONTINUITY.md` como instância específica do projeto;
- `PROJECT_STATE.md` como snapshot operacional atual;
- `NEW_CHAT_BOOTSTRAP_PROMPT.md` ou equivalente;
- policies/dependencies ativas e mapa de documentos canônicos.

O agente lê `AGENTS.md` quando disponível, resolve os paths canônicos
declarados pelo projeto e usa payload ou attachments fornecidos. Não inventa
paths. Fonte não localizada é `MISSING` ou `UNVERIFIED`.

O Standard não distribui identidade, state ou artifacts ativos de projeto.
Histórico é evidência contextual, não authority corrente.

## 3. Adoção e retrofit de continuidade

```text
CONTINUITY_ADOPTION_MODE = STANDARD_ALREADY_ADOPTED | RETROFIT_REQUIRED
```

Se `CONTINUITY_ADOPTION_MODE = RETROFIT_REQUIRED`, então:

```text
CONTINUITY_RETROFIT_GATE = NOT_PASSED
```

Antes de um handoff normal, materializar ou reconciliar, conforme aplicável,
`AGENTS.md`, `AGENT_CONTINUITY.md`, `PROJECT_STATE.md`, bootstrap,
policies/dependencies e mapa de documentos ativos. Não inventar histórico de
projeto inexistente. Somente após a reconciliação factual:

```text
CONTINUITY_RETROFIT_GATE = PASS
```

## 4. Gate de preparação do handoff

O chat/agente atual prepara o handoff antes de o novo chat iniciar. Quando
aplicável, `HANDOFF_PREPARATION_GATE = PASS` exige:

```text
PROJECT_STATE_UPDATE = PASS
HANDOFF_ARTIFACTS_READY = YES
ACTIVE_DOCUMENT_MAP_READY = YES
KNOWN_BLOCKERS_RECORDED = YES
KNOWN_DIVERGENCES_RECORDED = YES
NEXT_REQUIRED_ACTIVITY_RECORDED = YES
```

O próximo item precisa ser registrado, mas não é permissão de execução. Falta
de evidência material mantém o gate não passado.

```text
CHAT_ATUAL -> HANDOFF_PREPARATION_GATE -> NOVO_CHAT -> CONTINUITY_RECOVERY_GATE
```

## 5. Contrato da primeira resposta

Todo novo chat começa fail-closed:

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

Nenhuma sugestão no state, urgência ou mensagem anterior remove essas
restrições. A primeira resposta explica primeiro, em linguagem humana, o estado
recuperado, pendências, blockers, divergências, itens não verificados,
confirmações necessárias e próximo passo.

Depois apresenta, quando verificável:

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

## 6. Validação e retomada

Após apresentar a recuperação, o agente aguarda confirmação explícita:

```text
USER_CONTINUITY_VALIDATION = PASS
CONTINUITY_RECOVERY_GATE = PASS
```

Mesmo após isso, a atividade seguinte exige scope, authority, preflight,
critérios de aceite e autorização próprios. `NEXT_REQUIRED_ACTIVITY` não cria
permission; `CONTINUITY_RECOVERY_GATE = PASS` não é
`IMPLEMENTATION_PREFLIGHT = PASS`.

## 7. Facts, capability e segurança

Quando disponível, Git é a fonte factual para root, branch, `HEAD`, upstream,
worktree e staging. Sem capability, declarar os campos como `UNVERIFIED`.
Não fabricar paths, facts, capabilities, aprovações ou resultados.

Secrets permanecem fora de prompts, documentos, logs e respostas. Ações
irreversíveis ou externas exigem authority e autorização próprias.

## 8. Definition of Done

Recuperação só fica completa após recuperar identidade, governança, state,
facts, contradições e ausências, apresentar a primeira resposta sem mutações e
obter validação humana. Atividade formal só declara `ACTIVITY_COMPLETE = YES`
com state persistido e verificado:

```text
PROJECT_STATE_UPDATE = PASS
```
