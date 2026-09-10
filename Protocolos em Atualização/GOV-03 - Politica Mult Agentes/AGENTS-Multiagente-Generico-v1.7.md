# Política transversal de execução direta e delegação multiagente — v1.7

## 0. Status e finalidade

```text
STATUS = GENERIC PROJECT-AGNOSTIC POLICY TEMPLATE
SCOPE = ANY GOVERNED PROJECT / AGENT
DIRECT_EXECUTION = DEFAULT
MULTIAGENT_EXECUTION = EXCEPTION
OPTIONAL_SUBAGENT = PROHIBITED
AUTO_ESCALATION = NO
REGISTERED_PROFILE_REQUIRED = YES
UNPROFILED_SUBAGENT = PROHIBITED
PROFILE_AVAILABLE != PROFILE_NECESSARY
USER_FINAL_AUTHORITY = YES
```

Esta política define **quando executar diretamente e quando delegar a subagentes**.
O objetivo é obter a melhor relação entre qualidade, robustez, tempo, consumo de
contexto/tokens e custo de coordenação.

O modo multiagente **não é padrão, ritual, sinal de qualidade nem consequência
automática da complexidade da tarefa**. Ele só deve ser usado quando houver
**ganho material, identificável e verificável** em relação à execução direta.

Regra central:

> **Se não houver benefício material demonstrável de decomposição, paralelismo,
> especialização, independência ou adjudicação, execute diretamente.**

---

## 1. Precedência e autoridade

As authorities, regras de segurança, limites de escopo, gates, convenções e
instruções específicas do projeto, repositório, diretório ou tarefa têm
precedência sobre esta política.

```text
THIS_POLICY != PROJECT_AUTHORITY_REPLACEMENT
CAPABILITY != PERMISSION
DELEGATION != AUTHORITY_TRANSFER
MULTIAGENT != EXECUTION_AUTHORIZATION
```

O uso de subagentes não concede automaticamente autorização para:

- escrever arquivos;
- alterar arquitetura ou contrato;
- avançar fase/sprint/milestone;
- executar experimento;
- operar ambiente produtivo/LIVE;
- alterar dados persistidos;
- executar comandos de alto impacto;
- realizar `git add`, commit, push ou tag;
- modificar governance;
- tomar decisão reservada ao usuário.

Quando existir política canônica de Skills/Plugins, segurança, continuidade ou
outra governança transversal, ela complementa esta política sem ser substituída
por ela.

---

## 2. Invariantes fundamentais

```text
DIRECT_EXECUTION = DEFAULT
MULTIAGENT_EXECUTION = EXCEPTION

OPTIONAL_SUBAGENT = PROHIBITED
AUTO_SPAWN = NO
AUTO_ESCALATION = NO

COMPLEX_TASK != MULTIAGENT_REQUIRED
LARGE_TASK != MULTIAGENT_REQUIRED
HIGH_RISK_TASK != AUTOMATIC_SUBAGENT
STRONG_MODEL != MULTIAGENT_MODE
REVIEW != INDEPENDENT_AGENT_REVIEW
SELF_REVIEW != INDEPENDENT_REVIEW

MODEL_ESCALATION != MULTIAGENT_ESCALATION
SKILL_USE != SUBAGENT_REQUIRED
PLUGIN_USE != SUBAGENT_REQUIRED

DELEGATION_REQUIRES_MATERIAL_BENEFIT
COORDINATION_COST_MUST_BE_JUSTIFIED
IF_BENEFIT_IS_UNCLEAR = DIRECT
```

---

## 3. Direct-first

O agente principal deve tentar resolver a atividade diretamente quando possuir
capacidade suficiente e o problema não exigir separação real de
responsabilidades.

Execução direta é preferida quando:

- existe uma única linha principal de raciocínio;
- o trabalho é sequencial;
- os mesmos arquivos/contextos seriam lidos por todos os agentes;
- há forte acoplamento entre as partes;
- a escrita ocorreria no mesmo conjunto de arquivos;
- a principal dificuldade é raciocínio, e não decomposição;
- a tarefa cabe de forma segura no contexto do agente principal;
- um self-review estruturado é suficiente;
- o ganho de delegação é menor ou incerto diante do custo de coordenação.

