# Política de Geração de Prompts Multiagente — v1.7

```text
STATUS = PROPOSED
LIFECYCLE = DRAFT
CANONICAL_AUTHORITY_BASELINE = Politica-Prompts-Agente-v1.4.md
CONTENT_BASELINE = Politica-Prompts-Agente-v1.6.md
CONTENT_BASELINE_STATUS = PREVIOUS CONSOLIDATED CANDIDATE
MULTIAGENT_CHANGE_SOURCE = GOV-02
SKILLS_PLUGINS_CHANGE_SOURCE = GOV-05
MODEL_TAXONOMY_CHANGE_SOURCE = GPT-6_ASTRA_UPDATE_2026-09
CHANGE_SCOPE = MODEL_SELECTION_AND_REASONING_EFFORT_WITH_ASTRA
MULTIAGENT_RULES_CHANGE = NO
SKILLS_PLUGINS_RULES_CHANGE = NO
CANONICALIZATION = NO
PROMOTION = NO
DOMAIN_SPECIFIC_CONTENT = PROHIBITED
UNRELATED_NORMATIVE_CHANGE = PROHIBITED
USER_REVIEW_REQUIRED = YES
```

> Esta é uma candidata controlada derivada da v1.6. A v1.4 permanece a
> autoridade canônica até promoção formal. A v1.7 introduz somente a atualização
> de seleção de modelo e esforço necessária para incorporar GPT-6 Astra, sem
> alterar nesta atividade as regras de multiagente ou de Skills/Plugins. A criação
> desta candidata não a torna vigente e não autoriza canonicalização, propagação,
> pacote, Git ou qualquer ação externa.

## 0. Finalidade, escopo e versionamento

Esta política define como preparar prompts de atividade para Work ou Codex,
incluindo **modelo, esforço de raciocínio, estratégia multiagente, skills,
plugins e execução nativa**. É transversal, project-agnostic e self-contained.

A v1.7 deriva da v1.6 e altera somente o eixo de **seleção de modelo e esforço**
para incorporar GPT-6 Astra ao lado de GPT-5.6 Luna, Terra e Sol. As regras de
multiagente e Skills/Plugins permanecem preservadas nesta revisão e deverão ser
sincronizadas, em atividade separada, com a policy especializada correspondente.

O objetivo é escolher a menor combinação que entregue qualidade suficiente com
o menor custo total esperado, considerando:

- capacidade cognitiva necessária;
- profundidade de raciocínio;
- tempo;
- consumo de quota/créditos/tokens;
- risco de erro;
- custo de retrabalho;
- dificuldade de verificação;
- complexidade operacional.

```text
MINIMUM_SUFFICIENT_CONFIGURATION =
MODEL + REASONING_EFFORT + EXECUTION_MODE + SKILL + PLUGIN
```

Disponibilidade não implica necessidade:

```text
MODEL_AVAILABLE != MODEL_REQUIRED
STRONGER_MODEL != BETTER_DEFAULT
HIGHER_EFFORT != BETTER_RESULT
LONG_TASK != STRONGER_MODEL_REQUIRED
IMPORTANT_TASK != ASTRA_REQUIRED
```

Os nomes e disponibilidades de modelos podem variar entre ChatGPT Work, Codex,
Chat e API. Portanto, antes de recomendar um modelo cuja disponibilidade seja
relevante para a execução:

```text
MODEL_AVAILABILITY = CONFIRM_AT_RUNTIME
```

A política usa as funções operacionais atualmente atribuídas a:

```text
GPT-5.6 Luna
GPT-5.6 Terra
GPT-5.6 Sol
GPT-6 Astra
```

Mudança futura de geração ou nome comercial não deve alterar automaticamente os
princípios desta policy.

---

## 1. Modelo, esforço e categoria

### 1.1 Modelo e esforço são eixos independentes

**Modelo** representa a capacidade-base disponível para compreender, decidir,
integrar e executar a tarefa.

**Esforço de raciocínio** representa quanto dessa capacidade será empregada na
deliberação, investigação, comparação e verificação.

