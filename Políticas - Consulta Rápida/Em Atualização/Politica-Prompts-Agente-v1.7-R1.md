# Política de Geração de Prompts Multiagente — v1.7-R1

```text
STATUS = PROPOSED
LIFECYCLE = DRAFT
TEST_CANDIDATE = YES
CANONICAL_AUTHORITY_BASELINE = Politica-Prompts-Agente-v1.4.md
CONTENT_BASELINE = Politica-Prompts-Agente-v1.7.md
CONTENT_BASELINE_STATUS = SUPERSEDED_DRAFT_FOR_MODEL_GATE_HARDENING
MULTIAGENT_CHANGE_SOURCE = GOV-02
SKILLS_PLUGINS_CHANGE_SOURCE = GOV-05
MODEL_TAXONOMY_CHANGE_SOURCE = GPT-6_ASTRA_UPDATE_2026-09
CHANGE_SCOPE = STRICT_MODEL_SELECTION_AND_REASONING_EFFORT_GATES
MULTIAGENT_RULES_CHANGE = NO
SKILLS_PLUGINS_RULES_CHANGE = NO
CANONICALIZATION = NO
PROMOTION = NO
DOMAIN_SPECIFIC_CONTENT = PROHIBITED
UNRELATED_NORMATIVE_CHANGE = PROHIBITED
USER_REVIEW_REQUIRED = YES
```

> Esta é uma candidata de teste endurecida derivada da v1.7. A v1.4 permanece
> a autoridade canônica até promoção formal. A v1.7-R1 torna a seleção de
> **Sol** e **Astra** explicitamente excepcional: disponibilidade, importância,
> tamanho, criticidade, quantidade de arquivos ou desejo genérico de qualidade
> não são justificativas válidas. Esta candidata não altera as regras de
> multiagente nem Skills/Plugins e não autoriza canonicalização, promoção,
> propagação, pacote, Git ou qualquer ação externa.

## 0. Finalidade, escopo e versionamento

Esta política define como preparar prompts de atividade para Work ou Codex,
incluindo **modelo, esforço de raciocínio, estratégia multiagente, skills,
plugins e execução nativa**. É transversal, project-agnostic e self-contained.

A v1.7-R1 endurece exclusivamente o eixo de **seleção de modelo e esforço** para
impedir uso trivial de GPT-5.6 Sol e GPT-6 Astra. As regras de multiagente e
Skills/Plugins permanecem preservadas nesta revisão.

O objetivo não é selecionar o modelo "mais forte". O objetivo é selecionar a
**menor configuração suficiente** para produzir resultado correto, verificável e
economicamente racional.

```text
OPTIMIZATION_TARGET =
SUFFICIENT_QUALITY
+ SUFFICIENT_ROBUSTNESS
+ SUFFICIENT_VERIFIABILITY
- UNNECESSARY_MODEL_COST
- UNNECESSARY_REASONING_COST
- UNNECESSARY_COORDINATION_COST
```

A configuração é composta por decisões independentes:

```text
MINIMUM_SUFFICIENT_CONFIGURATION =
MODEL
+ REASONING_EFFORT
+ EXECUTION_MODE
+ SKILL
+ PLUGIN
```

Disponibilidade, prestígio e criticidade não constituem necessidade:

```text
MODEL_AVAILABLE != MODEL_REQUIRED
STRONGER_MODEL != BETTER_DEFAULT
HIGHER_EFFORT != BETTER_DEFAULT
TASK_IMPORTANT != STRONGER_MODEL_REQUIRED
TASK_LARGE != STRONGER_MODEL_REQUIRED
MANY_FILES != STRONGER_MODEL_REQUIRED
LONG_CONTEXT != STRONGER_MODEL_REQUIRED
HIGH_RISK != STRONGER_MODEL_REQUIRED
```

A política usa como matriz operacional atual:

```text
GPT-5.6 Luna
GPT-5.6 Terra
GPT-5.6 Sol
GPT-6 Astra
```

A disponibilidade real depende da superfície, plano, rollout e configuração do
ambiente. Portanto:

```text
MODEL_AVAILABILITY = CONFIRM_AT_RUNTIME
```

Mudança futura de geração, nome, quota, preço ou disponibilidade não altera esta
policy automaticamente; exige nova revisão.

---

## 1. Modelo, esforço e categoria

### 1.1 Princípio central: Luna/Terra são a faixa normal; Sol/Astra são escalonamentos

```text
NORMAL_OPERATING_RANGE =
LUNA | TERRA

SOL =
ESCALATION_MODEL

ASTRA =
EXCEPTIONAL_CAPABILITY_MODEL
```

A seleção parte da carga cognitiva real, não da importância do projeto.

```text
DEFAULT_MODEL_SELECTION =
LOW_AMBIGUITY / MECHANICAL / REPETITIVE
→ LUNA

EVERYDAY_TECHNICAL_WORK / MODERATE_JUDGMENT
→ TERRA

COMPLEX_BUT_BOUNDED / STRONG_REASONING_REQUIRED
→ SOL, ONLY_IF_SOL_GATE = PASS

EXCEPTIONALLY_DEMANDING / NOVEL / OPEN_ENDED / HARD_END_TO_END
→ ASTRA, ONLY_IF_ASTRA_GATE = PASS
```