```text
IF ALL MULTIAGENT GATES = NO:
    EXECUTION_MODE = DIRECT
    SUBAGENTS_ALLOWED = NO
```

Se houver dúvida entre `DIRECT` e `MULTIAGENT`, a decisão padrão é:

```text
EXECUTION_MODE = DIRECT
```

---

## 4. Gate obrigatório para uso de multiagente

Um subagente só pode ser criado quando existir **benefício material verificável**
ligado a pelo menos uma das condições abaixo.

### G1 — Frentes paralelas realmente independentes

```text
PARALLEL_INDEPENDENT_FRONTS = YES
```

Exige pelo menos duas frentes que:

- possam avançar simultaneamente;
- tenham escopos claros e separáveis;
- não dependam de escrita concorrente sobre o mesmo estado;
- produzam entregáveis que possam ser reconciliados de forma objetiva;
- tragam redução real de tempo ou custo total.

### G2 — Especialização distinta necessária

```text
DISTINCT_SPECIALIZATION_REQUIRED = YES
```

Use somente quando uma capacidade especializada diferente for materialmente
necessária, por exemplo segurança, análise estatística, infraestrutura,
performance, design ou outra disciplina cujo tratamento separado reduza risco
ou melhore substancialmente a decisão.

Especialização apenas conveniente não basta.

### G3 — Ganho material de decomposição

```text
MATERIAL_DECOMPOSITION_GAIN = YES
```

A decomposição deve reduzir de forma real pelo menos um destes fatores:

- wall-clock time;
- consumo total de contexto;
- risco de omissão;
- volume operacional do agente principal;
- custo de execução;
- complexidade de integração.

Dividir uma tarefa apenas para distribuir trabalho não constitui ganho.

### G4 — Conflito identificado que exige adjudicação

```text
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION = YES
```

Deve existir divergência concreta entre evidências, contratos, interpretações ou
resultados. Não criar segundo agente preventivamente para procurar uma
controvérsia que ainda não existe.

### G5 — Governança exige revisão independente

```text
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = YES
```

Use agente independente quando um gate, policy, standard, contrato ou decisão do
usuário realmente exigir independência.

Uma preferência genérica por “segunda opinião” não equivale a requisito de
independência.

---

## 5. Regra de elegibilidade multiagente

Atender a um gate é necessário, mas não suficiente.

Antes de delegar, também deve ser verdadeiro:

```text
AT_LEAST_ONE_MULTIAGENT_GATE = YES
EXPECTED_MATERIAL_GAIN = YES
SCOPE_PARTITION_IS_CLEAR = YES
COORDINATION_COST_IS_ACCEPTABLE = YES
RESULTS_CAN_BE_RECONCILED = YES
AUTHORITY_BOUNDARIES_ARE_PRESERVED = YES
```

Somente então:

```text
EXECUTION_MODE = MULTIAGENT
```

Caso contrário:

```text
EXECUTION_MODE = DIRECT
SUBAGENTS_ALLOWED = NO
```

### 5.1 Regra custo-benefício

Considere explicitamente:

```text
NET_MULTIAGENT_GAIN =
EXPECTED_BENEFIT
-
COORDINATION_OVERHEAD
-
DUPLICATED_CONTEXT_COST
-
INTEGRATION_COST
-
CONSISTENCY_RISK
```

Se o ganho líquido não for claramente positivo:

```text
EXECUTION_MODE = DIRECT
```

---

## 6. Cabeçalho obrigatório de decisão

Em atividades governadas relevantes, declare antes da execução:

```text
EXECUTION_MODE = DIRECT | MULTIAGENT

PARALLEL_INDEPENDENT_FRONTS = YES | NO
DISTINCT_SPECIALIZATION_REQUIRED = YES | NO
MATERIAL_DECOMPOSITION_GAIN = YES | NO
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION = YES | NO
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = YES | NO

EXPECTED_MATERIAL_GAIN = YES | NO
COORDINATION_COST = LOW | MEDIUM | HIGH

SUBAGENTS_ALLOWED = YES | NO
SUBAGENTS_PLANNED = <n>
```

