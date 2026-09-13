# Política de Geração de Prompts Multiagente — v1.7-R2.md

```text
STATUS = PROPOSED_REVISION
LIFECYCLE = REVIEW_CANDIDATE
PREVIOUS_BASE = Politica-Prompts-Agente-v1.5-V2.md
CONSOLIDATES = Politica-Prompts-Agente-v1.7-R1.md
MULTIAGENT_ALIGNMENT = AGENTS-Multiagente-Generico-v1.7-R2.1-Roteamento-Economico
SCOPE = TRANSVERSAL
DOMAIN_SPECIFIC_CONTENT = PROHIBITED
BOUNDED_CYCLIC_EXECUTION_INCLUDED = NO
CANONICALIZATION = NO
PROMOTION = NO
USER_REVIEW_REQUIRED = YES
```

---

## 0. Finalidade

Esta política governa a criação de prompts de atividade para Work ou Codex.

Ela possui dois objetivos simultâneos:

1. escolher uma arquitetura de execução tecnicamente correta e economicamente racional;
2. entregar ao executor somente o contexto necessário para executar a atividade.

A política deve impedir dois desperdícios distintos:

```text
EXECUTION_WASTE =
UNNECESSARY_MODEL_COST
+ UNNECESSARY_REASONING_COST
+ UNNECESSARY_SUBAGENT_COST
+ UNNECESSARY_COORDINATION_COST

PROMPT_WASTE =
IRRELEVANT_EXECUTOR_CONTEXT
+ DUPLICATED_CONTEXT
+ INTERNAL_GOVERNANCE_REASONING_EXPOSED_TO_EXECUTOR
+ UNUSED_CAPABILITY_INFORMATION
```

Princípio central:

```text
THE_GENERATOR_MAY_REASON_BROADLY
THE_EXECUTOR_PROMPT_MUST_BE_NARROW
```

A análise necessária para escolher modelo, esforço, subagentes, Skills e Plugins
não precisa ser enviada integralmente ao Codex/Work.

---

## 1. Duas audiências, dois outputs

Toda geração de prompt deve separar obrigatoriamente:

```text
OUTPUT_A = EXECUTION_DECISION_CARD
AUDIENCE_A = USER

OUTPUT_B = EXECUTOR_PAYLOAD
AUDIENCE_B = CODEX | WORK
```

### 1.1 Regra de cópia

```text
USER_SHOULD_COPY_TO_EXECUTOR = OUTPUT_B_ONLY
```

O Card A existe para o usuário visualizar e auditar a decisão de roteamento.

O Card B contém o prompt executável.

Não misturar as duas audiências.

---

# PARTE I — DECISÃO INTERNA DO GERADOR

## 2. Internal Routing Worksheet — NÃO enviar ao executor

O agente gerador deve avaliar internamente, quando aplicável:

```text
TASK_CLASS
RISK
COGNITIVE_COMPLEXITY
OPERATIONAL_VOLUME
VERIFIABILITY
REVERSIBILITY

COGNITIVE_HOTSPOTS
MECHANICAL_WORK
OBJECTIVE_VALIDATION_WORK

ROUTINE_EXECUTION_GATE
SOL_GATE
ASTRA_SELECTION_GATE

PARALLEL_INDEPENDENT_FRONTS
DISTINCT_SPECIALIZATION_REQUIRED
MATERIAL_DECOMPOSITION_GAIN
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW
MATERIAL_INTELLIGENCE_ROUTING_GAIN

EXPECTED_MATERIAL_GAIN
HANDOFF_COST
DUPLICATED_CONTEXT_COST
INTEGRATION_COST
REDUNDANCY_CHECK
```

Esses campos são instrumentos de decisão.

Por padrão:

```text
INTERNAL_ROUTING_WORKSHEET
NOT_IN_EXECUTOR_PAYLOAD
```

Só transformar uma conclusão interna em instrução do executor quando ela alterar:

- ação;
- escopo;
- authority;
- ownership;
- delegation;
- validação;
- stop condition;
- output esperado.

---

## 3. Relevance Gate do payload

Antes de inserir qualquer informação no Card B, aplicar:

```text
EXECUTOR_RELEVANCE_TEST
```

Pergunta:

> Se eu remover esta informação, existe chance material de o Codex/Work executar
> uma ação diferente, ultrapassar o escopo, validar incorretamente, delegar
> incorretamente, parar no lugar errado ou produzir um output inadequado?

Se:

```text
NO
```

então:

```text
OMIT_FROM_EXECUTOR_PAYLOAD
```

### 3.1 Informação normalmente pertinente

Inclua quando aplicável:

- objetivo;
- resultado esperado;
- root oficial;
- branch/baseline quando forem gates reais;
- authorities que precisam ser consultadas;
- arquivos ou superfícies relevantes;
- escopo autorizado;
- não escopo material;
- invariantes;
- contrato congelado;
- critérios de aceite;
- ações concretas;
- ordem operacional quando necessária;
- subagentes efetivamente autorizados;
- ownership;
- write mode;
- validações;
- comandos necessários;
- regras de Git;
- ações externas autorizadas ou proibidas quando plausíveis;
- stop conditions;
- formato mínimo de retorno.

### 3.2 Informação normalmente NÃO pertinente

Não enviar ao executor por padrão:

- histórico de evolução da policy;
- explicação longa sobre por que outro modelo foi rejeitado;
- gates completos G1–G6;
- score interno de risco;
- lista completa de alternativas descartadas;
- cálculo narrativo de economicidade;
- justificativas de `NO` para papéis não usados;
- catálogo de Skills não selecionadas;
- catálogo de Plugins não selecionados;
- anti-patterns genéricos da policy;
- exemplos de conformidade;
- telemetria de governança sem impacto na atividade;
- rationale repetido em múltiplas seções;
- conteúdo de documento canônico que o executor pode ler diretamente;
- regras genéricas que não mudam a execução concreta.

---

## 4. Referenciar em vez de duplicar

Quando Codex/Work tiver acesso ao repositório ou arquivo:

```text
REFERENCE_CANONICAL_SOURCE
PREFER_OVER_COPYING_CANONICAL_SOURCE
```

Use:

```text
AUTHORITY_TO_READ =
<path exato>
```

e, quando possível:

```text
READ_ONLY_RELEVANT_SECTION =
<título, seção ou assunto necessário>
```

Não copie para o prompt dezenas ou centenas de linhas de um documento local
se o executor pode lê-lo no próprio workspace.

Exceção:

- valor congelado necessário para comparação;
- checksum esperado;
- invariant curto;
- requisito que precisa estar imediatamente visível;
- boundary crítico cuja omissão seria perigosa.

---

# PARTE II — MODELO E ESFORÇO

## 5. Configuração mínima suficiente

A configuração é composta por decisões independentes:

```text
MINIMUM_SUFFICIENT_CONFIGURATION =
MODEL
+ REASONING_EFFORT
+ EXECUTION_MODE
+ SKILL
+ PLUGIN
+ NATIVE_EXECUTION
```

Objetivo:

```text
EXPECTED_COST_PER_SUCCESSFUL_TASK
```

sujeito a:

```text
QUALITY
ROBUSTNESS
VERIFIABILITY
AUTHORITY_PRESERVATION
SCOPE_CONTROL
```

Não selecionar por prestígio ou disponibilidade.

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

---

## 6. Taxonomia operacional de modelos

```text
NORMAL_OPERATING_RANGE =
LUNA | TERRA

SOL =
ESCALATION_MODEL

ASTRA =
EXCEPTIONAL_CAPABILITY_MODEL
```

### 6.1 Luna

Preferido para:

- trabalho focado;
- repetitivo;
- mecânico;
- baixo em ambiguidade;
- volumoso e sensível a custo;
- execução derivada de decisão já tomada.

Para subagentes:

```text
LUNA_DEFAULT = HIGH
LUNA_ANALYTICAL = XHIGH_WHEN_SUPPORTED
```

A política de subagentes não deve voltar a usar Luna Low/Medium como default.

### 6.2 Terra

Default para:

- trabalho técnico cotidiano;
- julgamento moderado;
- integração conhecida;
- implementação não puramente mecânica.

```text
TERRA_ROOT_BASELINE = MEDIUM
```

Terra/High é usado quando existe julgamento técnico elevado.

### 6.3 Sol

Sol é elegível apenas quando:

```text
SOL_GATE = PASS
```

Triggers materiais incluem:

```text
DIFFICULT_MULTI_COMPONENT_INTEGRATION
HARD_BUT_BOUNDED_DEBUGGING
MATERIAL_CONTRACT_OR_INVARIANT_REASONING
DEEP_CROSS_DOCUMENT_SYNTHESIS
NONTRIVIAL_ARCHITECTURAL_DECISION
MULTIPLE_INTERDEPENDENT_TECHNICAL_CONSTRAINTS
TERRA_EXPECTED_TO_REQUIRE_MATERIAL_REWORK
```

