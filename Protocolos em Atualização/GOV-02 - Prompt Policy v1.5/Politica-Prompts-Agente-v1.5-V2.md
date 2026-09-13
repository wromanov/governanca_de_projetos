# Política de Geração de Prompts Multiagente — v1.5

STATUS = PROPOSED_REVISION  
PREVIOUS_VERSION = v1.4  
SCOPE = TRANSVERSAL  
DOMAIN_SPECIFIC_CONTENT = PROHIBITED  
TARGET_ALIGNMENT = AGENTS_MULTIAGENTE_v1.7_R2.1  
BOUNDED_CYCLIC_EXECUTION_INCLUDED = NO  
HISTORICAL_DEPENDENCY_REQUIRED = NO  
READY_FOR_USER_REVIEW = YES  
USER_FINAL_APPROVAL = PENDING  

---

## 0. Finalidade, escopo e regra de autoridade

Esta política define como preparar prompts de atividade para Work ou Codex, incluindo:

- escolha do modelo principal;
- escolha do esforço de raciocínio;
- definição do ROOT / ORCHESTRATOR;
- decisão entre execução direta e multiagente;
- seleção de subagentes;
- roteamento econômico entre tiers de inteligência;
- uso de Skills / Capabilities;
- critérios de validação, escalonamento e revisão;
- limites de authority, escrita, Git e ações externas.

Ela é transversal e self-contained. O prompt gerado deve conseguir ser interpretado sem depender de histórico oculto ou de convenções não materializadas.

Esta política não substitui:

- authorities de projeto;
- contratos de domínio;
- políticas de segurança;
- regras de release;
- regras de Git;
- documentos canônicos específicos do projeto;
- autorização explícita do usuário.

A política de geração de prompts define COMO estruturar e rotear uma atividade.

Ela não amplia O QUE a atividade está autorizada a fazer.

Princípio:

```text
PROMPT_GENERATION_POLICY
!= PROJECT_AUTHORITY
```

e:

```text
CAPABILITY != AUTHORITY
CAPABILITY != PERMISSION
DELEGATION != AUTHORITY_TRANSFER
```

---

## 1. Objetivo de otimização

O objetivo não é:

- minimizar o número de agentes;
- usar sempre o modelo mais barato;
- usar sempre o modelo mais forte;
- usar multiagente sempre que disponível;
- manter o ROOT executando todas as etapas porque ele é capaz.

O objetivo é minimizar:

```text
EXPECTED_COST_PER_SUCCESSFUL_TASK
```

sujeito a:

```text
QUALITY
RELIABILITY
RISK_CONTROL
VERIFIABILITY
AUTHORITY_PRESERVATION
SCOPE_CONTROL
```

Portanto:

```text
MINIMUM_CONFIGURATION
!= MINIMUM_NUMBER_OF_AGENTS
```

e:

```text
LOWEST_CALL_COST
!= LOWEST_TOTAL_EXPECTED_COST
```

A configuração correta é a menor arquitetura de execução que preserve qualidade e autoridade com o melhor custo esperado total.

---

## 2. Modelo, esforço e categoria

Modelo e esforço são eixos independentes.

Modelo representa capacidade-base.

Esforço representa profundidade de deliberação.

### 2.1 Perfis gerais

```text
Luna  -> execução delimitada, repetitiva, observável ou analítica de baixo custo
Terra -> julgamento técnico, integração e implementação não puramente mecânica
Sol   -> arquitetura, hard root cause, hard review ou decisão sistêmica excepcional
```

### 2.2 Esforço

```text
Médio      -> planejamento e integração normais
Alto       -> investigação, revisão, julgamento sustentado
Extra Alto -> deliberação excepcional quando o problema realmente justificar
```

### 2.3 Regra operacional

Use a menor combinação suficiente de modelo e esforço.

Não escalar por:

- ansiedade;
- aparência de tarefa grande;
- hábito;
- preferência pessoal;
- disponibilidade de modelo forte.

Escalar somente quando houver evidência de:

- complexidade cognitiva;
- ambiguidade material;
- risco elevado;
- impacto sistêmico;
- dificuldade de validação;
- necessidade arquitetural;
- hard root cause;
- hard review.

### 2.4 Baseline recomendado