Se `EXECUTION_MODE = DIRECT`:

```text
SUBAGENTS_ALLOWED = NO
SUBAGENTS_PLANNED = 0
```

Não declarar subagente como “opcional”. O agente deve decidir antes da execução
se há justificativa material.

---

## 7. Escalonamento de modelo e esforço

Escolha o modelo e o nível de esforço pelo julgamento efetivamente exigido, e
não pelo papel de orquestrador.

```text
USE_SMALLEST_SUFFICIENT_MODEL = YES
USE_SMALLEST_SUFFICIENT_EFFORT = YES
```

Uma tarefa difícil, mas essencialmente monolítica, deve preferir **um agente
principal mais capaz em modo direto** a vários agentes lendo e reinterpretando o
mesmo contexto.

```text
HARD_SINGLE_THREAD_PROBLEM
→ PREFER_STRONGER_DIRECT_REASONING
→ DO_NOT_AUTO_SPAWN_SUBAGENTS
```

Escalar modelo/esforço é uma decisão distinta de ativar multiagente.

Se a plataforma utilizar tiers ou nomes específicos de modelos, escolha o menor
tier suficiente para a responsabilidade. Nomes de modelos são configuração de
ambiente, não parte essencial deste contrato.

---

## 8. Registro operacional de subagentes

Os perfis concretos disponíveis no ambiente Codex devem ser tratados como
**capacidades operacionais registradas**, e não como participantes obrigatórios
do fluxo.

A política permanece project-agnostic; os nomes abaixo refletem o registro
operacional atualmente configurado em `.codex/agents/`.

| Perfil registrado | Função | Modelo/esforço configurado | Sandbox | Uso permitido |
|---|---|---|---|---|
| `luna_explorer` | exploração de arquivos, símbolos, dependências, fluxos e configurações | `gpt-5.6-luna` / `medium` | `read-only` | somente quando exploração delegada trouxer ganho material |
| `luna_test_analyst` | análise independente de testes, cobertura, regressões e casos extremos | `gpt-5.6-luna` / `high` | `read-only` | somente quando a frente de testes justificar separação |
| `luna_worker` | implementação clara, delimitada e previamente decidida | `gpt-5.6-luna` / `high` | `workspace-write` | somente quando houver ganho real de delegação e escrita estiver autorizada |
| `terra_reviewer` | revisão técnica independente | `gpt-5.6-terra` / `high` | `read-only` | somente quando independência for exigida ou materialmente vantajosa |
| `terra_security` | revisão defensiva de segurança | `gpt-5.6-terra` / `high` | `read-only` | somente quando houver superfície material de segurança |
| `sol_architect` | consulta arquitetural complexa, ambígua ou de alto impacto | `gpt-5.6-sol` / `high` | `read-only` | somente para decisão arquitetural material que justifique consulta separada |

Aplicar:

```text
REGISTERED_PROFILE_REQUIRED = YES
UNPROFILED_SUBAGENT = PROHIBITED
ROLE_EXISTS != ROLE_MUST_BE_USED
PROFILE_AVAILABLE != PROFILE_NECESSARY
PROFILE_RELEVANT != MULTIAGENT_JUSTIFIED
```

A existência de um perfil adequado à natureza da tarefa **não** é justificativa
suficiente para ativar multiagente. Primeiro deve passar o gate de ganho
material desta política.

Não inventar aliases ou perfis inexistentes. Em particular, nomes presentes em
documentação histórica mas ausentes de `.codex/agents/` não devem ser chamados
como se fossem perfis configurados.

O `default_subagent_model` do ambiente é apenas fallback técnico de
configuração. Ele não constitui autorização para criar subagente genérico.

```text
DEFAULT_SUBAGENT_MODEL != SUBAGENT_AUTHORIZATION
```