```text
MODEL != REASONING_EFFORT
MODEL_ESCALATION != EFFORT_ESCALATION
```

Uma tarefa pode precisar de modelo mais forte com esforço baixo, ou de um modelo
mais econômico com esforço maior.

Não presumir que:

```text
LOWER_MODEL + HIGH_EFFORT
>
STRONGER_MODEL + LOW_EFFORT
```

nem o inverso sem evidência da carga de trabalho.

A orientação operacional atual da OpenAI informa que GPT-6 Astra em esforço
baixo pode superar GPT-5.6 Sol em esforço alto em determinadas cargas. Portanto,
o agente deve avaliar **capacidade-base e esforço conjuntamente**, e não tratar
esforço como substituto automático de capacidade de modelo.

### 1.2 Papel operacional de cada modelo

#### GPT-5.6 Luna — execução focada e econômica

Preferir Luna quando o problema for claro, observável e com baixo grau de
julgamento aberto.

Adequado para:

- extração e classificação;
- edição curta;
- transformação mecânica;
- busca/localização objetiva;
- tarefas repetitivas;
- alterações pequenas com comportamento já definido;
- trabalho volumoso, porém conceitualmente simples;
- execução derivada de decisão já tomada.

```text
LUNA_DEFAULT_DOMAIN =
FOCUSED | REPETITIVE | MECHANICAL | LOW_AMBIGUITY
```

Não escalar para Terra, Sol ou Astra apenas porque a tarefa contém muitos
arquivos ou demora para executar.

#### GPT-5.6 Terra — trabalho cotidiano com julgamento moderado

Preferir Terra quando houver necessidade real de integrar contexto, interpretar
documentos, tomar decisões técnicas rotineiras ou executar trabalho profissional
cotidiano com equilíbrio entre velocidade, capacidade e consumo.

Adequado para:

- alteração de código rotineira;
- análise de documentos;
- relatório técnico;
- integração de componentes conhecidos;
- investigação moderada;
- comparação de alternativas bem delimitadas;
- consolidação de evidências;
- revisão que exija julgamento, mas não raciocínio de fronteira.

```text
TERRA_DEFAULT_DOMAIN =
EVERYDAY_TECHNICAL_WORK | MODERATE_JUDGMENT | MODERATE_INTEGRATION
```

Terra não deve ser promovido para Sol por prestígio, tamanho do projeto ou
preferência do agente.

#### GPT-5.6 Sol — trabalho complexo, porém suficientemente delimitado

Preferir Sol quando a tarefa exige capacidade forte de programação, pesquisa,
síntese ou trabalho profissional, mas o problema continua suficientemente
definido para não justificar o custo adicional do Astra.

Adequado para:

- implementação complexa e bem especificada;
- síntese de pesquisa extensa;
- análise técnica difícil, mas delimitada;
- integração de múltiplos componentes;
- debug difícil com espaço de hipóteses controlável;
- contratos e invariantes importantes;
- arquitetura com alternativas conhecidas;
- revisão profunda de sistema;
- trabalho longo que exige forte consistência e julgamento.

```text
SOL_DEFAULT_DOMAIN =
COMPLEX_BUT_BOUNDED | STRONG_JUDGMENT | DEEP_SYNTHESIS
```

Sol é o **modelo forte de uso geral**. Ele deve ser preferido ao Astra quando
entregar qualidade suficiente com menor consumo esperado.

#### GPT-6 Astra — problemas especialmente exigentes e end-to-end

Astra é o modelo de maior capacidade desta matriz e deve ser reservado para
situações em que sua inteligência-base superior produza ganho material.

Astra é adequado quando existir pelo menos um trigger material como:

```text
ASTRA_TRIGGERS =
UNFAMILIAR_OR_OPEN_ENDED_PROBLEM |
HARD_END_TO_END_MULTI_STEP_WORK |
MATERIAL_AMBIGUITY_OR_NOVELTY |
VERY_DIFFICULT_DEBUG_OR_CAUSALITY |
HIGH_COMPLEXITY_TOOL_OR_COMPUTER_USE |
VERY_LONG_CONTEXT_CROSS_SOURCE_REASONING |
FRONTIER_SCIENTIFIC_OR_TECHNICAL_REASONING |
HIGH_IMPACT_DECISION_WITH_DIFFICULT_VERIFICATION |
SOL_CAPABILITY_PROVEN_INSUFFICIENT
```