Não existe obrigação de percorrer uma escada:

```text
NO_MANDATORY_MODEL_LADDER = YES
```

Uma tarefa claramente classe Astra pode iniciar em Astra, mas somente após o
gate explícito desta policy.

---

### 1.2 Modelo e esforço são eixos independentes

**Modelo** define a capacidade-base.

**Esforço** define quanto dessa capacidade será usado para deliberar.

```text
MODEL != REASONING_EFFORT
MODEL_ESCALATION != EFFORT_ESCALATION
```

A orientação operacional atual da OpenAI informa que menor esforço não equivale
necessariamente a menor capacidade entre modelos e que, em certas cargas,
Astra em Low pode superar Sol em High. Portanto:

```text
DO_NOT_USE_REASONING_EFFORT_AS_MODEL_SUBSTITUTE = YES
DO_NOT_ASSUME_HIGHER_EFFORT_ALWAYS_WINS = YES
```

Classifique o problema corretamente:

```text
CAPABILITY_GAP
→ CONSIDER_STRONGER_MODEL

DELIBERATION_GAP
→ CONSIDER_HIGHER_EFFORT

MISSING_INFORMATION_OR_ACCESS
→ ACQUIRE_INFORMATION_OR_STOP
```

Nunca escalar modelo/esforço para compensar:

```text
MISSING_FILE
MISSING_CONTEXT
MISSING_REQUIREMENT
MISSING_PERMISSION
MISSING_TOOL
MISSING_PLUGIN
MISSING_AUTHORITY
```

---

### 1.3 GPT-5.6 Luna — trabalho focado, repetitivo e econômico

Luna é preferido quando a atividade é clara, observável, repetitiva ou
essencialmente mecânica.

Adequado para:

- extração e classificação;
- busca/localização objetiva;
- edição curta e transformação mecânica;
- boilerplate;
- atualização de manifest/checksum;
- alteração pequena com comportamento já definido;
- execução de script conhecido;
- tarefas volumosas, mas conceitualmente simples;
- aplicação de decisão já tomada;
- operações documentais mecânicas.

```text
LUNA_DOMAIN =
FOCUSED |
REPETITIVE |
MECHANICAL |
LOW_AMBIGUITY |
HIGH_VOLUME_COST_SENSITIVE
```

Quantidade de arquivos não altera essa classificação por si só.

---

### 1.4 GPT-5.6 Terra — default do trabalho técnico cotidiano

Terra é o default para atividades que exigem julgamento profissional moderado,
integração conhecida e tomada de decisão cotidiana.

Adequado para:

- implementação rotineira de código;
- integração moderada de componentes conhecidos;
- análise de documentos;
- elaboração de relatório técnico;
- investigação moderada;
- comparação de alternativas delimitadas;
- revisão técnica comum;
- refactor conhecido;
- testes de comportamento especificado;
- endpoint/CRUD convencional;
- ajustes de UI não arquiteturais;
- consolidação de evidências.

```text
TERRA_DOMAIN =
EVERYDAY_TECHNICAL_WORK |
MODERATE_JUDGMENT |
MODERATE_INTEGRATION |
BALANCED_CAPABILITY_COST
```

Regra:

```text
IF_TERRA_IS_EXPECTED_TO_BE_SUFFICIENT:
    SOL_ELIGIBLE = NO
    ASTRA_ELIGIBLE = NO
```

---

### 1.5 Gate de rotina — bloqueio antecipado de Sol/Astra

Antes de avaliar Sol ou Astra, responder:

```text
ROUTINE_EXECUTION_GATE =

REQUIREMENTS_ARE_CLEAR = YES | NO
SOLUTION_PATTERN_IS_KNOWN = YES | NO
ARCHITECTURAL_DECISION_REQUIRED = YES | NO
MATERIAL_AMBIGUITY_EXISTS = YES | NO
NOVEL_REASONING_REQUIRED = YES | NO
CROSS_SYSTEM_INTEGRATION_IS_DIFFICULT = YES | NO
VALIDATION_IS_DIFFICULT = YES | NO
```

Se:

```text
REQUIREMENTS_ARE_CLEAR = YES
SOLUTION_PATTERN_IS_KNOWN = YES
ARCHITECTURAL_DECISION_REQUIRED = NO
MATERIAL_AMBIGUITY_EXISTS = NO
NOVEL_REASONING_REQUIRED = NO
CROSS_SYSTEM_INTEGRATION_IS_DIFFICULT = NO
VALIDATION_IS_DIFFICULT = NO
```

então:

```text
ROUTINE_EXECUTION_GATE = PASS
SOL_ELIGIBLE = NO
ASTRA_ELIGIBLE = NO
MODEL = LUNA | TERRA
```

Esse resultado é obrigatório.

---

### 1.6 GPT-5.6 Sol — modelo de escalonamento para complexidade delimitada

Sol não é o default do projeto. Sol é elegível quando a tarefa é realmente
complexa, mas continua suficientemente delimitada.

```text
SOL_ROLE =
COMPLEX_BUT_BOUNDED_ESCALATION_MODEL
```