### 8.1 Limites de leitura e escrita por perfil

Os sandboxes configurados fazem parte da elegibilidade operacional:

```text
READ_ONLY_TASK
→ WRITE_CAPABLE_SUBAGENT_AS_WRITER = PROHIBITED

WRITE_CAPABLE_PROFILE
!= WRITE_AUTHORIZATION
```

`luna_worker` possui `workspace-write`, mas só pode escrever quando a tarefa
principal já possuir autorização de escrita e o contrato delegado delimitar
explicitamente seu ownership.

Os demais perfis registrados são `read-only` e não devem ser utilizados para
contornar ou ampliar limites de escrita.

### 8.2 Concorrência

A configuração atual permite no máximo quatro subagentes simultâneos.

```text
MAX_CONCURRENT_SUBAGENTS = 4
MAX_CONCURRENT_SUBAGENTS != TARGET_SUBAGENTS
MINIMUM_NECESSARY_SUBAGENTS = PREFERRED
```

O limite técnico nunca deve ser interpretado como recomendação de usar quatro
agentes.

---

## 8.3 Gate de seleção do perfil

Mesmo depois de `EXECUTION_MODE = MULTIAGENT`, selecionar um perfil exige uma
segunda decisão:

```text
1. QUAL MATERIAL GAIN JUSTIFICOU MULTIAGENT?
2. QUAL RESPONSABILIDADE PRECISA SER SEPARADA?
3. QUAL PERFIL REGISTRADO É O MENOR SUFICIENTE?
4. O SANDBOX DO PERFIL É COMPATÍVEL COM O ESCOPO?
5. HÁ OVERLAP COM OUTRO AGENTE?
```

Mapeamento operacional:

```text
REPOSITORY_EXPLORATION
→ luna_explorer

TEST_ANALYSIS
→ luna_test_analyst

DEFINED_IMPLEMENTATION
→ luna_worker

INDEPENDENT_TECHNICAL_REVIEW
→ terra_reviewer

MATERIAL_SECURITY_REVIEW
→ terra_security

MATERIAL_ARCHITECTURAL_CONSULTATION
→ sol_architect
```

Esse mapeamento somente escolhe **qual perfil usar depois** de a delegação ter
sido justificada. Ele não ativa multiagente por si próprio.

Exemplos:

```text
TESTS_EXIST = YES
!=
USE_luna_test_analyst

CODE_WRITE_REQUIRED = YES
!=
USE_luna_worker

SECURITY_RELEVANT_PROJECT = YES
!=
USE_terra_security

ARCHITECTURE_EXISTS = YES
!=
USE_sol_architect

IMPLEMENTATION_COMPLETED = YES
!=
USE_terra_reviewer
```

---

## 9. Contrato mínimo de delegação

Todo subagente deve receber um contrato explícito contendo, no mínimo:

```text
DELEGATED_OBJECTIVE
SCOPE_IN
SCOPE_OUT
INPUTS
READ_WRITE_MODE
EXPECTED_OUTPUT
VALIDATION_EXPECTED
STOP_CONDITIONS
AUTHORITY_LIMITS
```

O contrato deve impedir que o subagente:

- expanda escopo por conta própria;
- altere arquitetura fora da tarefa;
- tome decisões reservadas ao agente principal ou usuário;
- execute operações Git não autorizadas;
- escreva fora do ownership definido;
- crie novos subagentes sem autorização explícita.

```text
SUBAGENT_AUTO_DELEGATION = PROHIBITED
```

---

## 10. Responsabilidade do agente principal

O agente principal continua responsável por:

- interpretar a tarefa;
- preservar authorities;
- decidir se delegação é necessária;
- definir contratos dos subagentes;
- controlar dependências;
- reconciliar evidências;
- resolver divergências dentro de sua authority;
- validar o estado final;
- emitir o veredicto final;
- retornar ao usuário quando houver decisão reservada.

```text
DELEGATION != ACCOUNTABILITY_TRANSFER
```

O agente principal não deve apenas concatenar respostas de subagentes.

---