A política de geração de prompts deve tratar como baseline operacional:

```text
ROOT_BASELINE = TERRA / MEDIUM
```

Luna não é o root padrão de tarefas normais de engenharia.

Sol não é o orquestrador persistente padrão.

Terra/High é apropriado quando a atividade possui julgamento técnico elevado.

Sol/High deve ser reservado a necessidades arquiteturais, sistêmicas ou excepcionalmente difíceis.

### 2.5 Luna

Para subagentes Luna:

```text
LUNA_DEFAULT = HIGH
LUNA_ANALYTICAL = EXTRA_HIGH_WHEN_SUPPORTED
```

Luna Leve e Luna Médio não devem ser selecionados como default de novos prompts.

---

## 3. ROOT / ORCHESTRATOR vem antes dos subagentes

Todo prompt deve primeiro decidir:

```text
ORCHESTRATOR_MODEL
ORCHESTRATOR_EFFORT
```

Somente depois deve decidir se existem subagentes materialmente úteis.

A escolha dos subagentes nunca pode ser feita isoladamente da inteligência já presente no ROOT.

Princípio:

```text
ROOT_INTELLIGENCE_IS_PART_OF_ROUTING_DECISION
```

Antes de criar qualquer subagente, pergunte:

```text
DOES_ROOT_ALREADY_COVER_THIS_ROLE_SUFFICIENTLY?
```

Se:

```text
YES
```

então verificar:

```text
INDEPENDENCE_REQUIRED?
DISTINCT_SPECIALIZATION_GAIN?
MATERIAL_ECONOMIC_GAIN?
```

Se todas forem:

```text
NO
```

então:

```text
DO_NOT_SPAWN
```

---

## 4. Análise obrigatória da natureza do trabalho

Antes de decidir DIRECT ou MULTIAGENT, o prompt deve classificar a atividade em pelo menos estas dimensões:

```text
TASK_CLASS
RISK
COGNITIVE_COMPLEXITY
OPERATIONAL_VOLUME
VERIFIABILITY
REVERSIBILITY
```

Além disso, identificar:

```text
COGNITIVE_HOTSPOTS
MECHANICAL_WORK
OBJECTIVE_VALIDATION_WORK
```

### 4.1 Cognitive Hotspot

É uma parte da atividade em que inteligência superior altera materialmente a probabilidade de sucesso.

Exemplos conceituais:

- matemática sensível;
- invariantes críticos;
- debugging difícil;
- integração complexa;
- concorrência;
- semântica de domínio;
- análise arquitetural;
- adjudicação entre evidências conflitantes.

### 4.2 Mechanical Work

É trabalho em que:

- a solução já está fechada;
- os invariantes estão definidos;
- o escopo é bounded;
- os arquivos ou ownership estão claros;
- a execução é prescrita;
- o resultado é objetivamente verificável;
- pouca ou nenhuma decisão técnica nova é necessária.

### 4.3 Objective Validation Work

Inclui:

- testes focais;
- testes de módulo;
- suíte completa;
- lint;
- análise estática;
- build;
- diff check;
- checksum;
- coleta factual;
- reconciliação quantitativa objetiva.

---

## 5. DIRECT vs MULTIAGENT

Execução direta continua válida e desejável quando possui menor custo esperado total.

Mas:

```text
DIRECT_FIRST
```

não deve ser interpretado como:

```text
ROOT_CAN_DO_IT
→ ROOT_SHOULD_DO_ALL_OF_IT
```

A regra correta é:

```text
ROOT_CAN_EXECUTE
!= ROOT_SHOULD_EXECUTE
```

e:

```text
LOWER_TIER_CAN_EXECUTE
!= LOWER_TIER_SHOULD_EXECUTE
```

### 5.1 DIRECT

Escolher DIRECT quando:

- o contexto é pequeno;
- o trabalho restante é pequeno;
- o handoff custa mais que a economia;
- o ROOT já possui o contexto necessário;
- a decomposição não reduz risco, custo ou contexto;
- o volume é insuficiente para amortizar contratação e reconciliação;
- não existe requisito de independência;
- não existe especialização material separável.

Se benefício de delegação for incerto:

```text
IF_BENEFIT_IS_UNCLEAR = DIRECT
```

### 5.2 MULTIAGENT

