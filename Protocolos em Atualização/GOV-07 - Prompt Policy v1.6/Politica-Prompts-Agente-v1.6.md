# Política de Geração de Prompts Multiagente — v1.6

```text
STATUS = PROPOSED
LIFECYCLE = DRAFT
CANONICAL_AUTHORITY_BASELINE = Politica-Prompts-Agente-v1.4.md
CONTENT_BASELINE = Politica-Prompts-Agente-v1.5.md
CONTENT_BASELINE_STATUS = PROPOSED / DRAFT
MULTIAGENT_CHANGE_SOURCE = GOV-02
SKILLS_PLUGINS_CHANGE_SOURCE = GOV-05
CANONICALIZATION = NO
PROMOTION = NO
DOMAIN_SPECIFIC_CONTENT = PROHIBITED
THIRD_NORMATIVE_CHANGE = PROHIBITED
USER_REVIEW_REQUIRED = YES
```

> Esta é uma candidata consolidada e controlada. A v1.4 permanece a autoridade
> canônica do baseline; a v1.5 permanece congelada como baseline de conteúdo
> revisado, proposto e em draft. Esta criação não torna a v1.6 vigente, nem
> autoriza canonicalização, pacote, propagação ou ação externa.

## 0. Finalidade, escopo e versionamento

Esta política define como preparar prompts de atividade para Work ou Codex,
incluindo modelo, esforço, estratégia multiagente, skills, plugins e execução
nativa. É transversal e self-contained. A v1.6 é conceitualmente a v1.5
congelada acrescida apenas da sincronização mínima GOV-05 para Skills/Plugins.

O objetivo é otimizar qualidade, custo, latência, uso de contexto, risco de
regressão e complexidade de coordenação. Disponibilidade de subagente, skill
ou plugin não implica necessidade de uso.

Os nomes Luna, Terra e Sol representam modelos configurados no aplicativo.
Leve, Médio, Alto e Extra Alto representam níveis de deliberação. A
disponibilidade exata deve ser confirmada no seletor atual do ambiente.

## 1. Modelo, esforço e categoria

Modelo é a capacidade-base necessária para a decisão; esforço é a deliberação
necessária para investigar, planejar, revisar e validar. São eixos independentes.

```text
Sol    -> decisões difíceis, sistêmicas ou críticas
Terra  -> julgamento técnico e integração moderada
Luna   -> tarefas delimitadas, repetitivas e observáveis

Leve       -> decisão direta e verificações simples
Médio      -> planejamento e cruzamento de contexto
Alto       -> investigação, comparação e revisão aprofundadas
Extra Alto -> deliberação excepcional para problemas críticos ou incertos
```

Use a menor combinação suficiente. Terra Alto, Sol e Extra Alto exigem
evidência de risco, ambiguidade, impacto ou dificuldade de validação; não
escalar por ansiedade, tamanho aparente ou preferência.

| Categoria | Modelo | Esforço | Perfil |
|---|---|---|---|
| A | Luna | Leve | trivial e localizada |
| B | Luna | Médio | simples com algum cruzamento |
| C | Luna | Alto | clara, extensa e repetitiva |
| C+ | Terra | Leve | clara, tecnicamente exigente |
| D | Terra | Médio | desenvolvimento normal |
| E | Terra | Alto | debug, integração ou julgamento elevado |
| E+ | Terra | Extra Alto | investigação excepcional limitada |
| F | Sol | Alto | arquitetural, sistêmica ou crítica |
| F+ | Sol | Extra Alto | crítica e excepcionalmente ambígua |

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

Modelo principal recomendado: [...]
Esforço recomendado: [...]
Categoria: [...]
Motivo da escolha: [...]

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
skills/plugins são quatro decisões independentes: modelo forte não implica
subagente; complexidade não implica plugin; disponibilidade não implica uso;
review não implica segundo agente.

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

1. Enquadrar objetivo, restrições, risco, modelo, esforço, as quatro decisões
   independentes e as authorities.
2. Consolidar evidências antes da primeira escrita relevante; verificar
   disponibilidade somente quando necessária.
3. Aplicar o gate multiagente e as regras native/skill/plugin.
4. Implementar no escopo autorizado, validar proporcionalmente e revisar.
5. Parar e relatar conflito normativo real, authority ausente, capability
   crítica indisponível ou mudança fora do escopo.

O relatório final informa arquivos, validações, achados, pendências, riscos,
ausência de expansão de escopo, modelo/esforço, gate multiagente e decisões de
skill/plugin/nativo. Commit, push, publicação ou ação externa exigem
autorização explícita.

```text
PROPOSED_POLICY_REVIEW = REQUIRED
POLICY_EFFECTIVE = NO
CANONICALIZATION_AUTHORIZED = NO
PROMOTION_AUTHORIZED = NO
```
