ATIVIDADE — ADOÇÃO E VERIFICAÇÃO EVIDENCIADA DE POLÍTICAS v2.1

MODO PADRÃO = ADOPT_AND_VERIFY
READ_ONLY_BY_DEFAULT = YES
SELF_ATTESTATION_ONLY = INSUFFICIENT

======================================================================
0. QUANDO USAR
======================================================================

Use este prompt quando o usuário entregar ao agente:

- uma policy nova;
- uma revisão de uma policy já existente;
- várias policies atualizadas;
- uma policy isolada que substitui versão anterior;
- um conjunto de policies para adoção operacional.

Objetivo:

garantir, com evidência objetiva, que o agente:

1. leu integralmente as policies entregues;
2. identificou identidade, versão, status, escopo e precedência;
3. resolveu supersession e referências stale;
4. entendeu o que mudou;
5. consegue aplicar as regras novas em decisões concretas;
6. abandonou fallback silencioso para regras antigas;
7. está apto a usar o conjunto válido nas próximas atividades relevantes.

======================================================================
0.1 COMO USAR
======================================================================

Exemplo A — policy nova isolada

Entregar:
- este prompt;
- a policy nova.

Resultado esperado:
- leitura integral;
- identidade resolvida;
- regras extraídas;
- probes policy-derived;
- READY_TO_APPLY ou estado equivalente.

Exemplo B — revisão de policy existente

Entregar:
- este prompt;
- a nova revisão;
- versão anterior, se disponível ou necessária para comparação.

Resultado esperado:
- POLICY_SET_DELTA;
- NEW / CHANGED / REMOVED RULES;
- supersession resolvida;
- stale references identificadas;
- apenas impactos materiais revalidados.

Exemplo C — várias policies

Entregar:
- este prompt;
- todas as policies que devem ser adotadas.

Resultado esperado:
- responsabilidade e precedência reconciliadas;
- conflitos reais identificados;
- probes derivados do conjunto;
- readiness final.

======================================================================
1. SIGNIFICADO DE "INTERNALIZAR"
======================================================================

"Internalizar" nesta atividade significa:

POLICY_OPERATIONAL_ADOPTION =
usar as policies entregues como referências operacionais válidas
dentro do contexto, workspace e authorities disponíveis ao agente.

Não significa:

- memória permanente;
- persistência garantida fora do contexto acessível;
- modificar policy;
- alterar perfil/configuração;
- promover documento;
- criar regra nova;
- reescrever governance.

SELF_ATTESTATION_ONLY = INSUFFICIENT

Adoção válida precisa ser observável por:

SOURCE_IDENTIFIED
+
FULL_READ
+
VERSION_RESOLVED
+
PRECEDENCE_RECONCILED
+
SUPERSESSION_RESOLVED
+
CHANGE_IMPACT_UNDERSTOOD
+
BEHAVIORAL_CONFORMANCE_PASS
+
AUTHORITY_PRESERVED
+
READY_FOR_FUTURE_USE

======================================================================
2. MODOS
======================================================================

MODE =
ADOPT_AND_VERIFY
| VERIFY_ONLY
| QUICK_ADOPT

Se o usuário não informar:

MODE = ADOPT_AND_VERIFY

----------------------------------------------------------------------
2.1 ADOPT_AND_VERIFY
----------------------------------------------------------------------

Usar quando o agente deve:

READ
→ RECONCILE
→ ADOPT
→ PROBE
→ REPORT

----------------------------------------------------------------------
2.2 VERIFY_ONLY
----------------------------------------------------------------------

Usar quando o objetivo é apenas verificar compatibilidade.

Não presumir adoção.

Executar:

POLICY_EXPECTATION
vs
CURRENT_BEHAVIOR / CONFIG / REFERENCES

e reportar divergências.

----------------------------------------------------------------------
2.3 QUICK_ADOPT
----------------------------------------------------------------------

Usar somente para:

POLICY_COUNT = 1
AND POLICY_SCOPE = SMALL_OR_BOUNDED
AND NO_COMPLEX_CROSS_POLICY_CONFLICT = YES

Mesmo em QUICK_ADOPT são obrigatórios:

SOURCE_IDENTITY
FULL_READ
SUPERSESSION_OR_DELTA_CHECK
2_TO_4_POLICY_DERIVED_PROBES
READINESS_STATE

QUICK_ADOPT != SELF_ATTESTATION

Se surgir conflito, impacto amplo ou alteração transversal:

ESCALATE_TO_ADOPT_AND_VERIFY = YES

======================================================================
3. POLICY SET
======================================================================

POLICIES_TO_ADOPT =

Todos os arquivos de policy explicitamente:

- anexados à atividade;
- listados pelo usuário como policies a adotar.

Não ampliar o conjunto por proximidade de diretório ou inferência.

Para cada policy registrar:

POLICY_ID =
FILE =
PATH_OR_SOURCE =
VERSION =
STATUS =
SCOPE =
RESPONSIBILITY =
SUPERSEDES =
DEPENDS_ON =
CANONICAL_FOR_THIS_ACTIVITY = YES | NO

Se identidade, versão ou status não puderem ser determinados:

POLICY_IDENTITY = AMBIGUOUS

e:

POLICY_ADOPTION_STATE = ADOPTION_BLOCKED

até resolução.

======================================================================
4. LEITURA INTEGRAL
======================================================================

POLICY_FULL_READ_REQUIRED = YES

Não se basear apenas em:

- nome;
- cabeçalho;
- resumo anterior;
- memória;
- descrição de outro agente;
- versão histórica.

Se algum documento não puder ser lido integralmente:

ADOPTION_BLOCKED

Informar:

DOCUMENT =
LIMITATION =
INACCESSIBLE_SURFACE =
IMPACT =

======================================================================
5. RESPONSABILIDADE / OWNERSHIP
======================================================================

Construir internamente:

POLICY_RESPONSIBILITY_MATRIX

Para cada policy determinar:

- o que governa;
- o que NÃO governa;
- decisões que controla;
- authorities superiores;
- policies complementares;
- documentos substituídos;
- dependências de runtime/capability.

Se duas policies aparentarem governar a mesma decisão:

1. verificar precedência explícita;
2. verificar supersession;
3. verificar escopo mais específico;
4. verificar authority superior.

Se conflito material permanecer:

DO_NOT_GUESS
CONFLICT_REQUIRES_USER_DECISION = YES

======================================================================
6. PRECEDÊNCIA
======================================================================

Aplicar primeiro a precedência definida pelas próprias authorities.

Na ausência de regra mais específica:

1. instrução explícita atual do usuário;
2. authorities/contratos canônicos específicos do projeto;
3. limites de segurança/operação/authority;
4. policies transversais aplicáveis;
5. protocolos operacionais;
6. convenções auxiliares.

Preservar:

CAPABILITY != AUTHORITY
PERMISSION != MODEL_CAPABILITY
DELEGATION != AUTHORITY_TRANSFER

======================================================================
7. SUPERSESSION E HIGIENE DE VERSÃO
======================================================================

Classificar documentos relevantes:

CURRENT
ACTIVE
SUPERSEDED
HISTORICAL_ONLY
COMPATIBILITY_ONLY
AMBIGUOUS

Executar:

STALE_POLICY_REFERENCE_CHECK

Verificar, quando acessível:

- prompts ativos;
- AGENTS;
- continuity docs;
- config/registry;
- perfis;
- instruções locais;
- referências documentais relevantes.

Não alterar arquivos sem autorização.

Preservar:

HISTORICAL_REFERENCE != ACTIVE_POLICY_REFERENCE

Adicionar regra obrigatória:

NO_SILENT_FALLBACK_TO_OLD_VERSION = YES

Se uma nova revisão for adotada:

SUPERSEDED_RULE
MUST_NOT_REMAIN_OPERATIONAL_DEFAULT

======================================================================
8. POLICY_SET_DELTA
======================================================================

Quando o agente já tiver um conjunto válido e receber uma policy revisada:

POLICY_SET_DELTA = REQUIRED

Comparar:

PREVIOUS_VERSION
vs
NEW_VERSION

Identificar:

NEW_RULES =
CHANGED_RULES =
REMOVED_RULES =
UNCHANGED_RULES =
NEW_DEFAULTS =
REMOVED_DEFAULTS =
NEW_GATES =
REMOVED_GATES =
AUTHORITY_CHANGES =
ROLE_CHANGES =
RUNTIME_DEPENDENCY_CHANGES =

Revalidar apenas o impacto material da mudança.

Não repetir auditoria completa do que permaneceu inequivocamente inalterado,
salvo quando existir dependência real.

Aplicar:

DELTA_FIRST_VALIDATION = DEFAULT

FULL_REVALIDATION_REQUIRED_WHEN =
    PRECEDENCE_CHANGED
    OR AUTHORITY_CHANGED
    OR CROSS_POLICY_CONFLICT_CHANGED
    OR IDENTITY_AMBIGUITY
    OR MATERIAL_ROLE_OR_RUNTIME_CHANGE
    OR USER_REQUESTS_FULL_REVALIDATION

======================================================================
9. CHANGE IMPACT MAP
======================================================================

Para policy nova ou revisada, construir:

CHANGE_IMPACT_MAP

Cobrir, quando aplicável:

AFFECTED_POLICIES =
AFFECTED_ROLES =
AFFECTED_MODELS_EFFORTS =
AFFECTED_PROMPTS =
AFFECTED_CONFIG =
AFFECTED_RUNTIME =
AFFECTED_AGENTS_FILES =
AFFECTED_CONTINUITY_DOCS =
AFFECTED_REGISTRY =
AFFECTED_PROTOCOLS =
AFFECTED_PROJECT_AUTHORITIES =