Escolher MULTIAGENT quando existir pelo menos um ganho material demonstrável e a decomposição for segura.

Multiagente não exige paralelismo.

```text
MULTIAGENT != PARALLELISM
```

Pipeline sequencial é válido:

```text
ROOT
→ IMPLEMENTER
→ VALIDATOR
→ ROOT
```

desde que o ganho econômico e operacional seja material.

---

## 6. Gates de elegibilidade multiagente

O gerador de prompt deve avaliar os seguintes gates.

### G1 — Parallel Independent Fronts

```text
PARALLEL_INDEPENDENT_FRONTS = YES
```

quando existem frentes independentes que podem avançar sem dependência imediata.

### G2 — Distinct Specialization

```text
DISTINCT_SPECIALIZATION_REQUIRED = YES
```

quando uma responsabilidade exige especialização material separável.

### G3 — Material Decomposition Gain

Existe quando a decomposição reduz materialmente:

- wall-clock;
- contexto do ROOT;
- risco de omissão;
- volume operacional no ROOT;
- custo total;
- complexidade de integração;
- carga de validação.

Separar trabalho apenas para distribuí-lo não constitui ganho.

### G4 — Conflict Adjudication

Usar quando existem evidências, análises ou findings independentes que precisam de adjudicação explícita.

### G5 — Governance-Required Independent Review

Usar quando política, gate, contrato ou usuário exige independência formal.

### G6 — Material Intelligence Routing Gain

Este gate é central.

```text
HIGHER_TIER_REQUIRED_FOR_REASONING = YES
AND LOWER_TIER_CAPABLE_OF_BOUNDED_EXECUTION = YES
AND DELEGATED_WORK_IS_OBJECTIVELY_VERIFIABLE = YES
AND HANDOFF_SCOPE_IS_CLEAR = YES
AND EXPECTED_COST_SAVING > COORDINATION_OVERHEAD
→ MULTIAGENT_ALLOWED
```

G6 pode justificar multiagente mesmo quando:

```text
PARALLEL_INDEPENDENT_FRONTS = NO
```

---

## 7. Economic Tiering

Princípio:

```text
EXPENSIVE_INTELLIGENCE_SHOULD_BE_RESERVED_FOR_COGNITIVE_HOTSPOTS
```

e:

```text
BOUNDED_VERIFIABLE_EXECUTION_SHOULD_USE_THE_LOWEST_SUFFICIENT_TIER
```

Exemplo conceitual válido:

```text
TERRA / HIGH ROOT
→ LUNA / HIGH MECHANICAL_IMPLEMENTER
→ LUNA / HIGH VALIDATOR
→ TERRA / HIGH ROOT SELF-REVIEW
```

Isso não é receita obrigatória.

É somente um padrão admissível quando G6 é satisfeito.

### 7.1 Threshold entre tiers adjacentes

Delegação como:

```text
TERRA / HIGH ROOT
→ TERRA / MEDIUM IMPLEMENTER
```

somente é justificada quando:

```text
IMPLEMENTATION_VOLUME
+
LOWER_TIER_SAVING
>
HANDOFF_COST
+
DUPLICATED_CONTEXT_COST
+
INTEGRATION_COST
```

Portanto:

```text
HIGH_ROOT_TO_MEDIUM_IMPLEMENTER
REQUIRES_MATERIAL_NET_GAIN = YES
```

Ser capaz de executar não é suficiente.

---

## 8. Múltiplas rotas válidas

Uma atividade pode admitir mais de uma arquitetura tecnicamente correta.

Por exemplo:

```text
ROUTE_A = HIGH_ROOT_DIRECT_IMPLEMENTATION
ROUTE_B = HIGH_ROOT + MEDIUM_IMPLEMENTER
```

Nesse caso o gerador deve selecionar pela melhor combinação de:

```text
EXPECTED_COST_PER_SUCCESSFUL_TASK
RELIABILITY
AUTHORITY_PRESERVATION
CONTEXT_EFFICIENCY
HANDOFF_COST
VERIFIABILITY
```

Regra:

```text
MULTIPLE_VALID_ROUTINGS_MAY_EXIST = YES
```

A política não exige uma topologia única quando duas rotas são tecnicamente válidas.

Exige justificativa econômica e operacional.

---