Um trigger isolado ainda não basta. Também deve existir:

```text
EXPECTED_ASTRA_MATERIAL_GAIN = YES
ASTRA_USAGE_COST_ACCEPTABLE = YES
LOWER_MODEL_SUFFICIENCY = NO | MATERIALLY_INFERIOR
```

Astra pode ser escolhido diretamente quando a natureza da tarefa já demonstrar
essas condições. Não é obrigatório desperdiçar uma tentativa anterior com Sol
para "provar" insuficiência.

Por outro lado:

```text
TASK_LONG = YES
!= ASTRA_REQUIRED

TASK_IMPORTANT = YES
!= ASTRA_REQUIRED

TASK_HIGH_RISK = YES
!= ASTRA_REQUIRED

TASK_HAS_MANY_FILES = YES
!= ASTRA_REQUIRED

ASTRA_AVAILABLE = YES
!= ASTRA_SHOULD_BE_USED
```

### 1.3 Astra é uma capacidade premium, não um default

A disponibilidade atual do Astra em Work/Codex pode consumir a quota incluída
mais rapidamente que GPT-5.6 Sol. Portanto:

```text
ASTRA_USAGE = SELECTIVE
ASTRA_BY_PRESTIGE = PROHIBITED
ASTRA_BY_AVAILABILITY = PROHIBITED
ASTRA_FOR_ROUTINE_WORK = PROHIBITED
```

O custo relevante não é apenas consumo bruto. Deve-se considerar custo total:

```text
EXPECTED_TOTAL_COST =
MODEL_USAGE
+ LATENCY
+ REWORK
+ FAILURE_RISK
+ VERIFICATION_COST
```

Um modelo aparentemente mais caro pode ser economicamente correto se reduzir
materialmente retrabalho ou falhas. Da mesma forma, Astra é desperdício quando
Luna, Terra ou Sol resolvem adequadamente a tarefa.

### 1.4 Regra Sol Alto versus Astra Baixo/Médio

Quando a decisão estiver entre **Sol com alto esforço** e **Astra com esforço
baixo ou médio**, não aplicar uma regra hierárquica cega.

Avaliar:

```text
NEED_STRONGER_BASE_INTELLIGENCE
TASK_NOVELTY
TASK_AMBIGUITY
END_TO_END_COMPLEXITY
EXPECTED_REWORK_REDUCTION
ALLOWANCE_SENSITIVITY
VALIDATION_DIFFICULTY
```

Preferir **Sol** quando:

- o problema é complexo, mas conhecido e bem delimitado;
- Sol possui histórico de desempenho suficiente nessa classe;
- a prioridade material é preservar quota;
- o ganho esperado do Astra é pequeno ou incerto.

Preferir **Astra Low/Medium** quando:

- a tarefa é especialmente exigente, desconhecida ou aberta;
- maior inteligência-base reduz risco material de erro/retrabalho;
- há workflow end-to-end complexo;
- o problema exige uso avançado de ferramentas/computador;
- Sol exigiria esforço muito alto sem confiança equivalente;
- a diferença de qualidade esperada justifica maior consumo.

```text
IF_ASTRA_SELECTED:
    START_WITH_LOW_OR_MEDIUM_WHEN_SUFFICIENT
```

Não usar Astra High/XHigh/Max automaticamente.

### 1.5 Escalonamento de esforço

Mapeamento conceitual:

```text
LOW / LEVE
→ decisão clara, investigação curta, primeira passagem eficiente

MEDIUM / MÉDIO
→ integração, planejamento e raciocínio moderado

HIGH / ALTO
→ investigação difícil, múltiplas hipóteses, verificação aprofundada

XHIGH / EXTRA_ALTO
→ problema excepcionalmente difícil, com benefício demonstrável de mais iterações

MAX
→ esforço máximo disponível; uso excepcional e explicitamente justificado
```