Para usar Sol:

```text
SOL_GATE = PASS
```

Exige **pelo menos um trigger material**:

```text
SOL_TRIGGER =

DIFFICULT_MULTI_COMPONENT_INTEGRATION |
HARD_BUT_BOUNDED_DEBUGGING |
MATERIAL_CONTRACT_OR_INVARIANT_REASONING |
DEEP_CROSS_DOCUMENT_SYNTHESIS |
NONTRIVIAL_ARCHITECTURAL_DECISION |
MULTIPLE_INTERDEPENDENT_TECHNICAL_CONSTRAINTS |
TERRA_EXPECTED_TO_REQUIRE_MATERIAL_REWORK
```

e também:

```text
EXPECTED_SOL_GAIN = MATERIAL
TERRA_EXPECTED_SUFFICIENCY = NO | MATERIALLY_INFERIOR
```

Se nenhum trigger puder ser apontado concretamente:

```text
SOL_GATE = FAIL
→ USE_LUNA_OR_TERRA
```

#### Justificativas inválidas para Sol

As seguintes justificativas, isoladamente, são inválidas:

```text
INVALID_SOL_JUSTIFICATIONS =

"THE TASK IS IMPORTANT"
"THE PROJECT IS LARGE"
"THERE ARE MANY FILES"
"THE TASK IS LONG"
"THE TASK IS HIGH RISK"
"WE WANT MORE QUALITY"
"SOL IS AVAILABLE"
"SOL IS STRONGER"
"THIS IS A PRODUCTION PROJECT"
```

Justificativa genérica produz:

```text
SOL_GATE = FAIL
```

---

### 1.7 GPT-6 Astra — modelo excepcional para as cargas mais exigentes

Astra não é um "Sol melhor" para uso rotineiro.

```text
ASTRA_ROLE =
EXCEPTIONAL_HIGH_CAPABILITY_MODEL
```

Astra só é elegível quando:

```text
ASTRA_SELECTION_GATE = PASS
```

O gate possui três requisitos cumulativos.

#### Requisito A — hard trigger

Deve existir pelo menos um:

```text
ASTRA_HARD_TRIGGER =

OPEN_ENDED_UNFAMILIAR_PROBLEM |
MATERIAL_NOVELTY_WITH_NO_CLEAR_SOLUTION_PATTERN |
EXCEPTIONALLY_DIFFICULT_CAUSAL_DEBUGGING |
HARD_END_TO_END_REASONING_ACROSS_MULTIPLE_SYSTEMS |
FRONTIER_TECHNICAL_OR_SCIENTIFIC_REASONING |
VERY_DIFFICULT_LONG_CONTEXT_RECONCILIATION |
HIGH_COMPLEXITY_COMPUTER_OR_TOOL_ORCHESTRATION |
SOL_CAPABILITY_ALREADY_OBSERVED_AS_INSUFFICIENT
```

#### Requisito B — ganho material esperado

```text
EXPECTED_ASTRA_GAIN = MATERIAL
```

O ganho deve ser concreto, por exemplo:

- redução material de retrabalho;
- compreensão superior de problema novel;
- integração end-to-end que Sol não seja esperado executar com mesma robustez;
- redução material de risco de conclusão incorreta;
- capacidade causal/sistêmica necessária;
- execução avançada de computador/ferramentas;
- raciocínio técnico/científico de fronteira.

#### Requisito C — justificativa contra Sol

Obrigatório preencher:

```text
WHY_SOL_IS_NOT_PREFERRED =
<razão concreta e específica>
```

Também:

```text
ASTRA_USAGE_COST_ACCEPTABLE = YES
```

Sem os três requisitos:

```text
ASTRA_SELECTION_GATE = FAIL
```

#### Justificativas inválidas para Astra

São explicitamente inválidas:

```text
INVALID_ASTRA_JUSTIFICATIONS =

"ASTRA IS MORE CAPABLE"
"ASTRA IS THE NEWEST MODEL"
"THE TASK IS IMPORTANT"
"THE TASK IS COMPLEX"
"THE PROJECT IS LARGE"
"THERE ARE MANY FILES"
"THE CONTEXT IS LONG"
"THE TASK IS HIGH RISK"
"ASTRA MAY PRODUCE A BETTER RESULT"
"MORE INTELLIGENCE IS SAFER"
"WE WANT MAXIMUM QUALITY"
"ASTRA IS AVAILABLE"
"THIS IS A CRITICAL PROJECT"
```

Qualquer uma delas, sem hard trigger + ganho material + justificativa contra Sol:

```text
ASTRA_SELECTION_GATE = FAIL
```

---

### 1.8 Zona proibida de Astra para trabalho rotineiro

```text
ASTRA_PROHIBITED_FOR_ROUTINE_TASKS = YES
```

Por padrão, Astra não deve ser usado para:

- editar Markdown;
- organizar documentação;
- criar/mover arquivos;
- atualizar estado de sprint;
- Git rotineiro já autorizado;
- stage/commit/push mecanicamente definidos;
- renomear símbolos;
- correção localizada conhecida;
- escrever testes para comportamento já especificado;
- pequenos refactors;
- CRUD convencional;
- endpoint bem definido;
- alteração simples de UI/CSS;
- resumo delimitado;
- extração/classificação;
- boilerplate;
- atualização de manifest;
- cálculo/checksum;
- execução de scripts conhecidos;
- implementação derivada de contrato fechado.