Também:

```text
EXPECTED_SOL_GAIN = MATERIAL
TERRA_EXPECTED_SUFFICIENCY = NO | MATERIALLY_INFERIOR
```

### 6.4 Astra

Astra é excepcional.

Somente elegível quando:

```text
ASTRA_SELECTION_GATE = PASS
```

Exige cumulativamente:

```text
ASTRA_HARD_TRIGGER = PRESENT
EXPECTED_ASTRA_GAIN = MATERIAL
WHY_SOL_IS_NOT_PREFERRED = CONCRETE
ASTRA_USAGE_COST_ACCEPTABLE = YES
```

Hard triggers podem incluir:

```text
OPEN_ENDED_UNFAMILIAR_PROBLEM
MATERIAL_NOVELTY_WITH_NO_CLEAR_SOLUTION_PATTERN
EXCEPTIONALLY_DIFFICULT_CAUSAL_DEBUGGING
HARD_END_TO_END_REASONING_ACROSS_MULTIPLE_SYSTEMS
FRONTIER_TECHNICAL_OR_SCIENTIFIC_REASONING
VERY_DIFFICULT_LONG_CONTEXT_RECONCILIATION
HIGH_COMPLEXITY_COMPUTER_OR_TOOL_ORCHESTRATION
SOL_CAPABILITY_ALREADY_OBSERVED_AS_INSUFFICIENT
```

### 6.5 Modelo e esforço são independentes

```text
MODEL != REASONING_EFFORT

CAPABILITY_GAP
→ CONSIDER_STRONGER_MODEL

DELIBERATION_GAP
→ CONSIDER_HIGHER_EFFORT

MISSING_INFORMATION_OR_ACCESS
→ ACQUIRE_INFORMATION_OR_STOP
```

Nunca usar modelo ou esforço para compensar:

- arquivo ausente;
- contexto ausente;
- requisito ausente;
- permission ausente;
- tool/plugin ausente;
- authority ausente.

---

# PARTE III — ROTEAMENTO MULTIAGENTE

## 7. ROOT antes dos subagentes

Decidir primeiro:

```text
ORCHESTRATOR_MODEL
ORCHESTRATOR_EFFORT
```

Depois avaliar subagentes.

```text
ROOT_CAN_EXECUTE != ROOT_SHOULD_EXECUTE
LOWER_TIER_CAN_EXECUTE != LOWER_TIER_SHOULD_EXECUTE
```

---

## 8. DIRECT vs MULTIAGENT

### 8.1 DIRECT

Preferir DIRECT quando:

- trabalho pequeno;
- contexto pequeno;
- ROOT já possui contexto suficiente;
- decomposição não reduz custo/risco/contexto;
- handoff custa mais que a economia;
- não existe independência obrigatória;
- não existe especialização material separável.

```text
IF_BENEFIT_IS_UNCLEAR = DIRECT
```

### 8.2 MULTIAGENT

Multiagente exige ganho material demonstrável.

```text
MULTIAGENT != PARALLELISM
```

Pipeline sequencial é válido.

Exemplo:

```text
ROOT
→ IMPLEMENTER
→ VALIDATOR
→ ROOT
```

---

## 9. G6 — Material Intelligence Routing Gain

```text
HIGHER_TIER_REQUIRED_FOR_REASONING = YES
AND LOWER_TIER_CAPABLE_OF_BOUNDED_EXECUTION = YES
AND DELEGATED_WORK_IS_OBJECTIVELY_VERIFIABLE = YES
AND HANDOFF_SCOPE_IS_CLEAR = YES
AND EXPECTED_COST_SAVING > COORDINATION_OVERHEAD
→ MULTIAGENT_ALLOWED
```

Inteligência cara deve permanecer no hotspot cognitivo.

Trabalho bounded e verificável deve ser avaliado para tier inferior.

---

## 10. Redundancy Gate

Antes de criar subagente:

```text
DOES_ROOT_ALREADY_COVER_THIS_ROLE_SUFFICIENTLY?
```

Se sim, exigir pelo menos um:

```text
INDEPENDENCE_REQUIRED = YES
DISTINCT_SPECIALIZATION_GAIN = YES
MATERIAL_ECONOMIC_GAIN = YES
MATERIAL_RISK_REDUCTION = YES
```