## 11. Implementação: direct by default

Quando a implementação estiver suficientemente definida e puder ser executada
pelo principal sem benefício material de delegação:

```text
IMPLEMENT_DIRECTLY = YES
```

Não crie `luna_worker` apenas para transferir código de um agente para outro.

O `luna_worker` só é adequado quando houver ganho real, como:

- frente independente executável em paralelo;
- volume mecânico significativo que liberará o principal para outra frente
  material;
- especialização operacional específica;
- divisão por ownership de arquivos/módulos claramente isolados.

Mesmo quando arquitetura e contratos estiverem fechados:

```text
DECISIONS_CLOSED != DELEGATION_REQUIRED
```

Se o principal puder executar eficientemente:

```text
EXECUTION_MODE = DIRECT
```

---

## 12. Política de paralelismo

Paralelismo exige independência real.

Não paralelize:

- tarefas sequenciais;
- alterações nos mesmos arquivos;
- componentes fortemente acoplados;
- migrations e consumidores que dependam da mesma transição não estabilizada;
- investigações que exigem o mesmo contexto extenso;
- reviewers que apenas repetirão a mesma leitura sem independência necessária.

Quando houver paralelismo, estabeleça ownership explícito.

```text
CONCURRENT_WRITE_OVERLAP = PROHIBITED
```

O número máximo de subagentes simultâneos, quando configurado pela plataforma,
é **limite**, não objetivo.

```text
MAX_SUBAGENTS != TARGET_SUBAGENTS
MINIMUM_NECESSARY_SUBAGENTS = PREFERRED
```

---

## 13. Economia de contexto

Evite replicar o mesmo conjunto grande de arquivos ou documentos para vários
agentes.

Multiagente perde valor quando:

```text
DUPLICATED_CONTEXT_COST
>=
PARALLELISM_OR_SPECIALIZATION_GAIN
```

Prefira:

- uma única leitura pelo principal quando o contexto é altamente compartilhado;
- partições por responsabilidade quando os dados são realmente separáveis;
- retornos compactos com evidência suficiente para adjudicação.

---

## 14. Contrato de retorno dos subagentes

O retorno deve ser proporcional ao objetivo.

Para investigação/review, prefira estrutura compacta:

```text
finding_id
severity
source / file:line
fact
inference
contract_or_invariant
impact
recommendation
confidence
```

Para implementação:

```text
scope_completed
files_changed
validation_executed
known_limitations
blockers
unresolved_decisions
```

Evite relatórios narrativos extensos quando não agregarem informação material.

---

## 15. Revisão adaptativa

### 15.1 Self-review é o padrão

Na ausência de requisito de independência ou benefício material demonstrado, o
agente principal deve executar diretamente sua própria revisão:

```text
PRIMARY_ANALYSIS
CONSISTENCY_CHECK
ADVERSARIAL_SELF_REVIEW
FINAL_SELF_REVIEW
```

Isso **não** deve ser rotulado como revisão independente.

### 15.2 Reviewer independente não é padrão

Não criar `terra_reviewer` automaticamente porque houve implementação.

Um reviewer independente é elegível quando:

```text
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = YES
```

ou quando existir justificativa concreta de redução material de risco que o
principal sozinho não forneça adequadamente.

```text
IMPLEMENTATION_COMPLETE != REVIEWER_REQUIRED
HIGH_RISK != AUTOMATIC_REVIEWER
```

### 15.3 Escrita após review independente

Quando um gate realmente exigir independência, qualquer escrita posterior no
escopo aprovado invalida a aprovação desse escopo.

Fluxo:

```text
FIX
→ VALIDATE
→ INDEPENDENT_REVIEW_AGAIN
```

apenas quando a independência fizer parte do gate aplicável.

---

## 16. Segurança

Revisão de segurança é ortogonal à revisão técnica geral.

Use `terra_security` somente quando existir superfície
material, como:

- autenticação/autorização;
- secrets;
- trust boundaries;
- filesystem sensível;
- execução de comandos;
- deserialização/parser de entrada não confiável;
- criptografia;
- exposição de rede;
- permissões/ACL;
- mudança de release com impacto relevante de segurança.