Exceção somente se a tarefa concreta deixar de ser rotineira e passar
formalmente no `ASTRA_SELECTION_GATE`.

---

### 1.9 Esforço de raciocínio — menor nível suficiente

A OpenAI separa reasoning effort da escolha de modelo e informa que maior esforço
pode consumir mais allowance sem garantir resultado melhor.

Aplicar:

```text
START_WITH_LOWEST_SUFFICIENT_EFFORT = YES
HIGHER_EFFORT_REQUIRES_REASON = YES
```

Mapeamento conceitual:

```text
LOW / LEVE
→ decisão clara, investigação curta, primeira passagem eficiente

MEDIUM / MÉDIO
→ planejamento, integração e raciocínio moderado

HIGH / ALTO
→ investigação difícil, múltiplas hipóteses e verificação aprofundada

XHIGH / EXTRA_ALTO
→ exceção rara, quando mais deliberação possui ganho material demonstrável

MAX
→ último recurso; somente quando disponível e explicitamente justificado
```

Os nomes exatos disponíveis devem ser confirmados na superfície atual.

Defaults:

```text
LUNA_DEFAULT_EFFORT = LOW | MEDIUM
TERRA_DEFAULT_EFFORT = MEDIUM
SOL_DEFAULT_EFFORT = MEDIUM
ASTRA_DEFAULT_EFFORT = LOW | MEDIUM
```

Selecionar Astra não autoriza esforço alto:

```text
ASTRA_SELECTED != ASTRA_HIGH_REQUIRED
```

#### Gate para High / XHigh / Max

```text
HIGH_EFFORT =
EXCEPTION

XHIGH_EFFORT =
RARE_EXCEPTION

MAX_EFFORT =
LAST_RESORT
```

High exige razão concreta ligada a investigação difícil, múltiplas hipóteses,
ambiguidade material ou verificação aprofundada.

XHigh exige:

```text
EXCEPTIONAL_REASONING_DIFFICULTY = YES
EXPECTED_MATERIAL_GAIN_FROM_MORE_DELIBERATION = YES
```

Max exige, cumulativamente:

```text
EXTREME_REASONING_DIFFICULTY = YES
LOWER_EFFORT_EXPECTED_SUFFICIENT = NO
HIGH_VALUE_OF_ADDITIONAL_DELIBERATION = YES
```

Nunca usar High/XHigh/Max apenas por importância.

---

### 1.10 Matriz operacional simplificada

A policy adota quatro classes para evitar falsa precisão.

| Classe | Modelo inicial | Esforço inicial | Natureza |
|---|---|---|---|
| R1 | Luna | Low/Medium | mecânica, focada, repetitiva, baixa ambiguidade |
| R2 | Terra | Medium | trabalho técnico cotidiano, julgamento moderado |
| R3 | Sol | Medium | complexo, profundo, mas delimitado; exige `SOL_GATE = PASS` |
| R4 | Astra | Low/Medium | excepcionalmente difícil, novel, aberto ou end-to-end; exige `ASTRA_SELECTION_GATE = PASS` |

```text
TASK_CLASS != PROJECT_IMPORTANCE
TASK_CLASS != FILE_COUNT
TASK_CLASS != PROJECT_SIZE
```

---

### 1.11 Cabeçalho obrigatório de seleção de modelo

Todo prompt governado relevante deve conter antes do objetivo:

```text
MODEL SELECTION

TASK_CLASS =
R1 | R2 | R3 | R4

MODEL =
LUNA | TERRA | SOL | ASTRA

REASONING_EFFORT =
LOW | MEDIUM | HIGH | XHIGH | MAX

MODEL_AVAILABILITY =
CONFIRMED | VERIFY_AT_RUNTIME | UNKNOWN

ROUTINE_EXECUTION_GATE =
PASS | FAIL

SOL_GATE =
PASS | FAIL | NOT_EVALUATED

ASTRA_SELECTION_GATE =
PASS | FAIL | NOT_EVALUATED

MODEL_SELECTION_REASON =
<razão concreta>
```

Se `MODEL = SOL`:

```text
SOL_TRIGGER =
<trigger material>

EXPECTED_SOL_GAIN =
<ganho concreto>

WHY_TERRA_IS_NOT_PREFERRED =
<razão concreta>
```

Se `MODEL = ASTRA`:

```text
ASTRA_HARD_TRIGGER =
<trigger material>

WHY_SOL_IS_NOT_PREFERRED =
<razão concreta>

EXPECTED_ASTRA_GAIN =
<ganho concreto>

ASTRA_USAGE_COST_ACCEPTABLE =
YES | NO
```

Para qualquer esforço acima do default:

```text
WHY_THIS_REASONING_EFFORT =
<razão concreta>
```

Regra:

```text
GENERIC_JUSTIFICATION = INVALID
```

---

### 1.12 Anti-patterns de seleção de modelo