Senão:

```text
DO_NOT_SPAWN
```

Regra:

```text
DO_NOT_DUPLICATE_EXPENSIVE_INTELLIGENCE_WITHOUT_DISTINCT_VALUE
```

---

## 11. Papéis preferenciais

```text
SCOUT                  = LUNA / HIGH / READ_ONLY
RESEARCHER             = LUNA / XHIGH / READ_ONLY
VALIDATOR              = LUNA / HIGH / VALIDATION
TRIAGE_ANALYST         = LUNA / XHIGH / READ_ONLY
MECHANICAL_IMPLEMENTER = LUNA / HIGH / WORKSPACE_WRITE_BOUNDED
SCRIBE                 = LUNA / HIGH / DOCUMENTATION_BOUNDED
IMPLEMENTER            = TERRA / MEDIUM_OR_HIGH / WORKSPACE_WRITE
REVIEWER               = TERRA / HIGH / READ_ONLY
SECURITY_REVIEWER      = TERRA / HIGH / READ_ONLY
ARCHITECT              = SOL / HIGH / READ_ONLY
```

Disponibilidade real deve ser confirmada no ambiente.

### 11.1 Mechanical Implementer

Somente quando:

```text
SOLUTION_CLOSED = YES
INVARIANTS_CLOSED = YES
SCOPE_BOUNDED = YES
OWNERSHIP_CLEAR = YES
OBJECTIVE_VALIDATION_AVAILABLE = YES
MATERIAL_NET_GAIN = YES
```

### 11.2 Implementer

Use Terra quando ainda houver:

- julgamento técnico;
- integração;
- interpretação local;
- escolhas de implementação;
- entendimento de fluxo.

### 11.3 Validator

```text
VALIDATOR_VALIDATES
VALIDATOR_DOES_NOT_IMPLEMENT
```

Ferramentas podem gerar artefatos transitórios:

```text
TECHNICAL_WORKSPACE_WRITE_CAPABILITY = ALLOWED_WHEN_REQUIRED
SOURCE_WRITE_AUTHORIZATION = NO
```

### 11.4 Reviewer

```text
IMPLEMENTATION_COMPLETE != REVIEWER_REQUIRED
```

Se:

```text
ROOT_CAPABILITY >= REVIEW_REQUIREMENT
AND INDEPENDENT_REVIEW_REQUIRED = NO
```

então:

```text
ROOT_SELF_REVIEW = YES
REVIEWER = NO
```

### 11.5 Triage

```text
TEST_FAIL != TRIAGE_REQUIRED
```

Triage só entra com ganho diagnóstico material.

---

# PARTE IV — SKILLS, PLUGINS E EXECUÇÃO NATIVA

## 12. Taxonomia

```text
CAPABILITY != SKILL
SKILL != PLUGIN
PLUGIN_MAY_CONTAIN_SKILLS = YES
SKILL_MAY_EXIST_WITHOUT_PLUGIN = YES
NAME_SYNTAX_DOES_NOT_DEFINE_CLASS = YES
```

Capacidade nativa = função já disponível diretamente.

Skill = workflow, procedimento ou guidance reutilizável.

Plugin = recurso empacotado que pode fornecer skill, app, template, ferramenta ou integração.

Nenhum transfere authority.

---

## 13. Native-first

```text
NATIVE_EXECUTION = PREFERRED_WHEN_SUFFICIENT

PLUGIN_INSTALLED != PLUGIN_REQUIRED
SKILL_AVAILABLE != SKILL_REQUIRED

USE_ONLY_WITH_MATERIAL_BENEFIT = YES
TOOL_SPRAWL = PROHIBITED
```

Se nativo for suficiente:

```text
NATIVE_EXECUTION_SUFFICIENT = YES
SKILL = NONE
PLUGIN = NONE
```

---

## 14. Skills

Classificar apenas com evidência da superfície/runtime/documentação/catálogo
operacional aplicável.

Sem confirmação:

```text
SKILL_AVAILABILITY = VERIFY_AT_RUNTIME
```

Não inventar Skill.

`NONE` é decisão válida.

---

## 15. Plugins

Plugin só deve ser recomendado quando acrescentar capability material que o
nativo ou a Skill escolhida não fornecem adequadamente.

```text
PLUGIN_USE =
NONE
| OPTIONAL_IF_MATERIAL
| REQUIRED
```

Regra:

```text
PLUGIN_CAPABILITY != WRITE_AUTHORIZATION
CAPABILITY != PERMISSION
```

Se o ambiente exigir ação explícita do usuário para conectar/invocar o Plugin,
o prompt gerador deve informar isso no Card A.

Não inserir no payload do executor instruções sobre Plugins que não serão usados.

---

# PARTE V — FORMATO OBRIGATÓRIO DE SAÍDA

## 16. CARD A — EXECUTION DECISION CARD

Este card é para o usuário.

Deve aparecer no início da resposta do agente que está gerando a atividade.

Deve ser curto.

Formato:

```text
┌─────────────────────────────────────────────────────────────┐
│ EXECUTION CARD — NÃO COPIAR PARA O CODEX/WORK              │
├─────────────────────────────────────────────────────────────┤
│ AMBIENTE            = CODEX | WORK                          │
│ ORCHESTRATOR        = <MODEL> / <EFFORT>                    │
│ EXECUTION_MODE      = DIRECT | MULTIAGENT                   │
│ SUBAGENTS           = <NONE | perfis efetivamente usados>   │
│ SKILL               = <NONE | nome + uso>                   │
│ PLUGIN              = <NONE | nome + uso>                   │
│ NATIVE_EXECUTION    = YES | PARTIAL | NO                    │
│ ESCALATION          = <regra curta>                         │
├─────────────────────────────────────────────────────────────┤
│ COPY_TO_EXECUTOR    = CARD B ONLY                           │
└─────────────────────────────────────────────────────────────┘
```

### 16.1 Rationale no Card A

Adicionar no máximo uma justificativa curta quando materialmente útil.

Exemplo:

```text
RATIONALE =
Terra/High fecha o hotspot; Luna/High executa validação objetiva.
```

Não despejar no card:

- G1–G6;
- rejected alternatives;
- score de risco;
- long model rationale;
- policy history.

### 16.2 Sol/Astra

Se Sol ou Astra forem selecionados, Card A deve acrescentar somente o motivo
mínimo necessário:

```text
ESCALATION_REASON =
<1–2 linhas>
```

A análise completa do gate permanece interna.

---

## 17. CARD B — EXECUTOR PAYLOAD

Este é o único bloco que deve ser enviado ao Codex/Work.

Formato base:

```text
┌─────────────────────────────────────────────────────────────┐
│ EXECUTOR PAYLOAD — COPIAR ESTE BLOCO PARA CODEX/WORK       │
└─────────────────────────────────────────────────────────────┘

AMBIENTE = CODEX | WORK
IDIOMA = pt-BR
ROLE = ROOT_ORCHESTRATOR

OBJETIVO
<resultado concreto>

AUTHORITIES
<somente authorities que o executor precisa consultar>

ESCOPO AUTORIZADO
<ações/arquivos/superfícies permitidos>

NÃO ESCOPO
<somente proibições materialmente plausíveis>

INVARIANTES / CONTRATOS
<somente os necessários>

ATIVIDADE
<passos executáveis>

DELEGAÇÃO
<somente se MULTIAGENT>

VALIDAÇÃO
<comandos e critérios realmente necessários>

GIT / AÇÕES EXTERNAS
<permissões e proibições pertinentes>

STOP CONDITIONS
<condições reais de parada>

RETORNO
<formato mínimo>
```

Se uma seção não for relevante:

```text
OMIT_SECTION
```

Não preencher com `NONE` apenas para manter template.

---

## 18. Minimal Payload Rule

O Card B não é um relatório de governança.

É um contrato de execução.

Aplicar:

```text
MINIMUM_SUFFICIENT_EXECUTOR_CONTEXT = REQUIRED
```

O gerador deve procurar remover, não adicionar, informação.

Antes de finalizar:

```text
FOR_EACH_PARAGRAPH:
    DOES_THIS_CHANGE_EXECUTION?
    IF NO:
        DELETE_OR_MOVE_TO_CARD_A_IF_USER_RELEVANT
```

---

## 19. Proibições do Card B

Não inserir automaticamente:

```text
TASK_CLASS
RISK
COGNITIVE_COMPLEXITY
OPERATIONAL_VOLUME
VERIFIABILITY
REVERSIBILITY

ROUTINE_EXECUTION_GATE
SOL_GATE
ASTRA_SELECTION_GATE

PARALLEL_INDEPENDENT_FRONTS
DISTINCT_SPECIALIZATION_REQUIRED
MATERIAL_DECOMPOSITION_GAIN
MATERIAL_INTELLIGENCE_ROUTING_GAIN

EXPECTED_MATERIAL_GAIN
COORDINATION_COST
DUPLICATED_CONTEXT_COST

ROOT_CAPABILITY_REDUNDANCY_CHECK
REDUNDANCY_GATE_ANALYSIS

MODEL_SELECTION_REASON
WHY_TERRA_IS_NOT_PREFERRED
WHY_SOL_IS_NOT_PREFERRED

WHY_ROOT_SHOULD_NOT_DO_THIS_WORK
EXPECTED_ECONOMIC_GAIN
```

Esses itens permanecem internos ou no Card A de forma condensada.

Exceção: inserir um deles somente quando seu valor for necessário para uma
decisão que o executor terá de tomar durante a atividade.

---

## 20. Delegação compacta no Card B

Se MULTIAGENT, não repetir um enorme bloco por agente.

Definir primeiro boundaries compartilhados:

```text
SHARED_DELEGATION_BOUNDARIES
- não ampliar escopo;
- não transferir authority;
- não executar Git consequencial sem autorização;
- não delegar recursivamente, salvo regra explícita.
```

Depois cada agente recebe apenas:

```text
SUBAGENT = <profile>
OBJECTIVE = <objetivo estreito>
OWNERSHIP = <arquivos/superfície>
WRITE_MODE = <modo>
RETURN = <evidência mínima>
```

Adicionar `MUST_NOT` individual apenas se existir proibição específica daquele
papel que não esteja coberta pelos boundaries compartilhados.

---

## 21. Authorities compactas

Não copiar documentos canônicos extensos.

Preferir:

```text
AUTHORITIES_TO_READ
1. <path> — ler somente <seção/tema>
2. <path> — usar como authority para <decisão>
```

Se um valor exato for gate:

```text
EXPECTED_VALUE =
<valor>
```

pode ser incluído diretamente.

---

## 22. Background filter

Contexto histórico só entra no Card B se alterar a execução atual.

Não incluir por padrão:

- história da sprint;
- commits antigos sem efeito no baseline atual;
- decisões superadas;
- tentativas anteriores já irrelevantes;
- narrativa de como a arquitetura evoluiu;
- explicações para o usuário compreender o projeto.

Codex/Work precisa de estado operacional atual, não de biografia do projeto.

---

## 23. Negative-boundary filter

Não listar dezenas de proibições genéricas.

Uma proibição entra somente se:

```text
ACTION_IS_PLAUSIBLE_IN_THIS_TASK = YES
OR CONSEQUENCE_IS_HIGH_IF_MISTAKEN = YES
OR GOVERNANCE_REQUIRES_EXPLICIT_BOUNDARY = YES
```

Exemplo:

Se a tarefa é read-only:

```text
SOURCE_WRITE = PROHIBITED
GIT_CONSEQUENTIAL = PROHIBITED
```

pode bastar.

Não é necessário repetir todas as operações impossíveis ou irrelevantes.

---

## 24. Validation filter

Enviar somente validações necessárias ao executor.

Não explicar no Card B por que cada validação foi escolhida.

Formato preferido:

```text
VALIDATION
1. <comando>
   EXPECTED = <critério>
2. <comando>
   EXPECTED = <critério>
```

Se o ROOT deve interpretar uma divergência:

```text
ON_MISMATCH =
REPORT_AND_ADJUDICATE
```

---

## 25. Output contract mínimo

Não exigir relatório gigantesco por padrão.

Formato base:

```text
FINAL_REPORT
STATUS =
FILES_CHANGED =
VALIDATIONS =
FINDINGS =
BLOCKERS =
UNAUTHORIZED_CHANGES = YES | NO
GIT_ACTIONS = NONE | <ações autorizadas realmente executadas>
FINAL_VERDICT =
```

Adicionar campos apenas quando materialmente necessários.

---

# PARTE VI — REGRAS DE GERAÇÃO

## 26. Fluxo interno do gerador

1. entender objetivo;
2. identificar authority;
3. classificar carga cognitiva;
4. escolher modelo e esforço;
5. escolher ROOT;
6. identificar hotspot;
7. identificar trabalho mecânico;
8. identificar validação objetiva;
9. avaliar DIRECT;
10. avaliar multiagente e G6;
11. aplicar Redundancy Gate;
12. escolher subagentes mínimos;
13. avaliar execução nativa;
14. avaliar Skill;
15. avaliar Plugin;
16. montar Card A;
17. construir Card B aplicando `EXECUTOR_RELEVANCE_TEST`;
18. executar uma `PROMPT_COMPRESSION_PASS`;
19. entregar.