Uma tarefa ser “importante” não torna automaticamente necessário um agente de
segurança.

---

## 17. Conflitos e adjudicação

Subagente de adjudicação só deve ser considerado após existir conflito material
real.

```text
NO_CONFLICT = NO_ADJUDICATION_AGENT
```

Quando houver conflito não resolvível pelas authorities existentes ou pelo
agente principal dentro de sua responsabilidade:

```text
STOP_AT_SAFE_BOUNDARY = YES
AUTO_ESCALATION = NO
REPORT_EVIDENCE = YES
RETURN_TO_USER = YES
```

Não criar cadeia automática de reviewers ou arquitetos.

---

## 18. Skills, Plugins e multiagente

As decisões são independentes:

```text
MODEL
EFFORT
EXECUTION_MODE
SKILL
PLUGIN
```

Aplicar:

```text
SKILL_REQUIRED != SUBAGENT_REQUIRED
PLUGIN_REQUIRED != SUBAGENT_REQUIRED
SUBAGENT_REQUIRED != SKILL_REQUIRED
SUBAGENT_REQUIRED != PLUGIN_REQUIRED
```

Uma Skill ou Plugin pode ser usado pelo agente principal em modo direto.

Uma arquitetura multiagente não justifica uso adicional de Skills ou Plugins
sem benefício material próprio.

---

## 19. Read-only e limites de escrita

Se a atividade for read-only:

```text
READ_ONLY = YES
```

isso se aplica a todos os agentes envolvidos.

```text
SUBAGENT_WRITE_PERMISSION = NO
```

A delegação nunca expande permissão de escrita.

Quando escrita for autorizada, ownership deve ser claro e evitar overlap entre
agentes.

---

## 20. Git e operações consequenciais

Nenhum modo de execução autoriza por si só:

```text
GIT_STAGE
COMMIT
PUSH
TAG
RELEASE
DEPLOY
LIVE_EXECUTION
```

Essas operações dependem da autorização específica do projeto/usuário.

```text
MULTIAGENT_PASS != GIT_AUTHORIZATION
DIRECT_PASS != GIT_AUTHORIZATION
```

---

## 21. Early exit

Se um blocker inequívoco determinar que o gate necessariamente falhará:

1. registre evidência suficiente para caracterizar o blocker;
2. conclua apenas validações ainda necessárias para delimitar o estado;
3. evite gasto em findings de baixo valor que não alterariam a decisão;
4. pare em boundary seguro;
5. retorne ao agente principal/usuário conforme authority.

Não use early exit quando investigação adicional for necessária para delimitar
impacto ou preservar segurança.

---

## 22. Fluxo operacional recomendado

```text
1. CLASSIFY_TASK
2. LOAD_APPLICABLE_AUTHORITIES
3. CHOOSE_MINIMUM_SUFFICIENT_MODEL_AND_EFFORT
4. EVALUATE_MULTIAGENT_GATES
5. ESTIMATE_NET_MULTIAGENT_GAIN
6. IF GAIN NOT CLEAR -> DIRECT
7. IF MULTIAGENT -> DEFINE MINIMUM NECESSARY SUBAGENTS
8. DEFINE NON-OVERLAPPING CONTRACTS
9. EXECUTE
10. VALIDATE
11. SELF-REVIEW BY DEFAULT
12. INDEPENDENT REVIEW ONLY IF JUSTIFIED/REQUIRED
13. RECONCILE RESULTS
14. STOP ON UNAUTHORIZED ESCALATION OR MATERIAL CONFLICT
15. FINALIZE ONLY WHEN STATE IS STABLE
```

---

## 23. Decision matrix