```text
USE_SOL_BECAUSE_PROJECT_IS_IMPORTANT = PROHIBITED
USE_SOL_BECAUSE_TASK_IS_LARGE = PROHIBITED
USE_SOL_BECAUSE_MANY_FILES_EXIST = PROHIBITED
USE_SOL_FOR_GENERIC_QUALITY_ASSURANCE = PROHIBITED

USE_ASTRA_BECAUSE_IT_IS_NEWEST = PROHIBITED
USE_ASTRA_BECAUSE_IT_IS_STRONGEST = PROHIBITED
USE_ASTRA_BECAUSE_PROJECT_IS_CRITICAL = PROHIBITED
USE_ASTRA_BECAUSE_CONTEXT_IS_LONG = PROHIBITED
USE_ASTRA_FOR_ROUTINE_IMPLEMENTATION = PROHIBITED
USE_ASTRA_FOR_GENERIC_SECOND_OPINION = PROHIBITED
USE_ASTRA_AS_DEFAULT_ARCHITECT = PROHIBITED

USE_HIGH_EFFORT_BY_DEFAULT = PROHIBITED
USE_XHIGH_EFFORT_BY_DEFAULT = PROHIBITED
USE_MAX_EFFORT_BY_DEFAULT = PROHIBITED
```

---

### 1.13 Exemplos adversariais de roteamento

#### Exemplo A — atualizar 120 arquivos com substituição previamente definida

```text
FILE_COUNT = 120
AMBIGUITY = LOW
DECISION_ALREADY_MADE = YES

TASK_CLASS = R1
MODEL = LUNA
```

Número de arquivos não justifica Sol/Astra.

#### Exemplo B — implementar endpoint com contrato fechado

```text
REQUIREMENTS_ARE_CLEAR = YES
SOLUTION_PATTERN_IS_KNOWN = YES

TASK_CLASS = R2
MODEL = TERRA
```

#### Exemplo C — bug difícil envolvendo vários componentes conhecidos

```text
HARD_BUT_BOUNDED_DEBUGGING = YES
EXPECTED_SOL_GAIN = MATERIAL

SOL_GATE = PASS
TASK_CLASS = R3
MODEL = SOL
```

#### Exemplo D — projeto considerado crítico, mas alteração simples

```text
PROJECT_CRITICAL = YES
CHANGE = SIMPLE

SOL_GATE = FAIL
ASTRA_SELECTION_GATE = FAIL

MODEL = LUNA | TERRA
```

Criticidade não redefine carga cognitiva.

#### Exemplo E — problema novo, aberto e sistêmico sem padrão de solução claro

```text
OPEN_ENDED_UNFAMILIAR_PROBLEM = YES
MATERIAL_NOVELTY_WITH_NO_CLEAR_SOLUTION_PATTERN = YES
WHY_SOL_IS_NOT_PREFERRED = <razão específica>
EXPECTED_ASTRA_GAIN = MATERIAL
ASTRA_USAGE_COST_ACCEPTABLE = YES

ASTRA_SELECTION_GATE = PASS
TASK_CLASS = R4
MODEL = ASTRA
```

#### Exemplo F — "usar Astra para garantir qualidade"

```text
ASTRA_HARD_TRIGGER = NONE
JUSTIFICATION = "maximum quality"

ASTRA_SELECTION_GATE = FAIL
```

---

### 1.14 Regra de fallback e escalonamento durante execução

Se Luna/Terra revelar capability gap real:

```text
CURRENT_MODEL_CAPABILITY_GAP = YES
→ REEVALUATE_MODEL
```

Se Sol revelar capability gap real:

```text
SOL_CAPABILITY_ALREADY_OBSERVED_AS_INSUFFICIENT = YES
→ ASTRA_MAY_BECOME_ELIGIBLE
```

Entretanto, falha causada por instrução ruim, arquivo ausente, permissão,
ferramenta ou contexto faltante não conta como capability gap.

```text
INPUT_OR_ACCESS_FAILURE
!=
MODEL_FAILURE
```

O agente deve corrigir entrada/acesso quando autorizado ou parar no boundary
seguro.

---

### 1.15 Telemetria para impedir escalonamento por hábito

Para atividades recorrentes, quando viável, registrar:

```text
TASK_CLASS
MODEL
REASONING_EFFORT
SOL_GATE
ASTRA_SELECTION_GATE
SUCCESS
REWORK_CYCLES
ESCALATION_OCCURRED
APPROX_USAGE_IF_AVAILABLE
```

A telemetria deve responder:

- Terra estava sendo suficiente?
- Sol reduziu retrabalho de forma material?
- Astra trouxe ganho mensurável?
- o effort escolhido foi necessário?
- houve escalonamento por hábito sem trigger?

```text
EMPIRICAL_WORKLOAD_EVIDENCE
>
MODEL_PRESTIGE
```

Se Sol/Astra não demonstrar ganho recorrente para determinada classe de tarefa,
o roteamento futuro deve retornar ao modelo inferior suficiente.

---

## 2. Multiagentes (conteúdo GOV-02 preservado)

Execução direta é o padrão. Sem benefício material e verificável de
coordenação, declarar:

```text
EXECUTION_MODE = DIRECT
SUBAGENTS_ALLOWED = NO
OPTIONAL_SUBAGENT = PROHIBITED
AUTO_ESCALATION = NO
```

Não usar subagente por importância, tamanho, criticidade, capacidade
disponível ou revisão aparentemente prudente. Um subagente somente pode ser
considerado com benefício material e verificável ligado a pelo menos uma
condição:

```text
PARALLEL_INDEPENDENT_FRONTS = YES
DISTINCT_SPECIALIZATION_REQUIRED = YES
MATERIAL_DECOMPOSITION_GAIN = YES
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION = YES
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = YES
```

As condições são alternativas. A justificativa descreve ganho material,
entregável delimitado, consolidação e ausência de sobreposição de escrita.
Keywords, tamanho, criticidade ou intenção genérica de cobertura não provam o
gate. O agente principal mantém decisão, integração, inventário, autoridade de
escopo e validação final; não delega decisões arquiteturais, contratos,
invariantes ou expansão de escopo sem autorização explícita.

```text
TASK_IMPORTANT = YES  does not imply SUBAGENT_ALLOWED = YES
TASK_LARGE = YES      does not imply SUBAGENT_ALLOWED = YES
TASK_CRITICAL = YES   does not imply SUBAGENT_ALLOWED = YES
REVIEW_REQUIRED = YES does not imply REVIEWER_SUBAGENT_REQUIRED = YES
REVIEW_PASS != INDEPENDENT_AGENT_REVIEW
```

O modelo principal pode realizar `SELF_REVIEW`, `CONSISTENCY_CHECK`,
`ADVERSARIAL_PASS` e `FINAL_SELF_REVIEW` sem outro agente. Revisão
independente só é admissível com benefício demonstrável ou gate de governança
explícito; reviewer, explorer, worker ou architect preventivo não justificam
delegação.

### 2.1 Autoridade de escalonamento e decision gate

Se surgir necessidade real de escalonamento durante execução direta:

```text
SAFE_BOUNDARY
→ STOP
→ REPORT EVIDENCE
→ RECOMMEND ESCALATION
→ USER DECISION
```

Não criar agente automaticamente. Registrar `ESCALATION_REQUIRED`, razão,
evidência, insuficiência atual, modelo e papel recomendados, com
`SUBAGENT_STARTED = NO` e `USER_AUTHORIZATION_REQUIRED = YES`.

Antes de multiagente, avaliar com evidência as cinco condições acima e
`MATERIAL_VERIFIABLE_BENEFIT`. Condição sem evidência é `NO`. Quando todas são
`NO`, ou sem benefício verificável, o resultado obrigatório é execução direta
e `SUBAGENTS_ALLOWED = NO`. Esta política não cria policy separada de
delegação: `PROMPT_POLICY` contém `MODEL`, `EFFORT`, `MULTIAGENT` e
`SKILLS / PLUGINS`.

## 3. Taxonomia e fonte de Skills/Plugins (sincronização GOV-05)

```text
CAPABILITY != SKILL
SKILL != PLUGIN
PLUGIN_MAY_CONTAIN_SKILLS = YES
SKILL_MAY_EXIST_WITHOUT_PLUGIN = YES
NAME_SYNTAX_DOES_NOT_DEFINE_CLASS = YES
```

Capacidade nativa é função já disponível diretamente. Skill é workflow,
procedimento ou guidance reutilizável; plugin é recurso empacotado que pode
fornecer skills, apps, templates, ferramentas ou integrações. Nenhum deles
transfere authority.

Classificar somente nesta ordem: (1) runtime/metadata oficial, (2)
documentação oficial, (3) catálogo operacional adotado; sem confirmação,
`CLASSIFICATION = VERIFY_AT_RUNTIME`. Não inferir por `@name`, `$name`,
`/name`, produto, template ou nome de plugin.

```text
SKILLS_SOURCE_POLICY = OPENAI_FIRST_PARTY_ONLY
CUSTOM_SKILLS = NO
LOCAL_SKILLS = NO
USER_CREATED_SKILLS = NO
PLUGINS_SOURCE_POLICY = OPENAI_PLUGIN_ECOSYSTEM + GOVERNANCE_APPROVAL
OPENAI_AUTHORED = DO_NOT_ASSUME
```

Não criar, recomendar criar ou usar skill local/customizada/do usuário. A
disponibilidade no ecossistema OpenAI não prova autoria OpenAI, aprovação de
governança ou aderência ao projeto. Detalhes operacionais, catálogo e matriz
permanecem na Política de Uso de Skills e Plugins v1.1, authority especializada
aplicável; esta Prompt Policy contém apenas o contrato de decisão.

## 4. Cabeçalho obrigatório de decisão

Todo prompt Work/Codex começa, antes do objetivo, com estrutura equivalente:

```text
RECOMENDAÇÃO DE EXECUÇÃO

MODEL SELECTION

TASK_CLASS = [R1 | R2 | R3 | R4]
MODEL = [LUNA | TERRA | SOL | ASTRA]
REASONING_EFFORT = [LOW | MEDIUM | HIGH | XHIGH | MAX]
MODEL_AVAILABILITY = [CONFIRMED | VERIFY_AT_RUNTIME | UNKNOWN]

ROUTINE_EXECUTION_GATE = [PASS | FAIL]
SOL_GATE = [PASS | FAIL | NOT_EVALUATED]
ASTRA_SELECTION_GATE = [PASS | FAIL | NOT_EVALUATED]

MODEL_SELECTION_REASON = [...]

IF MODEL = SOL:
SOL_TRIGGER = [...]
EXPECTED_SOL_GAIN = [...]
WHY_TERRA_IS_NOT_PREFERRED = [...]

IF MODEL = ASTRA:
ASTRA_HARD_TRIGGER = [...]
WHY_SOL_IS_NOT_PREFERRED = [...]
EXPECTED_ASTRA_GAIN = [...]
ASTRA_USAGE_COST_ACCEPTABLE = [YES | NO]

WHY_THIS_REASONING_EFFORT = [...]

🧩 SKILLS
SKILL OFICIAL OPENAI RECOMENDADA = [nome | NONE]
SKILL_USE = [NONE | OPTIONAL_IF_MATERIAL | REQUIRED]
SKILL_AVAILABILITY = [CONFIRMED | VERIFY_AT_RUNTIME | UNKNOWN | NOT_REQUIRED]
SKILL_PURPOSE = [...]

🔌 PLUGINS
PLUGIN RECOMENDADO = [nome | NONE]
PLUGIN_USE = [NONE | OPTIONAL_IF_MATERIAL | REQUIRED]
PLUGIN_AVAILABILITY = [CONFIRMED | VERIFY_AT_RUNTIME | UNKNOWN | NOT_REQUIRED]
USER_PLUGIN_INVOCATION = [NOT_REQUIRED | REQUIRED_IF_ACTUALLY_USED | REQUIRED_BEFORE_DEPENDENT_STEP]
PLUGIN_PURPOSE = [...]

⚙️ EXECUÇÃO NATIVA
NATIVE_EXECUTION_SUFFICIENT = [YES | NO | PARTIAL]
NATIVE_EXECUTION_PURPOSE = [...]

Estratégia multiagente: [...]
Responsabilidade pela implementação: [...]
Critério de escalonamento: [...]

IDIOMA OBRIGATÓRIO:
RESPONDA SEMPRE EM PORTUGUÊS DO BRASIL (pt-BR).
```

`NONE` é decisão explícita válida. Modelo, esforço, multiagente e
skills/plugins são decisões independentes: modelo forte não implica
subagente; Astra não implica esforço alto; complexidade não implica plugin;
disponibilidade não implica uso; review não implica segundo agente.

## 5. Native-first, seleção e disponibilidade

```text
NATIVE_EXECUTION = PREFERRED_WHEN_SUFFICIENT
PLUGIN_INSTALLED != PLUGIN_REQUIRED
SKILL_AVAILABLE != SKILL_REQUIRED
USE_ONLY_WITH_MATERIAL_BENEFIT = YES
TOOL_SPRAWL = PROHIBITED
```

Quando a capacidade nativa resolve a tarefa de modo simples e seguro:

```text
NATIVE_EXECUTION_SUFFICIENT = YES
→ PREFER_NATIVE_EXECUTION
→ SKILL = NONE
→ PLUGIN = NONE
```

Skill oficial OpenAI só é considerada se alinhada à tarefa, disponível na
superfície, com benefício material e sem sobreposição inaceitável. Se fator
crítico não for confirmável, usar `SKILL_AVAILABILITY = VERIFY_AT_RUNTIME`;
nunca inventar a skill. Plugin aprovado só é considerado quando acrescenta
capability material que execução nativa ou skill isolada não fornece. Não usar
por curiosidade, instalação, prevenção, credenciais dispensáveis ou quando
nativo basta.

`PLUGIN_INSTALLED != PLUGIN_AVAILABLE_IN_SURFACE`,
`PLUGIN_AVAILABLE != APP_CONNECTED`, `PLUGIN_AVAILABLE != WRITE_AUTHORIZED` e
`SKILL_KNOWN != SKILL_AVAILABLE`. Não presumir disponibilidade.

## 6. Disposição, invocação e segurança de plugins

```text
PLUGIN_USE = NONE
→ USER_PLUGIN_INVOCATION = NOT_REQUIRED

PLUGIN_USE = OPTIONAL_IF_MATERIAL
→ USER_PLUGIN_INVOCATION = REQUIRED_IF_ACTUALLY_USED

PLUGIN_USE = REQUIRED
→ USER_PLUGIN_INVOCATION = REQUIRED_BEFORE_DEPENDENT_STEP
```

`NONE` significa que não será usado. Em `OPTIONAL_IF_MATERIAL`, não usar não
exige invocação; se decidir usar, deve notificar, solicitar invocação/seleção e
aguardar. Em `REQUIRED`, identificar o plugin, explicar motivo, solicitar
invocação e aguardar antes da etapa dependente.