## 9. Papéis preferenciais

### 9.1 SCOUT

Modelo:

```text
LUNA / HIGH
```

Uso:

- exploração read-only;
- localizar arquivos;
- mapear superfície;
- encontrar authorities;
- inventariar fatos;
- reduzir contexto do ROOT.

Não usar quando a exploração é tão pequena que o ROOT já precisa ler o mesmo material.

### 9.2 RESEARCHER

Modelo:

```text
LUNA / EXTRA_HIGH
```

quando suportado.

Uso:

- pesquisa analítica delimitada;
- comparação de alternativas;
- análise factual extensa;
- investigação read-only que justifique esforço analítico maior.

Não recebe authority de implementação.

### 9.3 VALIDATOR

Modelo:

```text
LUNA / HIGH
```

Uso:

- testes;
- lint;
- build;
- análise estática;
- diff checks;
- checksums;
- coleta factual;
- reconciliação objetiva.

Regra:

```text
VALIDATOR_VALIDATES
VALIDATOR_DOES_NOT_IMPLEMENT
```

Ferramentas de validação podem precisar criar:

- cache;
- logs;
- build outputs;
- artefatos transitórios.

Portanto:

```text
TECHNICAL_WORKSPACE_WRITE_CAPABILITY = ALLOWED_WHEN_REQUIRED
SOURCE_WRITE_AUTHORIZATION = NO
```

### 9.4 TRIAGE_ANALYST

Modelo:

```text
LUNA / EXTRA_HIGH
```

quando suportado.

Uso:

- diagnosticar falhas ambíguas;
- separar failure signature de root cause;
- classificar regressões;
- levantar hipóteses sem escrever correção.

Regra:

```text
TEST_FAIL != TRIAGE_REQUIRED
```

Uma falha autoexplicativa não exige Triage.

Triage só deve ser criado quando existe ganho diagnóstico material.

### 9.5 MECHANICAL_IMPLEMENTER

Modelo:

```text
LUNA / HIGH
```

Uso somente quando:

```text
SOLUTION_CLOSED = YES
INVARIANTS_CLOSED = YES
SCOPE_BOUNDED = YES
OWNERSHIP_CLEAR = YES
OBJECTIVE_VALIDATION_AVAILABLE = YES
MATERIAL_NET_GAIN = YES
```

Pode:

- aplicar patch prescrito;
- editar arquivos definidos;
- materializar testes já especificados;
- executar trabalho repetitivo de escrita.

Não pode:

- inventar semântica;
- redesenhar arquitetura;
- alterar contrato;
- expandir escopo;
- criar nova regra de negócio;
- resolver ambiguidade por conta própria.

### 9.6 IMPLEMENTER

Modelo padrão:

```text
TERRA / MEDIUM
```

Pode ser elevado a Terra/High quando necessário.

Uso quando a implementação continua exigindo:

- julgamento técnico;
- integração;
- interpretação local;
- escolhas de implementação;
- entendimento de fluxo;
- resolução de detalhes não puramente mecânicos.

Regra:

```text
MECHANICAL_IMPLEMENTER
!= IMPLEMENTER
```

### 9.7 REVIEWER

Modelo típico:

```text
TERRA / HIGH
```

Uso quando:

- revisão independente é obrigatória;
- existe ganho material de review separado;
- a capacidade do ROOT não é suficiente para o review exigido;
- governança explicitamente requer independência.

Não criar Reviewer automaticamente após implementação.

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

### 9.8 SECURITY_REVIEWER

Modelo:

```text
TERRA / HIGH
```

Uso somente quando existe superfície material de segurança ou exigência de governança.

Não utilizar por padrão em toda alteração técnica.

### 9.9 ARCHITECT

Modelo:

```text
SOL / HIGH
```

Uso temporário para:

- arquitetura;
- decisão sistêmica;
- hard root cause;
- hard review;
- problema excepcionalmente difícil.

Architect não deve ser orquestrador persistente por conveniência.

### 9.10 SCRIBE

Modelo:

```text
LUNA / HIGH
```

Uso:

- atualizar documentação;
- materializar estado já decidido;
- reconciliar evidências já aprovadas;
- produzir changelog ou checkpoint.

Não pode inventar:

- PASS;
- aprovação;
- decisão;
- authority;
- estado de projeto.