Classificar cada impacto:

REQUIRED_CHANGE
RECOMMENDED_CHANGE
RUNTIME_CHECK
NO_ACTION
UNKNOWN

Não alterar nada sem autorização.

======================================================================
10. EXTRAÇÃO DOS CONTROLES
======================================================================

As policies entregues são a fonte normativa.

Extrair:

MANDATORY_RULES =
PROHIBITIONS =
DEFAULTS =
GATES =
ESCALATION_RULES =
STOP_CONDITIONS =
AUTHORITY_BOUNDARIES =
ROLE_CONTRACTS =
OUTPUT_CONTRACTS =
RUNTIME_DEPENDENCIES =

Não inventar valores ausentes.

Quando uma regra depender de runtime/model/skill/plugin/profile/capability:

VERIFY_RUNTIME_IF_AVAILABLE

Se não puder verificar:

RUNTIME_DEPENDENCY = UNVERIFIED

Não transformar automaticamente em policy failure.

======================================================================
11. CONFORMANCE PROBES
======================================================================

Gerar testes curtos derivados das próprias policies.

ADOPT_AND_VERIFY:
3_TO_7_PROBES

QUICK_ADOPT:
2_TO_4_PROBES

Cada probe:

PROBE_ID =
SOURCE_POLICY =
SOURCE_SECTION =
SCENARIO =
EXPECTED_DECISION =
ACTUAL_DECISION =
RESULT = PASS | FAIL

Cobrir somente mecanismos realmente presentes, por exemplo:

- model/effort;
- DIRECT vs MULTIAGENT;
- delegation/roles;
- authority/permission;
- escalation;
- stop conditions;
- validation/review;
- supersession;
- runtime dependency;
- comportamento novo introduzido pela revisão.

Não expor chain-of-thought.

Fornecer apenas:

DECISION
RULE_OR_SECTION
EVIDENCE
RESULT

======================================================================
12. REGRESSION / LEGACY CHECK
======================================================================

Procurar comportamento legado incompatível.

Para cada ocorrência:

LEGACY_RULE =
CURRENT_RULE =
IMPACT =
STATUS = RESOLVED | CONFLICT | NOT_APPLICABLE

Não presumir validade de regra antiga apenas porque já foi usada antes.

======================================================================
13. PERFIS / CONFIG / RUNTIME
======================================================================

Se a policy alterar:

- modelo;
- effort;
- role;
- subagent;
- skill;
- plugin;
- runtime;
- tool surface;

comparar, quando acessível:

POLICY_EXPECTATION
vs
RUNTIME_CONFIGURATION

Classificar:

COMPATIBLE
COMPATIBLE_WITH_RUNTIME_LIMITATION
INCOMPATIBLE
UNVERIFIED

Não editar config/profile sem autorização.

Se a policy permitir algo não suportado pelo runtime:

POLICY_ADOPTION_CAN_STILL_PASS = YES

desde que:

- limitação esteja identificada;
- boundaries sejam compreendidas;
- nenhuma regra seja inventada para compensar a limitação.

======================================================================
14. CHECKS INTERNOS DE ADOÇÃO
======================================================================

Executar internamente, na mesma atividade:

SOURCE_IDENTITY_CHECK
NORMATIVE_RECONCILIATION_CHECK
SUPERSESSION_DELTA_CHECK
BEHAVIORAL_CONFORMANCE_CHECK
FUTURE_USE_READINESS_CHECK

Não criar microgates ou fases separadas para cada check.

A atividade deve seguir:

READ
→ RECONCILE
→ DELTA
→ PROBE
→ REPORT

======================================================================
15. FUTURE-USE READINESS
======================================================================

Antes de declarar readiness, verificar internamente:

1. Sei qual policy governa a decisão?
2. Sei qual authority tem precedência?
3. Estou usando versão superseded?
4. Existe gate obrigatório?
5. Existe authority suficiente?
6. Existe stop condition?
7. O comportamento novo da revisão foi compreendido?
8. Estou adicionando burocracia que a policy não exige?
9. Existe runtime limitation?
10. Sei o que mudou em relação à versão anterior?

Se qualquer resposta material permanecer incerta:

ADOPTION_BLOCKED

ou:

READY_WITH_RUNTIME_LIMITATION

======================================================================
16. FUTURE BEHAVIOR OBSERVABILITY
======================================================================

Internalização não termina no relatório.

FUTURE_BEHAVIOR_OBSERVABILITY = REQUIRED

Depois de READY_TO_APPLY:

- aplicar a versão current/canonical;
- não recitar a policy sem necessidade;
- não repetir o relatório de adoção a cada tarefa;
- abandonar defaults superseded;
- preservar authority;
- demonstrar internalização pelas decisões futuras.