```text
PLUGIN_ACTUAL_USE_INTENDED = YES
→ AGENT_MUST_NOTIFY_USER = YES
→ USER_PLUGIN_INVOCATION_REQUIRED = YES
→ AGENT_MUST_WAIT_FOR_USER_CONFIRMATION = YES
→ DEPENDENT_STEP_EXECUTION_BEFORE_CONFIRMATION = PROHIBITED

SILENT_PLUGIN_USE = PROHIBITED
SILENT_REQUIRED_PLUGIN_SUBSTITUTION = PROHIBITED
PLUGIN_AVAILABILITY_ASSUMPTION = PROHIBITED
```

A regra vale inclusive quando a plataforma permitir seleção automática. Se
plugin `REQUIRED` não estiver disponível, parar a etapa dependente, relatar e
não simular/substituir silenciosamente. Quando `OPTIONAL_IF_MATERIAL` não for
usado e nativo for suficiente, o fallback nativo é permitido e deve ser
registrado.

Capability não é permissão. Plugin não autoriza automaticamente commit, push,
merge, deploy, delete, migration, ação em produção, mensagem, billing, escrita
de banco ou manipulação de secrets:

```text
PLUGIN_CAPABILITY != WRITE_AUTHORIZATION
CAPABILITY != PERMISSION
```

## 7. Fluxo, relatório e princípios finais

1. Enquadrar objetivo, authorities, restrições, risco e verificabilidade.
2. Classificar a carga em `R1 | R2 | R3 | R4`.
3. Avaliar primeiro se Luna ou Terra são suficientes.
4. Antes de Sol, aplicar `ROUTINE_EXECUTION_GATE` e `SOL_GATE`.
5. Antes de Astra, aplicar `ASTRA_SELECTION_GATE` completo.
6. Selecionar separadamente o menor `REASONING_EFFORT` suficiente.
7. Verificar disponibilidade do modelo somente quando relevante para execução.
8. Aplicar independentemente o gate multiagente.
9. Aplicar independentemente as regras native/skill/plugin.
10. Executar no escopo autorizado.
11. Validar e realizar self-review proporcional.
12. Escalar modelo somente por `CAPABILITY_GAP`.
13. Escalar esforço somente por `DELIBERATION_GAP`.
14. Não usar modelo/esforço para compensar informação, acesso ou authority ausente.
15. Registrar justificativa específica sempre que Sol, Astra ou effort acima do
    default forem usados.
16. Para workloads recorrentes, recalibrar com evidência local de sucesso,
    retrabalho e consumo.

O relatório final deve informar, quando aplicável:

```text
TASK_CLASS
MODEL
REASONING_EFFORT
ROUTINE_EXECUTION_GATE
SOL_GATE
ASTRA_SELECTION_GATE
MODEL_SELECTION_REASON
WHY_THIS_REASONING_EFFORT
```

Se Sol for usado:

```text
SOL_TRIGGER
EXPECTED_SOL_GAIN
WHY_TERRA_IS_NOT_PREFERRED
```

Se Astra for usado:

```text
ASTRA_HARD_TRIGGER
WHY_SOL_IS_NOT_PREFERRED
EXPECTED_ASTRA_GAIN
ASTRA_USAGE_COST_ACCEPTABLE
```

Commit, push, publicação ou ação externa continuam exigindo autorização
explícita.

```text
MODEL_SELECTION_MASTER_RULES =

NORMAL_OPERATION =
LUNA | TERRA

SOL =
ESCALATION_ONLY

ASTRA =
EXCEPTIONAL_CAPABILITY_ONLY

IF_SOL_GAIN_IS_UNCLEAR =
USE_LOWER_SUFFICIENT_MODEL

IF_ASTRA_GAIN_IS_UNCLEAR =
DO_NOT_USE_ASTRA

IF_EFFORT_GAIN_IS_UNCLEAR =
USE_LOWER_EFFORT

MODEL_SELECTION_MUST_OPTIMIZE_TOTAL_OUTCOME
NOT_MODEL_PRESTIGE

PROPOSED_POLICY_REVIEW = REQUIRED
POLICY_EFFECTIVE = NO
CANONICALIZATION_AUTHORIZED = NO
PROMOTION_AUTHORIZED = NO
```

### 7.1 Referências operacionais externas — não normativas

Esta revisão foi calibrada com documentação oficial OpenAI consultada em
2026-09-10. A documentação atual sustenta, em síntese operacional:

- GPT-6 Astra é o modelo de maior capacidade, voltado aos trabalhos end-to-end
  mais difíceis;
- GPT-5.6 Sol é destinado a trabalho profissional complexo;
- GPT-5.6 Terra busca equilíbrio entre capacidade, velocidade e custo no
  trabalho cotidiano;
- GPT-5.6 Luna é o modelo mais rápido e de menor custo da família GPT-5.6;
- modelo e reasoning effort são decisões separadas;
- maior reasoning effort pode consumir mais allowance e não garante resultado
  melhor;
- Astra Low pode superar Sol High em determinadas cargas;
- no Work/Codex, Astra pode consumir allowance mais rapidamente que Sol;
- Astra suporta múltiplos níveis de reasoning effort, mas a disponibilidade
  exata deve ser confirmada na superfície atual.

Essas referências são **evidência de calibração**, não authority normativa
permanente. Mudança futura de produto requer nova revisão antes de alterar esta
policy.

---