| Situação | Modo recomendado |
|---|---|
| Tarefa pequena/local | `DIRECT` |
| Tarefa longa, porém conceitualmente única | `DIRECT` |
| Debug difícil com uma linha principal de investigação | `DIRECT` com maior esforço/modelo se necessário |
| Vários arquivos, mas fortemente acoplados | `DIRECT` |
| Implementação clara que cabe ao principal | `DIRECT` |
| Self-review suficiente | `DIRECT` |
| Duas frentes verdadeiramente independentes e paralelizáveis | `MULTIAGENT` |
| Especialização distinta materialmente necessária | `MULTIAGENT` |
| Gate exige revisão independente | `MULTIAGENT` |
| Conflito real exige adjudicação independente | `MULTIAGENT` |
| Divisão reduz custo/tempo de forma demonstrável | `MULTIAGENT` |
| Benefício da delegação incerto | `DIRECT` |
| Todos os agentes teriam de reler o mesmo contexto extenso | `DIRECT` |

---

## 24. Anti-patterns proibidos

```text
SPAWN_SUBAGENT_BECAUSE_TASK_IS_COMPLEX = PROHIBITED
SPAWN_REVIEWER_BECAUSE_CODE_WAS_WRITTEN = PROHIBITED
SPAWN_WORKER_TO_TRANSFER_TRIVIAL_WORK = PROHIBITED
SPAWN_MULTIPLE_AGENTS_FOR_SAME_ANALYSIS = PROHIBITED
AUTO_ESCALATE_TO_ARCHITECT = PROHIBITED
USE_SUBAGENT_AS_AUTHORITY = PROHIBITED
OPTIONAL_SUBAGENT = PROHIBITED
CONCURRENT_WRITE_OVERLAP = PROHIBITED
MULTIAGENT_AS_STATUS_SYMBOL = PROHIBITED
USE_UNREGISTERED_SUBAGENT_PROFILE = PROHIBITED
USE_luna_worker_WITHOUT_WRITE_AUTHORIZATION = PROHIBITED
USE_terra_reviewer_AS_ROUTINE_SECOND_OPINION = PROHIBITED
USE_sol_architect_FOR_ROUTINE_EXPLORATION = PROHIBITED
```

---

## 25. Exemplos genéricos

### Exemplo A — correção localizada

```text
PARALLEL_INDEPENDENT_FRONTS = NO
DISTINCT_SPECIALIZATION_REQUIRED = NO
MATERIAL_DECOMPOSITION_GAIN = NO
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION = NO
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = NO

EXECUTION_MODE = DIRECT
SUBAGENTS_ALLOWED = NO
```

### Exemplo B — investigação longa, mas altamente compartilhada

Todos precisariam ler o mesmo conjunto de documentos e acompanhar a mesma cadeia
causal.

```text
EXPECTED_PARALLEL_GAIN = LOW
DUPLICATED_CONTEXT_COST = HIGH
EXECUTION_MODE = DIRECT
```

Aumentar esforço/modelo do principal se necessário.

### Exemplo C — duas frentes independentes

Um agente pode analisar persistência e outro segurança, com entregáveis
independentes e sem escrita concorrente.

```text
PARALLEL_INDEPENDENT_FRONTS = YES
DISTINCT_SPECIALIZATION_REQUIRED = YES
EXPECTED_MATERIAL_GAIN = YES
COORDINATION_COST = LOW
EXECUTION_MODE = MULTIAGENT
```

Usar somente os dois agentes necessários.

### Exemplo D — implementação seguida de review

Se nenhuma regra exigir review independente e o risco for controlável pelo
principal:

```text
IMPLEMENTATION = DIRECT
SELF_REVIEW = REQUIRED
INDEPENDENT_REVIEWER = NO
```

Se um gate exigir independência:

```text
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = YES
EXECUTION_MODE = MULTIAGENT
INDEPENDENT_REVIEWER = YES
```

---

## 26. Telemetria opcional para calibração

Quando fizer sentido e sem criar burocracia, registrar:

- modo `DIRECT` ou `MULTIAGENT`;
- motivo da decisão;
- gates multiagente ativados;
- quantidade de subagentes;
- tempo aproximado;
- consumo disponível de tokens/créditos;
- ciclos de retrabalho;
- conflitos de integração;
- se a delegação gerou ganho real.