Se comportamento futuro contradizer a policy adotada:

POLICY_ADOPTION_REGRESSION = DETECTED

e a reconciliação deve ser reexecutada.

======================================================================
17. STATUS
======================================================================

Usar somente:

POLICY_ADOPTION_STATE =
READY_TO_APPLY
| READY_WITH_RUNTIME_LIMITATION
| ADOPTION_BLOCKED

READY_TO_APPLY:
- identity resolved;
- full read;
- reconciliation pass;
- supersession/delta resolved;
- probes pass;
- future-use readiness pass.

READY_WITH_RUNTIME_LIMITATION:
- entendimento/reconciliação pass;
- existe limitação factual de runtime;
- limitation não impede compreender/aplicar boundaries;
- nenhuma regra inventada.

ADOPTION_BLOCKED:
- policy ausente/inacessível;
- identity ambiguous;
- conflito normativo não resolvido;
- probes fail;
- versão ativa indefinida;
- entendimento insuficiente.

======================================================================
18. RELATÓRIO OBRIGATÓRIO
======================================================================

Produzir relatório curto.

POLICY_ADOPTION_REPORT

MODE =

STATUS =
ACTIVITY_COMPLETION_PERCENT =
COMPLETION_BASIS =

POLICIES_EXPECTED =
POLICIES_READ =
POLICIES_ACTIVE =
POLICIES_SUPERSEDED =
POLICIES_HISTORICAL_ONLY =

POLICY_SET_DELTA =
<NEW / CHANGED / REMOVED RULES ou NOT_APPLICABLE>

CHANGE_IMPACT_MAP =
<resumo objetivo>

SOURCE_IDENTITY_CHECK = PASS | FAIL
NORMATIVE_RECONCILIATION_CHECK = PASS | FAIL
SUPERSESSION_DELTA_CHECK = PASS | FAIL
BEHAVIORAL_CONFORMANCE_CHECK = PASS | FAIL
FUTURE_USE_READINESS_CHECK = PASS | FAIL

CONFLICTS_FOUND =
AMBIGUITIES_FOUND =
STALE_ACTIVE_REFERENCES =
RUNTIME_LIMITATIONS =
MISSING_CAPABILITIES =

CONFORMANCE_PROBES =
<PROBE_ID + RESULT>

POLICY_ADOPTION_STATE =
READY_TO_APPLY
| READY_WITH_RUNTIME_LIMITATION
| ADOPTION_BLOCKED

NEXT_ACTION =

======================================================================
19. ACTIVITY_COMPLETION_PERCENT
======================================================================

ACTIVITY_COMPLETION_PERCENT mede somente esta atividade.

STATUS = PASS
→ normalmente 100%

STATUS = BLOCKED
→ percentual efetivamente concluído

STATUS = FAIL
→ percentual efetivamente executado

100_PERCENT_COMPLETE != SUCCESS

======================================================================
20. QUANDO REEXECUTAR
======================================================================

Reexecutar esta verificação quando:

- usuário entregar nova policy;
- usuário entregar nova revisão;
- versão/status/precedência mudar;
- surgir conflito real de authority;
- runtime/config mudar de modo material para regra dependente dele;
- comportamento futuro indicar regressão.

Não reexecutar a cada tarefa sem motivo.

======================================================================
21. COMPORTAMENTO APÓS ADOÇÃO
======================================================================

Se:

POLICY_ADOPTION_STATE = READY_TO_APPLY

então:

- aplicar as policies nas próximas atividades relevantes;
- usar current/canonical;
- abandonar superseded;
- não repetir relatório sem necessidade;
- preservar project authorities;
- demonstrar adoção pelo comportamento.

Se:

POLICY_ADOPTION_STATE = READY_WITH_RUNTIME_LIMITATION

então:

- aplicar tudo suportado;
- declarar limitação somente quando afetar decisão concreta;
- não inventar workaround normativo.

Se:

POLICY_ADOPTION_STATE = ADOPTION_BLOCKED

então:

- não afirmar que adotou;
- reportar blocker exato;
- não substituir policy por memória, histórico ou inferência.

======================================================================
22. REGRA FINAL
======================================================================

Adoção válida não é:

"Li e entendi."

Adoção válida é:

SOURCE_IDENTIFIED
+
FULL_READ
+
VERSION_RESOLVED
+
PRECEDENCE_RECONCILED
+
SUPERSESSION_OR_DELTA_RESOLVED
+
CHANGE_IMPACT_UNDERSTOOD
+
BEHAVIORAL_CONFORMANCE_PASS
+
AUTHORITY_PRESERVED
+
READY_FOR_FUTURE_USE

Não gere burocracia textual permanente após a verificação.

A internalização deve ser observável no comportamento futuro.