---

## 27. Prompt Compression Pass

Antes de entregar Card B:

```text
PROMPT_COMPRESSION_PASS = REQUIRED
```

Verificar:

```text
DUPLICATED_INFORMATION = REMOVE
INTERNAL_REASONING = REMOVE
REJECTED_ALTERNATIVES = REMOVE
UNUSED_CAPABILITIES = REMOVE
GENERIC_POLICY_TEXT = REMOVE
REDUNDANT_PROHIBITIONS = COLLAPSE
CANONICAL_TEXT_AVAILABLE_BY_PATH = REFERENCE
REPEATED_RATIONALE = REMOVE
NON_ACTIONABLE_HISTORY = REMOVE
```

Objetivo:

```text
EVERY_REMAINING_LINE
MUST_HAVE_EXECUTION_VALUE
```

---

## 28. Escalonamento durante execução

Escalar modelo apenas por:

```text
CAPABILITY_GAP
```

Escalar effort apenas por:

```text
DELIBERATION_GAP
```

Falha causada por input, permission, arquivo, tool ou authority ausente não é
capability gap.

Quando o hotspot termina, considerar de-escalonamento.

---

## 29. Review

```text
IMPLEMENTATION_COMPLETE != REVIEWER_REQUIRED
```

Se ROOT cobre review e não existe independência obrigatória:

```text
ROOT_SELF_REVIEW = YES
REVIEWER = NO
```

Independent Reviewer só entra quando independência ou ganho distinto real
justificar.

---

## 30. Triage

```text
TEST_FAIL != TRIAGE_REQUIRED
```

Falha autoexplicativa pode ser tratada diretamente pelo ROOT ou executor
apropriado.

---

## 31. Git e ações externas

Prompt não autoriza implicitamente:

- commit;
- push;
- tag;
- release;
- deploy;
- alteração LIVE;
- publicação;
- exclusão externa;
- mensagem externa.

Incluir no Card B apenas os boundaries pertinentes à atividade.

---

# PARTE VII — EXEMPLOS DE SAÍDA

## 32. Exemplo — DIRECT

```text
┌─────────────────────────────────────────────────────────────┐
│ EXECUTION CARD — NÃO COPIAR PARA O CODEX/WORK              │
├─────────────────────────────────────────────────────────────┤
│ AMBIENTE         = CODEX                                    │
│ ORCHESTRATOR     = TERRA / MEDIUM                           │
│ EXECUTION_MODE   = DIRECT                                   │
│ SUBAGENTS        = NONE                                     │
│ SKILL            = NONE                                     │
│ PLUGIN           = NONE                                     │
│ NATIVE_EXECUTION = YES                                      │
│ ESCALATION       = somente capability gap material          │
├─────────────────────────────────────────────────────────────┤
│ COPY_TO_EXECUTOR = CARD B ONLY                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ EXECUTOR PAYLOAD — COPIAR ESTE BLOCO PARA CODEX/WORK       │
└─────────────────────────────────────────────────────────────┘

AMBIENTE = CODEX
IDIOMA = pt-BR
ROLE = ROOT_ORCHESTRATOR

OBJETIVO
Corrigir o mapeamento localizado já especificado.

ESCOPO AUTORIZADO
- editar o formatter;
- ajustar o teste correspondente se necessário.

VALIDAÇÃO
- executar teste focal;
- executar check estático padrão se aplicável.

GIT / AÇÕES EXTERNAS
- commit/push não autorizados.

RETORNO
- arquivos alterados;
- validações;
- resultado final.
```

---

## 33. Exemplo — MULTIAGENT econômico