---

## 10. Redundancy Gate

Antes de criar qualquer subagente, executar:

```text
REDUNDANCY_CHECK
```

Perguntas:

```text
1. O ROOT já cobre esta responsabilidade suficientemente?
2. Existe requisito real de independência?
3. Existe especialização material distinta?
4. Existe ganho econômico líquido?
5. Existe ganho de contexto?
6. Existe ganho de risco?
```

Se a resposta material for não:

```text
DO_NOT_SPAWN
```

Princípio:

```text
DO_NOT_DUPLICATE_EXPENSIVE_INTELLIGENCE_WITHOUT_DISTINCT_VALUE
```

Anti-pattern:

```text
TERRA/HIGH ROOT
+ TERRA/HIGH IMPLEMENTER
+ TERRA/HIGH REVIEWER
```

sem justificativas independentes para cada tier.

---

## 11. Review e independência

Separar sempre:

```text
CAPABILITY_TO_REVIEW
```

de:

```text
INDEPENDENT_REVIEW_REQUIREMENT
```

Um ROOT forte pode possuir capacidade total para revisar e ainda assim não satisfazer independência formal.

Portanto:

```text
STRONG_ROOT != INDEPENDENT_REVIEW
```

Mas:

```text
STRONG_ROOT
+
NO_INDEPENDENCE_REQUIREMENT
=
DO_NOT_DUPLICATE_REVIEW_INTELLIGENCE
```

Reviewer independente somente entra quando independência é realmente requerida ou quando review separado oferece ganho material demonstrável.

---

## 12. Falhas, Triage e retries

Esta política não introduz Bounded Cyclic Execution.

Não definir aqui:

- ciclos autônomos;
- retry ledger;
- Work Units;
- contagem formal de ciclos;
- structured autonomous loop.

Quando uma validação falhar:

```text
FAILURE != AUTOMATIC_TRIAGE
FAILURE != AUTOMATIC_ESCALATION
FAILURE != AUTOMATIC_NEW_AGENT
```

Primeiro avaliar:

```text
FAILURE_IS_SELF_EXPLANATORY?
CONTRACT_IS_CLEAR?
ROOT_CAN_DIAGNOSE_CHEAPLY?
```

Se sim, o ROOT pode tratar diretamente.

Triage é condicional.

Escalonamento é condicional.

---

## 13. Validação

Validação deve ser proporcional ao risco e orientada por gates.

Não executar validações extensas apenas por ritual.

Padrão conceitual:

```text
FOCUSED_VALIDATION
→ MODULE_VALIDATION
→ FULL_VALIDATION_WHEN_APPROPRIATE
```

A seleção deve considerar:

- risco;
- blast radius;
- tipo de alteração;
- authorities;
- custo;
- observabilidade;
- necessidade de evidência.

Após escrita material, validar no nível proporcional à alteração antes de avançar.

Não ignorar falha.

Não transformar falha automaticamente em autorização para corrigir fora do contrato.

---

## 14. Skills / Capabilities — bloco obrigatório

Todo prompt preparado para Work ou Codex deve conter:

```text
🧩 SKILLS / CAPABILITIES

AMBIENTE = [Work | Codex]
🌐 SITE/UI TASK = [YES | NO]
SKILL PRINCIPAL RECOMENDADA = [skill | NONE]
SKILLS AUXILIARES RECOMENDADAS = [skills | NONE]
MOTIVO:
[...]
CATÁLOGO/AVAILABILITY CHECK = [REQUIRED | NOT_REQUIRED]
```

`NONE` é decisão explícita e válida.

Não usar skill por:

- decoração;
- hábito;
- disponibilidade;
- curiosidade;
- ausência de necessidade material.

Nunca inventar, simular ou presumir uma capability.

---

## 15. UI / Sites

Para atividade de implementação ou evolução visual:

```text
SITE/UI TASK = YES
```

e utilizar capability especializada somente se realmente disponível e adequada.

Skills de UI podem auxiliar:

- composição;
- responsividade;
- hierarquia;
- fidelidade;
- acessibilidade;
- consistência visual.

Não transferem authority sobre:

- domínio;
- contrato;
- lifecycle;
- segurança;
- aprovação.

Para atividade não-UI:

```text
SITE/UI TASK = NO
```

---

## 16. Separação de responsabilidades

O gerador deve manter separados:

```text
MODEL / EFFORT = capacidade cognitiva e deliberação

MULTIAGENT = arquitetura de execução e decomposição

SKILLS / CAPABILITIES = especialização ou workflow auxiliar

AUTHORITY = o que pode ser decidido ou executado

PERMISSION = operações concretamente autorizadas
```

Regras:

```text
SKILL != ARCHITECTURAL_AUTHORITY
SKILL != PRODUCT_AUTHORITY
SKILL != USER_AUTHORITY
CAPABILITY != AUTHORITY
CAPABILITY != PERMISSION
MODEL_STRENGTH != AUTHORITY
```

---

## 17. Estrutura obrigatória dos prompts

Todo prompt deve começar com:

```text
RECOMENDAÇÃO DE EXECUÇÃO

TASK_CLASS = [...]
RISK = [...]
COGNITIVE_COMPLEXITY = [...]
OPERATIONAL_VOLUME = [...]
VERIFIABILITY = [...]

ORCHESTRATOR_MODEL = [...]
ORCHESTRATOR_EFFORT = [...]
ORCHESTRATOR_JUSTIFICATION = [...]

COGNITIVE_HOTSPOTS = [...]
MECHANICAL_WORK = [...]
OBJECTIVE_VALIDATION_WORK = [...]

EXECUTION_MODE = [DIRECT | MULTIAGENT]

PARALLEL_INDEPENDENT_FRONTS = [YES | NO]
DISTINCT_SPECIALIZATION_REQUIRED = [YES | NO]
MATERIAL_DECOMPOSITION_GAIN = [YES | NO]
MATERIAL_INTELLIGENCE_ROUTING_GAIN = [YES | NO]
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = [YES | NO]

EXPECTED_MATERIAL_GAIN = [...]
COORDINATION_COST = [...]
DUPLICATED_CONTEXT_COST = [...]

SUBAGENTS_ALLOWED = [YES | NO]
SUBAGENTS_PLANNED = [...]

RESPONSABILIDADE_PELA_IMPLEMENTAÇÃO = [...]
RESPONSABILIDADE_PELA_VALIDAÇÃO = [...]
RESPONSABILIDADE_PELA_REVISÃO_FINAL = [...]

CRITÉRIO_DE_ESCALONAMENTO = [...]

IDIOMA OBRIGATÓRIO:
RESPONDA SEMPRE EM PORTUGUÊS DO BRASIL (pt-BR).
```

Depois incluir o bloco Skills / Capabilities.

---

## 18. Estrutura de subagentes no prompt

Se:

```text
EXECUTION_MODE = MULTIAGENT
```

o prompt deve declarar para cada subagente:

```text
SUBAGENT_<N>_ROLE =
SUBAGENT_<N>_MODEL =
SUBAGENT_<N>_EFFORT =
SUBAGENT_<N>_OBJECTIVE =
SUBAGENT_<N>_OWNERSHIP =
SUBAGENT_<N>_WRITE_MODE =
SUBAGENT_<N>_MUST_NOT =
SUBAGENT_<N>_RETURN_CONTRACT =
SUBAGENT_<N>_WHY_ROOT_SHOULD_NOT_DO_THIS_WORK =
SUBAGENT_<N>_EXPECTED_ECONOMIC_GAIN =
```

Evitar delegações vagas como:

```text
"analise isso"
"veja o que acha"
"ajude na implementação"
```

Cada subagente deve receber responsabilidade estreita, verificável e sem sobreposição material.

---

## 19. Compact Delegation Contract

Subagentes não devem receber automaticamente todo o prompt raiz quando isso causar duplicação desnecessária.

O ROOT deve preferir contratos compactos contendo:

- objetivo;
- authority relevante;
- escopo;
- ownership;
- invariantes;
- arquivos necessários;
- critérios de aceite;
- validação;
- proibições;
- formato de retorno.

Princípio:

```text
THIN_HANDOFF_CONTEXT
WHEN_SUFFICIENT = PREFERRED
```

Isso reduz:

```text
DUPLICATED_CONTEXT_COST
```

---

## 20. Fluxo de geração do prompt

O agente que prepara o prompt deve seguir esta ordem:

1. identificar objetivo;
2. identificar authorities e restrições;
3. classificar risco e complexidade;
4. identificar cognitive hotspots;
5. separar trabalho mecânico;
6. separar validação objetiva;
7. escolher ROOT;
8. avaliar DIRECT;
9. avaliar gates G1–G6;
10. calcular ganho econômico esperado;
11. aplicar Redundancy Gate;
12. escolher subagentes mínimos;
13. selecionar Skills / Capabilities;
14. definir write modes;
15. definir validações;
16. definir critérios de escalonamento;
17. definir Git e ações externas;
18. gerar prompt final.

Nunca selecionar subagentes antes de escolher o ROOT.

---

## 21. Escalonamento e de-escalonamento

Escalar somente quando houver evidência de insuficiência.

Razões válidas incluem:

- ambiguidade material nova;
- failure não explicável pelo contrato;
- hard root cause;
- conflito arquitetural;
- risco maior que o previsto;
- incapacidade demonstrada do tier atual;
- necessidade de independent review;
- descoberta de superfície crítica não prevista.

Quando o hotspot termina:

```text
DEESCALATION_SHOULD_BE_CONSIDERED
```

Exemplo:

```text
TERRA/HIGH
→ fecha decisão
→ LUNA/HIGH executa trabalho mecânico
```

ou:

```text
TERRA/HIGH
→ TERRA/MEDIUM implementa trabalho ainda técnico
```

quando houver ganho líquido material.

---

## 22. Git e ações consequenciais

Prompt não deve autorizar implicitamente:

- git add;
- commit;
- push;
- tag;
- release;
- publicação;
- alteração de recurso externo;
- operação LIVE.

Essas ações exigem autorização explícita.

Modelo forte não implica permissão.

Subagente não herda permission apenas por delegação.

---

## 23. Anti-patterns normativos

### 23.1 Root forte fazendo tudo

```text
TERRA/HIGH
→ análise
→ escrita mecânica
→ testes
→ logs
→ review
```

quando partes inferiores poderiam ser roteadas economicamente.

### 23.2 Multiagente por ornamentação

Criar subagentes apenas porque estão disponíveis.

### 23.3 Reviewer ritualístico

```text
IMPLEMENTATION_COMPLETE
→ ALWAYS REVIEWER
```

Proibido.

### 23.4 Triage ritualístico

```text
TEST_FAIL
→ ALWAYS TRIAGE
```

Proibido.

### 23.5 Luna para implementação que exige julgamento material

Mechanical Implementer não substitui Implementer.

### 23.6 Terra para trabalho puramente mecânico volumoso

Quando G6 está satisfeito, considerar Luna.

### 23.7 Sol persistente sem necessidade arquitetural

Sol não deve ser usado como orquestrador padrão.

### 23.8 Duplicação de tiers caros

Dois agentes do mesmo tier alto precisam de valor distinto demonstrável.

### 23.9 Full-context handoff sem necessidade

Duplicar todo o contexto para subagentes pode eliminar a economia de tiering.

### 23.10 Escalonamento por ansiedade

Falha ou dificuldade não justificam automaticamente modelo superior.

---

## 24. Padrões de conformidade de roteamento

Os exemplos abaixo são padrões conceituais, não receitas fixas.

### Padrão A — alteração trivial

```text
COGNITIVE_COMPLEXITY = LOW
OPERATIONAL_VOLUME = VERY_LOW
VERIFIABILITY = HIGH

EXPECTED:
DIRECT
```

Mesmo que Luna consiga executar, o handoff pode custar mais que o trabalho.

### Padrão B — hotspot forte + implementação mecânica

```text
HIGH_JUDGMENT_ROOT
→ MECHANICAL_IMPLEMENTER
→ VALIDATOR
→ ROOT_SELF_REVIEW
```

Esperado quando G6 é satisfeito.

### Padrão C — hotspot forte + implementação ainda técnica

```text
HIGH_JUDGMENT_ROOT
→ TERRA_IMPLEMENTER
→ VALIDATOR
→ ROOT_SELF_REVIEW
```

Somente se o ganho líquido superar duplicated context + handoff.

### Padrão D — independência obrigatória

```text
ROOT
→ INDEPENDENT_REVIEWER
→ ROOT_ADJUDICATION
```