Os nomes exatos disponíveis devem ser confirmados na superfície atual.

Regras:

```text
START_WITH_LOWEST_SUFFICIENT_EFFORT = YES
HIGHER_EFFORT_REQUIRES_REASON = YES
MAX_EFFORT_IS_EXCEPTION = YES
```

Aumentar esforço quando o problema for **deliberação insuficiente**.

Não aumentar esforço para compensar:

```text
MISSING_FILE
MISSING_PERMISSION
MISSING_PLUGIN
MISSING_CONTEXT
UNDEFINED_REQUIREMENT
AUTHORITY_CONFLICT
```

Esses casos exigem resolver a ausência ou parar no boundary adequado.

### 1.6 Escalonamento de modelo

Escalar modelo quando houver evidência de **capability gap**, como:

- entendimento insuficiente de um problema apesar de instruções adequadas;
- dificuldade persistente em integrar dependências;
- falha recorrente em preservar invariantes;
- ambiguidade material acima do perfil do modelo atual;
- custo de retrabalho superior ao ganho de economia;
- necessidade clara de capacidade end-to-end superior.

```text
CAPABILITY_GAP
→ CONSIDER_STRONGER_MODEL

DELIBERATION_GAP
→ CONSIDER_HIGHER_EFFORT

MISSING_INFORMATION
→ DO_NOT_SOLVE_BY_MODEL_OR_EFFORT_ESCALATION
```

### 1.7 Matriz de categorias revisada

A categoria classifica a **natureza da tarefa**, não o prestígio do modelo.

| Categoria | Modelo inicial recomendado | Esforço inicial | Perfil |
|---|---|---|---|
| A | Luna | Leve | trivial, localizada, mecânica |
| B | Luna | Médio | focada/repetitiva com algum cruzamento |
| C | Terra | Leve ou Médio | trabalho cotidiano e rotineiro |
| D | Terra | Médio ou Alto | julgamento técnico moderado |
| E | Sol | Leve ou Médio | complexa, mas bem delimitada |
| F | Sol | Alto | difícil, profunda, porém controlável |
| G | Astra | Leve ou Médio | especialmente exigente, novel, end-to-end ou muito ambígua |
| G+ | Astra | Alto | problema excepcional com forte necessidade de verificação |
| G++ | Astra | XHigh/Max, se disponível | último recurso para deliberação extrema com benefício explícito |

A matriz é um **default de roteamento**, não uma escada obrigatória.

```text
NO_MANDATORY_MODEL_LADDER = YES
```

Se a tarefa for claramente `G`, pode iniciar em Astra sem executar Luna, Terra
ou Sol antes. Se uma categoria inferior puder resolver com qualidade suficiente,
não escalar.

### 1.8 Gate obrigatório quando Astra for recomendado

Todo prompt que recomendar Astra deve incluir internamente uma justificativa
equivalente a:

```text
ASTRA_SELECTION_GATE = PASS

ASTRA_TRIGGER =
<condição material>

WHY_SOL_IS_NOT_PREFERRED =
<razão concreta>

EXPECTED_ASTRA_GAIN =
<qualidade | robustez | menor retrabalho | capacidade end-to-end | outro>

ASTRA_EFFORT =
LOW | MEDIUM | HIGH | XHIGH | MAX

WHY_THIS_EFFORT =
<razão concreta>
```

Se não for possível justificar:

```text
ASTRA_SELECTION_GATE = FAIL
→ CHOOSE_LOWER_SUFFICIENT_MODEL
```

### 1.9 Telemetria e recalibração

Para workloads recorrentes, evidência local deve superar preferência abstrata.

Quando viável, comparar:

- taxa de sucesso;
- ciclos de correção;
- tempo total;
- consumo de quota/créditos;
- necessidade de escalonamento;
- qualidade de validação;
- falhas de entendimento.

```text
EMPIRICAL_WORKLOAD_EVIDENCE
>
MODEL_PRESTIGE
```

A política deve ser recalibrada quando a OpenAI alterar substancialmente modelos,
disponibilidade, preços, quotas ou comportamento de esforço.

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