A telemetria serve para calibrar a política, não para justificar retroativamente
o uso de multiagente.

---

## 27. Regra de reavaliação durante a execução

Uma tarefa iniciada em modo `DIRECT` pode revelar posteriormente uma necessidade
real de multiagente. Isso não autoriza spawn automático.

O agente deve primeiro registrar:

```text
NEW_MULTIAGENT_TRIGGER = <gate material identificado>
EXPECTED_GAIN = <ganho concreto>
SCOPE_OF_DELEGATION = <escopo restrito>
```

Se a governança permitir delegação sem nova aprovação, use apenas o mínimo
necessário. Se não permitir, pare e solicite autorização.

Da mesma forma, uma tarefa iniciada como `MULTIAGENT` deve voltar ao modo mais
simples se a justificativa desaparecer.

```text
MULTIAGENT_JUSTIFICATION_LOST
→ DO_NOT_SPAWN_ADDITIONAL_AGENTS
→ CONSOLIDATE_TO_DIRECT_WHEN_SAFE
```

---

## 28. Checklist final

Antes de criar qualquer subagente, responder:

```text
1. Há uma frente independente real?
2. Há especialização distinta realmente necessária?
3. Há ganho material de decomposição?
4. Há conflito real que exige adjudicação?
5. A governança exige revisão independente?
6. O ganho esperado supera custo de coordenação e contexto duplicado?
7. O escopo pode ser particionado sem overlap perigoso?
8. O retorno pode ser reconciliado objetivamente?
```

Se as respostas não demonstrarem ganho claro:

```text
EXECUTION_MODE = DIRECT
SUBAGENTS_ALLOWED = NO
```

---

## 28.1 Registro operacional atual

```text
REGISTERED_SUBAGENTS =
luna_explorer |
luna_test_analyst |
luna_worker |
terra_reviewer |
terra_security |
sol_architect

UNPROFILED_SUBAGENT = PROHIBITED

MAX_CONCURRENT_SUBAGENTS = 4

DEFAULT_SUBAGENT_MODEL =
CONFIGURATION_FALLBACK_ONLY
```

Se `.codex/agents/` mudar, o registro operacional deve ser reconciliado sem
alterar automaticamente os princípios normativos desta política.

---

## 29. Resumo normativo

```text
DIRECT_EXECUTION = DEFAULT
MULTIAGENT_EXECUTION = EXCEPTION

USE_MULTIAGENT_ONLY_WITH_MATERIAL_VERIFIABLE_GAIN

VALID_MULTIAGENT_TRIGGERS =
PARALLEL_INDEPENDENT_FRONTS |
DISTINCT_SPECIALIZATION_REQUIRED |
MATERIAL_DECOMPOSITION_GAIN |
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION |
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW

AT_LEAST_ONE_TRIGGER_IS_NECESSARY_BUT_NOT_SUFFICIENT
EXPECTED_GAIN_MUST_EXCEED_COORDINATION_COST

IF_BENEFIT_IS_UNCLEAR = DIRECT
OPTIONAL_SUBAGENT = PROHIBITED
AUTO_ESCALATION = NO

SELF_REVIEW = DEFAULT
INDEPENDENT_REVIEW = ONLY_WHEN_REQUIRED_OR_MATERIALLY_JUSTIFIED

MODEL_ESCALATION != MULTIAGENT_ESCALATION
DELEGATION != AUTHORITY_TRANSFER
CAPABILITY != PERMISSION

USER_FINAL_AUTHORITY = YES
```

---

## 30. Encerramento

A arquitetura multiagente deve existir para resolver problemas que **realmente se
beneficiam de múltiplos agentes**. Sempre que um único agente puder executar,
validar e revisar a atividade com qualidade suficiente e menor overhead, o modo
correto é `DIRECT`.

Princípio final:

> **Não use mais agentes para tornar o processo aparentemente mais robusto. Use
> mais agentes somente quando eles tornarem o resultado materialmente melhor,
> mais seguro, mais independente ou mais eficiente. Caso contrário, execute
> diretamente.**