Mesmo quando ROOT e Reviewer usam tier semelhante.

O valor distinto é independência.

### Padrão E — failure autoexplicativo

```text
VALIDATION_FAIL
→ ROOT_DIRECT_DIAGNOSIS
```

sem Triage automático.

---

## 25. Bloco Skills / Capabilities e roteamento são independentes

A seleção de Skills não deve decidir:

- modelo;
- esforço;
- direct vs multiagent;
- authority;
- permission.

Da mesma forma, um modelo forte não elimina a necessidade de uma capability especializada quando ela produz ganho material.

Avaliar separadamente:

```text
COGNITIVE_ROUTING
EXECUTION_ROUTING
CAPABILITY_ROUTING
AUTHORITY
```

---

## 26. Relatório final obrigatório

O prompt deve exigir um relatório final com, no mínimo:

```text
FINAL_REPORT

EXECUTION_MODE =
ORCHESTRATOR_MODEL =
ORCHESTRATOR_EFFORT =

SUBAGENTS_USED =
SKILLS_USED =

FILES_CHANGED =
VALIDATIONS_EXECUTED =
VALIDATION_RESULTS =

FINDINGS =
CORRECTIONS =
PENDING_ITEMS =
RISKS =

SCOPE_EXPANSION = YES | NO
UNAUTHORIZED_CHANGES = YES | NO

INDEPENDENT_REVIEW_USED = YES | NO
ROOT_SELF_REVIEW_COMPLETED = YES | NO

GIT_ACTIONS_PERFORMED =
EXTERNAL_ACTIONS_PERFORMED =

FINAL_VERDICT =
```

---

## 27. Princípios finais

1. Modelo é capacidade-base; esforço é deliberação.
2. Escolha o ROOT antes dos subagentes.
3. Capacidade não implica economicidade.
4. ROOT_CAN_EXECUTE não implica ROOT_SHOULD_EXECUTE.
5. LOWER_TIER_CAN_EXECUTE não implica LOWER_TIER_SHOULD_EXECUTE.
6. Multiagente não exige paralelismo.
7. Sequential multiagent pipeline é válido.
8. Use inteligência cara somente onde ela produz ganho cognitivo material.
9. Use tiers inferiores para trabalho bounded e verificável quando o ganho líquido for material.
10. Mechanical Implementer não substitui implementação que exige julgamento.
11. Reviewer existe por independência ou ganho material, não por ritual.
12. TEST_FAIL não implica TRIAGE.
13. Validator valida; não implementa.
14. Delegação não transfere authority.
15. Skill não transfere authority.
16. Escrita técnica permitida por sandbox não implica source write authorization.
17. Múltiplas rotas podem ser válidas; escolha pela melhor relação entre confiabilidade e custo esperado.
18. Minimize EXPECTED_COST_PER_SUCCESSFUL_TASK, não apenas número de agentes.
19. Não introduzir Bounded Cyclic Execution nesta política.
20. Escalonar por evidência e de-escalonar quando a inteligência superior deixa de ser necessária.
21. Commit, push, publicação e operações externas exigem autorização explícita.
22. Todo prompt Work/Codex deve declarar idioma pt-BR e bloco Skills / Capabilities.
23. `NONE` é uma decisão válida.
24. Nunca inventar capability.
25. Quando não houver ganho material claro de delegação, permanecer DIRECT.

---

## 28. Estado desta revisão

```text
VERSION = 1.5
STATUS = PROPOSED_REVISION
PREVIOUS_VERSION = 1.4

ECONOMIC_INTELLIGENCE_ROUTING = INCLUDED
MATERIAL_INTELLIGENCE_ROUTING_GAIN_G6 = INCLUDED
SEQUENTIAL_MULTIAGENT_PIPELINE = INCLUDED
ROOT_REDUNDANCY_GATE = INCLUDED
MECHANICAL_IMPLEMENTER = INCLUDED
CONDITIONAL_TRIAGE = INCLUDED
INDEPENDENT_REVIEW_SEMANTICS = INCLUDED
BOUNDED_CYCLIC_EXECUTION = EXCLUDED

READY_FOR_USER_REVIEW = YES
CANONICAL_PROMOTION = PENDING_USER_APPROVAL
```