Modelo principal recomendado: [Luna | Terra | Sol | Astra]
Esforço recomendado: [Leve/Low | Médio/Medium | Alto/High | Extra Alto/XHigh | Max, conforme disponibilidade]
Categoria: [...]
MODEL_AVAILABILITY = [CONFIRMED | VERIFY_AT_RUNTIME | UNKNOWN]
Motivo da escolha: [...]

SE MODELO = ASTRA:
ASTRA_SELECTION_GATE = [PASS]
ASTRA_TRIGGER = [...]
WHY_SOL_IS_NOT_PREFERRED = [...]
EXPECTED_ASTRA_GAIN = [...]
WHY_THIS_EFFORT = [...]

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

1. Enquadrar objetivo, restrições, risco, novidade, ambiguidade, extensão,
   verificabilidade e authorities.
2. Classificar a tarefa e selecionar o **menor modelo suficiente** entre Luna,
   Terra, Sol e Astra.
3. Selecionar separadamente o **menor esforço suficiente**.
4. Se Astra for escolhido, aplicar `ASTRA_SELECTION_GATE`; sem justificativa
   material, escolher modelo inferior suficiente.
5. Consolidar evidências antes da primeira escrita relevante; verificar
   disponibilidade somente quando necessária.
6. Aplicar o gate multiagente e as regras native/skill/plugin.
7. Implementar no escopo autorizado, validar proporcionalmente e revisar.
8. Escalar modelo apenas por capability gap; escalar esforço apenas por
   deliberation gap.
9. Parar e relatar conflito normativo real, authority ausente, capability crítica
   indisponível, requisito indefinido ou mudança fora do escopo.
10. Para workloads recorrentes, usar telemetria para recalibrar custo/benefício
    entre modelos em vez de assumir superioridade econômica pelo nome.

O relatório final informa arquivos, validações, achados, pendências, riscos,
ausência de expansão de escopo, modelo/esforço, justificativa de Astra quando
aplicável, gate multiagente e decisões de skill/plugin/nativo. Commit, push,
publicação ou ação externa exigem autorização explícita.

```text
MODEL_SELECTION_PRINCIPLES =

LUNA  -> FOCUSED / REPETITIVE / ECONOMICAL
TERRA -> EVERYDAY / BALANCED / MODERATE_JUDGMENT
SOL   -> COMPLEX_BUT_BOUNDED / STRONG_GENERAL_PURPOSE
ASTRA -> ESPECIALLY_DEMANDING / NOVEL / END_TO_END

USE_SMALLEST_SUFFICIENT_MODEL = YES
USE_SMALLEST_SUFFICIENT_EFFORT = YES

ASTRA_AVAILABLE != ASTRA_REQUIRED
ASTRA_SELECTED != HIGH_EFFORT_REQUIRED
HIGHER_EFFORT != GUARANTEED_BETTER_RESULT

MODEL_ESCALATION = CAPABILITY_DECISION
EFFORT_ESCALATION = DELIBERATION_DECISION
MULTIAGENT_ESCALATION = SEPARATE_DECISION

PROPOSED_POLICY_REVIEW = REQUIRED
POLICY_EFFECTIVE = NO
CANONICALIZATION_AUTHORIZED = NO
PROMOTION_AUTHORIZED = NO
```

### 7.1 Referências operacionais externas — não normativas

A atualização de modelo desta versão foi calibrada com documentação oficial
OpenAI disponível em 2026-09-10, especialmente:

- GPT-6 Astra: modelo de maior capacidade para trabalho end-to-end difícil;
- orientação de seleção de modelo no ChatGPT Work/Codex;
- orientação de esforço, incluindo a observação de que Astra Low pode superar
  Sol High em determinadas cargas;
- aviso de que Astra pode consumir a quota de Work/Codex mais rapidamente que
  GPT-5.6 Sol;
- documentação de GPT-5.6 que caracteriza Sol, Terra e Luna por
  capacidade/eficiência.

Essas referências são **evidência de calibração**, não authority permanente.
Mudanças futuras de produto devem passar por nova revisão antes de alterar esta
policy.

---