```text
┌─────────────────────────────────────────────────────────────┐
│ EXECUTION CARD — NÃO COPIAR PARA O CODEX/WORK              │
├─────────────────────────────────────────────────────────────┤
│ AMBIENTE         = CODEX                                    │
│ ORCHESTRATOR     = TERRA / HIGH                             │
│ EXECUTION_MODE   = MULTIAGENT                               │
│ SUBAGENTS        = luna_worker, luna_validator              │
│ SKILL            = NONE                                     │
│ PLUGIN           = NONE                                     │
│ NATIVE_EXECUTION = YES                                      │
│ ESCALATION       = somente ambiguidade/capability gap       │
├─────────────────────────────────────────────────────────────┤
│ COPY_TO_EXECUTOR = CARD B ONLY                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ EXECUTOR PAYLOAD — COPIAR ESTE BLOCO PARA CODEX/WORK       │
└─────────────────────────────────────────────────────────────┘

AMBIENTE = CODEX
IDIOMA = pt-BR
ROLE = ROOT_ORCHESTRATOR
EXECUTION_MODE = MULTIAGENT

OBJETIVO
Corrigir o cálculo conforme o contrato congelado.

ROOT RESPONSIBILITIES
- fechar a decisão técnica;
- definir invariantes;
- congelar o contrato bounded;
- revisar diff/evidências;
- adjudicar resultado final.

SHARED_DELEGATION_BOUNDARIES
- não ampliar escopo;
- não alterar contrato;
- não executar commit/push;
- não delegar recursivamente.

SUBAGENT = luna_worker
OBJECTIVE = aplicar somente o patch prescrito e testes definidos pelo ROOT.
OWNERSHIP = arquivos explicitamente atribuídos pelo ROOT.
WRITE_MODE = bounded source/test write.
RETURN = diff summary + arquivos alterados.

SUBAGENT = luna_validator
OBJECTIVE = executar validações objetivas e retornar evidências.
OWNERSHIP = validation only.
WRITE_MODE = transient artifacts only; source write prohibited.
RETURN = resultados exatos + blockers.

VALIDAÇÃO
- testes focais;
- suíte aplicável;
- análise estática;
- diff check.

ON_VALIDATION_FAILURE
- reportar ao ROOT;
- não criar Triage automaticamente.

RETORNO
- diff final;
- resultados das validações;
- blockers;
- veredicto do ROOT.
```

---

# PARTE VIII — PRINCÍPIOS FINAIS

## 34. Regras mestres

1. O gerador pode raciocinar amplamente; o executor recebe contexto estreito.
2. Card A é para o usuário; Card B é para Codex/Work.
3. O usuário copia somente Card B.
4. Escolha ROOT antes de subagentes.
5. Modelo, effort, multiagente, Skill e Plugin são decisões independentes.
6. Luna/Terra são a faixa normal; Sol/Astra exigem gates materiais.
7. `ROOT_CAN_EXECUTE != ROOT_SHOULD_EXECUTE`.
8. Multiagente não exige paralelismo.
9. G6 permite tiering econômico sequencial.
10. Reviewer não é ritual.
11. Triage não é ritual.
12. Validator não implementa.
13. Delegação não transfere authority.
14. Skills e Plugins não transferem authority.
15. Native-first quando suficiente.
16. Skill disponível não implica Skill necessária.
17. Plugin instalado não implica Plugin necessário.
18. Nenhuma informação entra no Card B sem passar pelo `EXECUTOR_RELEVANCE_TEST`.
19. Authority extensa deve ser referenciada por path, não reproduzida.
20. O Card B deve passar por `PROMPT_COMPRESSION_PASS`.
21. O relatório final deve ser mínimo e suficiente.
22. Commit, push, deploy e ações externas exigem autorização explícita.
23. Bounded Cyclic Execution permanece fora desta revisão.
24. Se o ganho de delegação for incerto, permanecer DIRECT.
25. Se o ganho de Sol/Astra for incerto, usar o menor modelo suficiente.

---

## 35. Estado desta revisão

```text
VERSION = v1.5-V2-R1
STATUS = PROPOSED_REVISION

CONSOLIDATES_ECONOMIC_MULTIAGENT_ROUTING = YES
CONSOLIDATES_SOL_ASTRA_MODEL_GATES = YES
CONSOLIDATES_SKILL_PLUGIN_NATIVE_TAXONOMY = YES

DUAL_AUDIENCE_OUTPUT = YES
EXECUTION_DECISION_CARD = REQUIRED
EXECUTOR_PAYLOAD_CARD = REQUIRED
COPY_ONLY_EXECUTOR_PAYLOAD = YES

EXECUTOR_RELEVANCE_TEST = REQUIRED
PROMPT_COMPRESSION_PASS = REQUIRED
INTERNAL_ROUTING_WORKSHEET_EXPOSED_TO_EXECUTOR = NO

BOUNDED_CYCLIC_EXECUTION = EXCLUDED

READY_FOR_USER_REVIEW = YES
CANONICAL_PROMOTION = PENDING_USER_APPROVAL
```
