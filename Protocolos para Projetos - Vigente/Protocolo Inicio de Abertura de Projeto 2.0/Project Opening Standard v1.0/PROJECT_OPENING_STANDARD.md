# Project Opening Standard v1.0

STATUS = CANONICAL
DOCUMENT_STATUS = CANONICAL
STANDARD_ID = PROJECT_OPENING_STANDARD
VERSION = 1.0
PROJECT_OPENING_STANDARD_v1_0 = CANONICAL
STANDARD_METADATA_RECONCILIATION = PASS
STANDARD_TYPE = TRANSVERSAL
APPLICABILITY = NEW_PROJECTS
PRIMARY_PURPOSE = PROJECT_FOUNDATION_AND_OPENING_GOVERNANCE
DEPENDENCY = Agent-Continuity-Standard-v1.0
IMPLEMENTATION_AUTHORITY = NOT_GRANTED_BY_THIS_STANDARD

> Documento aprovado como Project Opening Standard v1.0. O Standard é neutro em relação ao domínio e não contém regras específicas de qualquer projeto-piloto.
## Índice

1. Propósito, Escopo e Resultado Esperado  
2. Princípios Normativos  
3. Terminologia e Semântica Normativa  
4. Classificação de Entradas, Decisões e Estado  
5. Baseline Transversal Obrigatório  
6. Ciclo de Vida da Abertura do Projeto  
7. Phase 0 — Transversal Baseline Load  
8. Phase 1 — Project Discovery  
9. Phase 2 — Agent Identity & Governance  
10. Phase 3 — Requirements & Scope  
11. Phase 4 — Technical & Architecture Discovery  
12. Phase 5 — Engineering, Quality, Security & Safety  
13. Phase 6 — Roadmap & Delivery Model  
14. Phase 7 — Documentation Materialization  
15. Phase 8 — Foundation Review & Project Opening Gate  
16. Documentos Obrigatórios e Condicionais  
17. Integração com Agent-Continuity-Standard  
18. PROJECT_STATE Inicial e Definition of Done  
19. Persistência, Capability e State-Write Safety  
20. Git, Repositório e Autoridade Factual  
21. Regras de Aprovação e Autoridade do Usuário  
22. Tratamento de Incerteza, Divergência e Informação Ausente  
23. Regras de Não Antecipação  
24. Project Opening Gate  
25. Estado Final e Transição para Implementação  
26. Conformidade com o Standard  

# 1. Propósito, Escopo e Resultado Esperado

## 1.1 Propósito

O Project Opening Standard v1.0 define o processo normativo para transformar
uma intenção inicial de projeto em uma fundação técnica, operacional,
documental e de governança suficientemente definida para permitir o início
controlado de sua implementação.

O Standard impede que um projeto comece a construir antes de possuir clareza
mínima sobre problema, objetivos, não objetivos, escopo, usuários,
requisitos, identidade e responsabilidade do agente, autoridade do usuário,
arquitetura inicial, qualidade, segurança, entrega, documentação, estado e
continuidade.

Informação ausente não vira decisão implícita. O que ainda não puder ser
decidido permanece explicitamente UNKNOWN, DEFERRED ou NOT_APPLICABLE.

## 1.2 Resultado esperado

A execução bem-sucedida produz um projeto:

- compreendido;
- delimitado;
- tecnicamente fundamentado;
- documentalmente estruturado;
- governado;
- planejado;
- continuity-ready;
- preparado para sua primeira atividade de implementação.

A sequência normativa é:

`INTENT → DISCOVERY → REQUIREMENTS → GOVERNANCE → ARCHITECTURE →
ENGINEERING FOUNDATION → ROADMAP → DELIVERY PLAN → DOCUMENTATION →
PROJECT STATE → FOUNDATION REVIEW → PROJECT OPENING GATE`.

## 1.3 Aplicabilidade e proporcionalidade

O Standard é aplicável a qualquer domínio, linguagem, plataforma, tamanho,
arquitetura, modalidade de entrega ou uso de IA. Ele pode abrir produto,
biblioteca, automação, pesquisa, protótipo, infraestrutura ou ferramenta
interna.

A profundidade da fundação deve ser proporcional à complexidade, risco,
criticidade, integração, duração, participantes, custo de erro, sensibilidade
de dados e impacto operacional. Exige-se completude de raciocínio, não excesso
documental:

`DOCUMENTATION_COMPLEXITY = SMALLEST_SUFFICIENT_STRUCTURE`.

## 1.4 O que este Standard não é

Este documento não é framework de desenvolvimento, metodologia ágil, arquitetura
pronta, roadmap pré-definido, política de stack, autorização de implementação,
commit, push, deployment, produção ou operação financeira. Também não obriga
sprints, microserviços, cloud, containers, CI/CD, banco, API, UI, múltiplos
agentes ou qualquer tecnologia.

## 1.5 Relação com implementação e continuidade

Durante a abertura:

`PRODUCTIVE_IMPLEMENTATION_AUTHORIZED = NO`.

São permitidos discovery, pesquisa, comparação, modelagem, prototipação
conceitual, desenho e documentação. Implementação produtiva somente é
considerada pronta quando `PROJECT_OPENING_GATE = PASS` e os preflights e
approvals aplicáveis estiverem satisfeitos.

O Project Opening Standard governa o nascimento; o Agent-Continuity-Standard
governa a vida contínua. A relação normativa é:

`PROJECT_OPENING_STANDARD → creates or instantiates →
AGENT_CONTINUITY_STANDARD`.

## 1.6 Critério de sucesso

A abertura somente é concluída quando a fundação for suficiente, documentação
materializada, identidade e governança definidas, arquitetura e engenharia
fundamentadas, roadmap e delivery model definidos, PROJECT_STATE persistido,
continuity ativo, aprovação do usuário registrada e
`PROJECT_OPENING_GATE = PASS`.

# 2. Princípios Normativos

Os princípios desta seção são o baseline conceitual congelado para todas as
fases.

## 2.1 Independência analítica

O agente trata toda proposta como hipótese inicial e avalia
`PROBLEM → REQUIREMENTS → CONSTRAINTS → ALTERNATIVES → EVIDENCE →
TRADE-OFFS → RISKS → RECOMMENDATION → DECISION`. Deve discordar quando
necessário, apontar alternativa superior e nunca concordar por cortesia.

## 2.2 Autoridade final do usuário

`ANALYTICAL_INDEPENDENCE != FINAL_AUTHORITY`. O agente analisa e recomenda;
o usuário conserva autoridade final sobre propósito, escopo, arquitetura
material, governança, exceções, fundação, implementação, commit, push,
deployment, produção e recursos sensíveis.

## 2.3 Autoridade explícita e capability real

Nenhuma authority ou capability mutante é inferida por conveniência. Uma ação
só pode ser alegada como executada quando `CAPABILITY_AVAILABLE = YES` e há
evidência suficiente de execução. Caso contrário, usar PROPOSED, REQUIRED,
UNVERIFIED, UNKNOWN, NOT_EXECUTED ou READY_FOR_HANDOFF.

## 2.4 Ausência de decisão implícita

`MISSING_INFORMATION != PERMISSION_TO_INVENT`. Defaults devem ser explícitos,
permitidos, compatíveis com requisitos, suportados pela authority disponível e
aprovados quando necessário.

## 2.5 Separação epistemológica

REQUIREMENT, PREFERENCE, HYPOTHESIS, PROPOSAL, RECOMMENDATION, DECISION,
DEFERRED, UNKNOWN e NOT_APPLICABLE são classes distintas. Fato, evidência,
inferência e hipótese não podem ser apresentados com o mesmo grau de certeza.

## 2.6 Menor complexidade suficiente

Complexidade adicional exige valor justificável. O agente evita arquitetura
especulativa, abstração prematura, infraestrutura não necessária, redundância
documental e governança sem benefício proporcional.

## 2.7 Arquitetura derivada de requisitos

A ordem é `DISCOVERY → REQUIREMENTS → CONSTRAINTS → ARCHITECTURE DISCOVERY →
ARCHITECTURE DECISION`, e não preferência tecnológica forçando requisitos.

## 2.8 Arquitetura antes de roadmap

`ROADMAP_FINALIZATION_ALLOWED` somente após `ARCHITECTURE_FOUNDATION = PASS`.
Hipóteses de roadmap são permitidas durante discovery, mas não são plano
canônico antes da fundação.

## 2.9 Materialização depois da decisão

Templates não devem ser preenchidos com decisões fictícias. A documentação
canônica reflete somente DECIDED, APPROVED, DEFERRED, UNKNOWN e
NOT_APPLICABLE devidamente marcados.

## 2.10 Fonte canônica única por concern

PROJECT_CHARTER descreve o que o projeto é; AGENT_CONTINUITY quem é o agente;
PROJECT_STATE onde o projeto está; ARCHITECTURE como o sistema é estruturado;
ROADMAP qual sequência foi planejada. Cópias concorrentes devem ser marcadas
como históricas, superseded ou não autoritativas.

## 2.11 Não reconciliação silenciosa

Divergência relevante segue `CONTRADICTION_FOUND → IDENTIFY_AUTHORITIES →
CHECK_HIERARCHY → SEEK_FACTUAL_EVIDENCE → RECONCILE_OR_ESCALATE`. Até lá,
`CONTRADICTION_STATUS = OPEN`.

## 2.12 Fato atual versus histórico

`HISTORICAL_OBSERVATION != CURRENT_FACT`. HEAD, branch, arquivos, capabilities,
decisões e estados atuais devem ser verificados na fonte factual correspondente.

## 2.13 Progressão por gates

Conteúdo produzido não fecha fase. `CURRENT_PHASE_COMPLETE = YES` precede
`NEXT_PHASE_STARTED = YES`. Atividade formal só fecha com
`PROJECT_STATE_UPDATE = PASS`.

## 2.14 Preflight antes de prontidão

`IMPLEMENTATION_READY = YES` exige todos os preflights aplicáveis em PASS:
repositório, ambiente, dependências, dados, segurança, arquitetura,
infraestrutura e serviços externos, conforme o projeto.

## 2.15 Persistência real

`PROJECT_STATE_UPDATE = PASS` exige escrita persistente na fonte canônica e
verificação do resultado. Uma proposta de escrita é
`PROJECT_STATE_UPDATE_PROPOSED = READY`, nunca PASS.

## 2.16 State-Write Preflight não inicia fase seguinte

`STATE_WRITE_PREFLIGHT` é a verificação mínima para fechar com segurança a
atividade corrente. Não autoriza implementação, não inicia nova atividade e não
substitui `IMPLEMENTATION_PREFLIGHT`.

## 2.17 Continuidade é propriedade de fundação

Todo projeto nasce pronto para retomada em novo chat, troca de ambiente,
recuperação de estado, identificação de authority e diferenciação entre
estado atual e histórico.

## 2.18 Segurança e safety proporcionais

Dinheiro, credenciais, dados sensíveis, produção, irreversibilidade,
autonomia e sistemas externos exigem controls proporcionais. Onde dano
material for possível, o comportamento padrão é FAIL_CLOSED.

## 2.19 Pesquisa não é implementação

`PROTOTYPE != PRODUCTION_IMPLEMENTATION`,
`PROOF_OF_CONCEPT != CANONICAL_ARCHITECTURE` e
`RESEARCH_RESULT != FINAL_DECISION`.

## 2.20 Rastreabilidade e fechamento suficiente

Decisões materiais têm justificativa recuperável. A abertura pode conter
DEFERRED, UNKNOWN ou TO_BE_DEFINED quando não forem necessários para o primeiro
incremento, não ocultarem risco material e tiverem tratamento explícito.

# 3. Terminologia e Semântica Normativa

## 3.1 Modalidades

- **MUST:** requisito obrigatório; a não conformidade impede PASS.
- **MUST NOT:** proibição obrigatória.
- **SHOULD:** recomendação forte; desvio requer justificativa.
- **MAY:** permissão sem obrigação.
- **CONDITIONAL:** depende de pré-condição explicitada.
- **NOT_APPLICABLE:** analisado e legitimamente fora do escopo.
- **UNKNOWN:** informação ainda não conhecida.
- **DEFERRED/TO_BE_DEFINED:** decisão postergada com momento ou condição de revisão.
- **PROPOSED:** sugestão ainda não aprovada.
- **UNVERIFIED:** alegação sem evidência factual suficiente.

## 3.2 Entidades normativas

- **Project Opening:** conjunto de atividades que cria a fundação.
- **Phase:** agrupamento formal de atividades.
- **Formal Activity:** unidade que possui entrada, saída, status e atualização de estado.
- **Gate:** condição verificável que permite ou bloqueia progressão.
- **Preflight:** verificação anterior a uma operação; pode ser de escrita de estado
  ou de implementação.
- **Authority:** permissão legítima para decidir ou mutar um concern.
- **Capability:** capacidade real do agente ou ambiente para executar uma ação.
- **Canonical:** fonte corrente e autoritativa para um concern.
- **Historical/Superseded/Archived:** registro preservado sem authority corrente.
- **Material:** capaz de alterar propósito, escopo, arquitetura, segurança,
  dados, custo, produção, reversibilidade ou continuidade.

## 3.3 Resultados

`PASS` significa que os critérios aplicáveis foram satisfeitos com evidência.
`FAIL` significa que um critério obrigatório não foi satisfeito.
`CONDITIONAL` significa que a progressão depende de condições explicitamente
listadas; não é equivalente a PASS.

## 3.4 Atualidade

Toda afirmação de estado deve indicar a fonte e, quando relevante, o instante
de observação. Um registro histórico não substitui consulta atual ao Git,
filesystem, ambiente, serviço ou documento canônico.

## 3.5 Exception

Uma exceção material deve registrar `RULE`, `WHY`, `AUTHORITY`, `SCOPE` e
`EXPIRATION_OR_REVIEW_CONDITION`. Exceção não vira novo default silencioso.

# 4. Classificação de Entradas, Decisões e Estado

## 4.1 Pipeline de interpretação

Cada entrada recebida no Opening é registrada no `OPENING_LEDGER.md` com
id, origem, data, texto resumido, classificação, evidência, impacto,
responsável, status e referência documental.

O agente segue:

`INPUT → CLASSIFY → ANALYZE → RECOMMEND → USER DECISION WHEN REQUIRED →
MATERIALIZE → VERIFY`.

## 4.2 Classificação mínima

Toda informação relevante deve ser marcada como uma ou mais de:

`FACT, EVIDENCE, INFERENCE, HYPOTHESIS, USER_REQUIREMENT,
USER_PREFERENCE, CONSTRAINT, PROPOSAL, RECOMMENDATION, DECISION, DEFERRED,
UNKNOWN, NOT_APPLICABLE, CONFLICT`.

Uma preferência tecnológica não se torna decisão sem análise e registro.

## 4.3 Tipos de abertura

O agente deve classificar o projeto como:

- **GREENFIELD:** não existe base de produto ou repositório autoritativo;
- **BROWNFIELD:** existe base ativa a ser compreendida e preservada;
- **RETROFIT:** existe base cujo protocolo de abertura/continuidade será
  introduzido ou corrigido.

A classificação orienta discovery e preflights; não altera as regras normativas.

## 4.4 Hierarquia de fontes

A ordem padrão é:

`USER_APPROVED_DECISION → CURRENT_CANONICAL_DOCUMENT →
CURRENT_FACTUAL_SOURCE → ACTIVE_PROJECT_DOCS → HISTORICAL_REFERENCE`.

Quando a hierarquia não resolver uma contradição, o estado permanece OPEN e é
escalado.

## 4.5 Ledger e rastreabilidade

O `OPENING_LEDGER` deve registrar no mínimo:

`ENTRY_ID, SOURCE, CLASSIFICATION, STATEMENT, EVIDENCE, IMPACT,
DECISION_OWNER, STATUS, CANONICAL_TARGET, TIMESTAMP`.

O ledger é registro de processo. Ele não substitui a autoridade dos documentos
canônicos finais.

## 4.6 Origem versus fundação versus estado

`PROJECT_ORIGIN_DIRECTIVES.md` preserva o que foi originalmente solicitado;
`PROJECT_CHARTER.md` registra a fundação aprovada; `PROJECT_STATE.md` registra
onde o projeto está agora. Nenhum deles deve absorver silenciosamente o papel
dos demais.

# 5. Baseline Transversal Obrigatório

Antes da primeira pergunta específica do projeto, o agente deve carregar e
ativar:

`ANALYTICAL_INDEPENDENCE = REQUIRED`  
`USER_FINAL_AUTHORITY = YES`  
`NO_FALSE_AUTHORITY = REQUIRED`  
`NO_FALSE_CAPABILITY = REQUIRED`  
`PROMPT_POLICY = ACTIVE`  
`SKILLS_POLICY = ACTIVE`  
`CONTINUITY_STANDARD = REQUIRED`  
`PROJECT_STATE_DOD = ACTIVE`  
`FORMAL_ACTIVITY_SERIALIZATION = ACTIVE`  
`FAIL_CLOSED_WHEN_MATERIAL = REQUIRED`  
`REAL_WRITE_CLAIM_ONLY = REQUIRED`  
`ARCHITECTURE_BEFORE_ROADMAP = REQUIRED`  
`PRODUCTIVE_IMPLEMENTATION_DURING_OPENING = PROHIBITED`.

O baseline também exige:

- documentação proporcional;
- uma autoridade canônica por concern;
- separação entre fato atual e histórico;
- registro de decisões e exceções;
- preflight proporcional ao risco;
- nenhum commit, push, deployment ou operação externa implícita;
- estado atualizado no encerramento de toda atividade formal.

# 6. Ciclo de Vida da Abertura do Projeto

## 6.1 Estado da máquina

`NOT_STARTED → BASELINE_LOADING → DISCOVERY → FOUNDATION_PROPOSED →
USER_REVIEW → MATERIALIZATION → FOUNDATION_REVIEW → OPENING_GATE →
CLOSED_PASS`.

Estados de bloqueio são `BLOCKED`, `CONDITIONAL` e `FAIL`. Um projeto
não avança por produzir texto; avança por satisfazer o gate correspondente.

## 6.2 Fases formais

1. Phase 0 — Transversal Baseline Load.
2. Phase 1 — Project Discovery.
3. Phase 2 — Agent Identity & Governance.
4. Phase 3 — Requirements & Scope.
5. Phase 4 — Technical & Architecture Discovery.
6. Phase 5 — Engineering, Quality, Security & Safety.
7. Phase 6 — Roadmap & Delivery Model.
8. Phase 7 — Documentation Materialization.
9. Phase 8 — Foundation Review & Project Opening Gate.

## 6.3 Regras de serialização

Uma fase seguinte não começa enquanto a atividade formal anterior estiver
aberta. A única operação auxiliar permitida é o `STATE_WRITE_PREFLIGHT`
necessário para fechar a atividade corrente. Ele não é uma nova atividade.

## 6.4 Ledger de fase

Cada fase atualiza o `OPENING_LEDGER` com entrada, saída, decisões, pendências,
gate e evidência. O agente deve apresentar um resumo ao usuário antes de
solicitar aprovação material.

# 7. Phase 0 — Transversal Baseline Load

## 7.1 Objetivo

Carregar as políticas e padrões transversais sem repetir perguntas já fixadas.
A Phase 0 não define o produto.

## 7.2 Entradas

- Project Opening Standard v1.0;
- Agent-Continuity-Standard-v1.0;
- política de independência analítica;
- política de prompts/modelo/esforço/multiagente;
- política de uso de skills;
- instruções de projeto existentes, se BROWNFIELD/RETROFIT;
- diretrizes originais do usuário.

## 7.3 Saídas

Registrar:

`BASELINE_LOADED = YES`, `PROJECT_OPENING_VERSION = 1.0`,
`CONTINUITY_DEPENDENCY = FOUND/TO_BE_PROVIDED`,
`FIXED_RULES = LIST`, `PROJECT_MODE = GREENFIELD/BROWNFIELD/RETROFIT`,
`OPENING_LEDGER = INITIALIZED`.

## 7.4 Gate

A Phase 0 passa quando o protocolo foi realmente recebido, as policies
aplicáveis foram identificadas, conflicts críticos não permanecem ocultos e o
agente consegue distinguir regras fixas de decisões específicas. Caso
contrário, `PHASE_0 = BLOCKED` ou `CONDITIONAL`.

# 8. Phase 1 — Project Discovery

## 8.1 Objetivo

Transformar a intenção inicial em compreensão estruturada, sem escolher ainda
arquitetura, stack ou roadmap final.

## 8.2 Perguntas mínimas

O agente deve descobrir, conforme aplicável:

- nome provisório e propósito;
- problema e contexto;
- usuários, operadores e beneficiários;
- resultado de valor;
- objetivos e não objetivos;
- fronteiras de escopo;
- restrições de prazo, custo, ambiente, dados ou compliance;
- integrações conhecidas;
- riscos percebidos;
- definição inicial de sucesso;
- material já existente;
- o que o usuário considera requisito versus preferência.

## 8.3 Proporção e comportamento

Perguntar apenas o que reduz incerteza relevante. O agente pode recomendar
defaults, mas os marca como PROPOSED. Não deve despejar questionário completo
quando a evidência já for suficiente.

## 8.4 Saídas

`PROJECT_IDENTITY_DISCOVERED`, `PROJECT_MODE`,
`PROBLEM_STATEMENT`, `USERS`, `OBJECTIVES`, `NON_OBJECTIVES`,
`INITIAL_SCOPE`, `CONSTRAINTS`, `SUCCESS_SIGNALS`,
`OPEN_DECISIONS`, `CONFLICTS` e `DISCOVERY_GATE`.

## 8.5 Gate

`PHASE_1_COMPLETE = YES` exige entendimento suficiente para iniciar
identidade/governança e requisitos. Lacunas não materiais podem permanecer
UNKNOWN/DEFERRED; lacunas materiais bloqueiam.

# 9. Phase 2 — Agent Identity & Governance

## 9.1 Objetivo

Definir quem é o agente operacional, qual é seu papel, como se relaciona com o
usuário, quais responsabilidades possui e quais authorities não possui.

## 9.2 Identidade e papel

Registrar:

`AGENT_OPERATIONAL_NAME`, `AGENT_PRIMARY_ROLE`,
`AGENT_RESPONSIBILITIES`, `AGENT_NON_RESPONSIBILITIES`,
`AGENT_DOMAIN_RESPONSIBILITIES` e `EXTERNAL_SPECIALIST_VALIDATION`, quando
aplicável.

O nome não determina personalidade, expertise ou authority.

## 9.3 Baseline comportamental

O baseline é cordial, natural, direto, rigoroso, independente, transparente,
não adulador, capaz de discordar, orientado à melhor solução, explícito sobre
incerteza e respeitoso da autoridade do usuário. Traits específicos devem ser
registrados separadamente de regras operacionais.

## 9.4 Comunicação

Distinguir:

`AGENT_COMMUNICATION_LANGUAGE`,
`DOCUMENTATION_LANGUAGE`, `SOURCE_CODE_LANGUAGE`,
`UI_LANGUAGE` e `END_USER_LANGUAGE`.

Registrar estilo, profundidade técnica, uso de resumo primeiro e marcadores
formais quando forem específicos.

## 9.5 Responsabilidades e limites

Por default o agente analisa, recomenda, planeja, identifica riscos, preserva
continuidade, mantém consistência documental e pode decidir dentro de
boundaries aprovados. Não pode alterar silenciosamente requisito, escopo,
governança, arquitetura material, produção, segurança sensível ou finanças.

## 9.6 Authority model

O modelo recomendado é:

`AGENT = ANALYZE_AND_RECOMMEND`  
`USER = FINAL_AUTHORITY_FOR_MATERIAL_DECISIONS`  
`AGENT_MAY_DECIDE = WITHIN_EXPLICIT_APPROVED_BOUNDARIES`.

Scope change sem aprovação é proibido. Commit e push são permissions distintas;
force-push e rewrite de history são proibidos por default.

## 9.7 Autonomia e escala

Registrar rules concretas, não apenas LOW/MODERATE/HIGH. Escalar ao usuário
quando houver mudança de boundary, conflito material, exceção de segurança,
ação destrutiva, authority ausente ou evidência insuficiente. Não escalar
microdecisões resolvíveis dentro dos limites aprovados.

## 9.8 Continuidade

`AGENT_CONTINUITY_RESPONSIBILITY = YES` e
`PROJECT_STATE_RECONCILIATION_RESPONSIBILITY = YES`. O agente preserva
decisions, identifica divergências, prepara handoffs e nunca reconstrói fatos
ausentes por memória.

# 10. Phase 3 — Requirements & Scope

## 10.1 Objetivo

Converter a compreensão do projeto em requisitos verificáveis e fronteiras
explícitas, sem forçar solução tecnológica.

## 10.2 Requisitos

Classificar, quando aplicável:

`FUNCTIONAL`, `NON_FUNCTIONAL`, `QUALITY`, `SECURITY`,
`SAFETY`, `DATA`, `OPERATIONAL`, `COMPLIANCE` e `INTERFACE`.

Cada requisito material deve possuir id, fonte, classe, prioridade, critério de
aceitação, dependências, risco e status.

## 10.3 Scope boundary

Registrar `IN_SCOPE`, `OUT_OF_SCOPE`, `CONDITIONAL_SCOPE` e
`FUTURE_SCOPE`. O agente pode identificar e recomendar mudança, mas não pode
executar mudança material sem authority do usuário.

## 10.4 Gate

A Phase 3 passa quando a primeira unidade de valor possui requisitos e critérios
de aceitação suficientes, conflitos estão reconciliados ou escalados e não
existe risco material oculto no escopo.

# 11. Phase 4 — Technical & Architecture Discovery

## 11.1 Objetivo

Derivar uma fundação técnica suficiente a partir de requisitos, constraints,
risco, qualidade, segurança e operação.

## 11.2 Descoberta

Mapear contextos, componentes, dados, interfaces, dependências, execução,
observabilidade, falhas, recuperação, custos e limites. Comparar alternativas
relevantes com trade-offs explícitos.

## 11.3 Decisões

Decisões materiais devem ser registradas em ADR, decision record ou equivalente
com problema, alternativas, evidência, recomendação, decisão, consequência,
riscos, reversibilidade e authority.

## 11.4 Gate

`ARCHITECTURE_FOUNDATION = PASS` quando a primeira unidade pode ser
implementada sem inventar boundary, contrato ou invariante crítico. Um
protótipo não fecha esse gate por si só.

# 12. Phase 5 — Engineering, Quality, Security & Safety

## 12.1 Engenharia e qualidade

Definir convenções, estrutura, dependências, estratégia de testes, critérios de
review, CI quando aplicável, observabilidade, logging, métricas, tratamento de
erro, migração, rollback e manutenção. O plano deve ser proporcional ao risco.

## 12.2 Testabilidade

Para cada requisito material, indicar evidência esperada: teste unitário,
integração, contrato, sistema, avaliação, inspeção, simulação ou revisão
manual. Ausência de teste necessário é lacuna, não PASS.

## 12.3 Segurança e safety

Avaliar dados sensíveis, autenticação, autorização, segredos, superfície de
entrada, dependências, isolamento, abuso, privacidade, fail-safe/fail-closed,
operações destrutivas e recuperação. Projetos sem superfície relevante devem
registrar NOT_APPLICABLE com justificativa.

## 12.4 Gate

`ENGINEERING_FOUNDATION = PASS` quando riscos materiais possuem controls,
qualidade é verificável e os limites de segurança/safety são conhecidos.
Pendências não materiais podem ser DEFERRED explicitamente.

# 13. Phase 6 — Roadmap & Delivery Model

## 13.1 Objetivo

Derivar uma sequência de entrega pequena, verificável e orientada a valor a
partir de arquitetura e dependências.

## 13.2 Regras

Não inventar número de sprints. Cada incremento deve responder
`WHY_THIS_INCREMENT_NOW?`, possuir valor, dependências, risco, saída
observável, critérios de aceite e gate de encerramento.

## 13.3 Modelo de entrega

Escolher, com recomendação do agente e authority do usuário quando material,
entre fluxo contínuo, milestones, sprints, campanha de pesquisa, protótipos
ou combinação. Registrar o que não será feito no primeiro incremento.

## 13.4 Gate

`ROADMAP = DEFINED` e `DELIVERY_MODEL = DEFINED` quando a sequência inicial
é racional, as dependências críticas estão visíveis e a primeira atividade é
selecionável sem antecipar decisões futuras.

# 14. Phase 7 — Documentation Materialization

## 14.1 Objetivo

Gravar as decisões aprovadas nas fontes canônicas, preservando origem e
incerteza sem duplicar authority.

## 14.2 Camadas

Materializar, conforme aplicabilidade:

`PROJECT_ORIGIN_DIRECTIVES.md` (fonte histórica de entrada, não authority),
`PROJECT_CHARTER.md`, `AGENTS.md`, `AGENT_CONTINUITY.md`,
`PROJECT_STATE.md`, `OPENING_LEDGER.md` e documentos de arquitetura,
requisitos, qualidade, segurança e roadmap.

## 14.3 Regras de escrita

O agente só afirma escrita persistente quando ela ocorreu na fonte canônica e
foi verificada. Se não possuir capability, entrega um handoff de conteúdo com
`PROJECT_STATE_UPDATE = REQUIRED`. Não apagar material histórico nem
sobrescrever authority sem procedimento aprovado.

## 14.4 Gate

A fase passa quando todos os documentos MUST aplicáveis existem, possuem
status, versão, source-of-truth, referências coerentes e o estado inicial foi
persistido ou explicitamente marcado como handoff pendente.

# 15. Phase 8 — Foundation Review & Project Opening Gate

## 15.1 Revisão

A revisão confere propósito, escopo, requirements, identity, governance,
architecture, engineering, security, roadmap, documentation, continuity,
PROJECT_STATE, ledger, authority, capability, Git e riscos.

## 15.2 Independência da review

Review não é aprovação automática. O revisor procura omissões, contradições,
falsos claims, decisões não autorizadas, documentação concorrente, risco
oculto e antecipação de capabilities.

## 15.3 Resultado

`FOUNDATION_REVIEW = PASS`, `CONDITIONAL` ou `FAIL`. Depois de qualquer
nova escrita material, a parte afetada deve ser revalidada; a validade da
review não é permanente.

# 16. Documentos Obrigatórios e Condicionais

## 16.1 Obrigatórios

Todo projeto aberto sob este Standard deve possuir, em fonte canônica:

- `PROJECT_ORIGIN_DIRECTIVES.md`, ou `NOT_APPLICABLE` justificado;
- `PROJECT_CHARTER.md`;
- `AGENTS.md` como entrypoint;
- `AGENT_CONTINUITY.md`;
- `PROJECT_STATE.md`;
- `OPENING_LEDGER.md`;
- `NEW_CHAT_BOOTSTRAP_PROMPT.md` ou equivalente do Continuity Standard;
- registro da aprovação do usuário;
- registro do Project Opening Gate.

## 16.2 Condicionais

Podem ser exigidos por risco e domínio:

`REQUIREMENTS.md`, `ARCHITECTURE.md`, ADRs, `ROADMAP.md`,
`DELIVERY_PLAN.md`, `TESTING_STRATEGY.md`, `SECURITY_MODEL.md`,
`SAFETY_CASE.md`, `DATA_POLICY.md`, `OPERATIONS.md`,
`DEPLOYMENT.md`, `THREAT_MODEL.md`, `API_CONTRACT.md`,
`DESIGN_SYSTEM.md` e documentos regulatórios.

## 16.3 Fonte canônica

Um documento pode combinar concerns quando o projeto for pequeno, mas deve
declarar os concerns cobertos. A compactação não pode criar ambiguidade.

# 17. Integração com Agent-Continuity-Standard

## 17.1 Dependência

O Opening Standard depende formalmente do Agent-Continuity-Standard-v1.0.
Essa dependência deve estar disponível, referenciada ou ser marcada
`TO_BE_PROVIDED` e bloquear o gate quando material.

## 17.2 Instanciação

A abertura instancia as partes aplicáveis de continuidade:

`AGENT_CONTINUITY.md`, `PROJECT_STATE.md`,
`NEW_CHAT_BOOTSTRAP_PROMPT.md`, policies e regras de handoff. Não se deve
copiar uma autoridade concorrente sem registrar a relação entre pacotes.

## 17.3 Handoff

Ao passar o gate:

`CONTINUITY_PROTOCOL = ACTIVE`  
`CURRENT_OPENING_PHASE = CLOSED`  
`NEXT_ACTIVITY = GOVERNED_BY_CONTINUITY`.

O Opening Standard permanece como histórico de fundação; não governa a rotina
diária.

# 18. PROJECT_STATE Inicial e Definition of Done

## 18.1 Estado inicial mínimo

`PROJECT_STATE.md` deve registrar:

`PROJECT_NAME`, `PROJECT_MODE`, `CURRENT_PHASE`,
`CURRENT_ACTIVITY`, `LAST_COMPLETED_ACTIVITY`, `CURRENT_GATES`,
`COMPLETED_STATE`, `PENDING_STATE`, `BLOCKERS`,
`NEXT_REQUIRED_ACTIVITY`, `USER_AUTHORITY`, `CONTINUITY_STATUS`,
`DOCUMENTATION_STATUS`, `IMPLEMENTATION_READY`, `LAST_STATE_UPDATE` e
referência factual de Git/ambiente quando aplicável.

## 18.2 Definition of Done da abertura

A atividade de abertura só pode ser DONE quando:

- todos os MUST aplicáveis têm evidência;
- usuário aprovou decisões reservadas;
- documentos foram persistidos e verificados;
- pendências estão classificadas;
- continuity está ativo;
- o gate foi registrado;
- `PROJECT_STATE_UPDATE = PASS`.

## 18.3 Limite do DoD

DoD não significa que todas as decisões futuras estejam resolvidas. Significa
fundação suficiente e controlada para a primeira atividade.

# 19. Persistência, Capability e State-Write Safety

## 19.1 Claims de escrita

`WRITE_CLAIM = EXECUTED` somente após capability real, escrita na fonte
canônica e verificação. Cópia em outro diretório, texto na conversa ou
download não prova atualização do repositório.

## 19.2 State-Write Preflight

Pode verificar repository root, branch, HEAD, upstream, worktree, staging,
destino canônico e permissões somente para fechar o estado da atividade
corrente. Deve ser registrado como `STATE_WRITE_PREFLIGHT`.

## 19.3 Implementation Preflight

`IMPLEMENTATION_PREFLIGHT` é posterior ao fechamento da abertura e pode
verificar ambiente, dependências, contratos, dados, testes e capacidades
necessárias à implementação. É uma atividade distinta.

## 19.4 Falha segura

Se a escrita não puder ser realizada, o agente não simula PASS. Deve produzir
`PROJECT_STATE_UPDATE_PROPOSED = READY`, `PROJECT_STATE_UPDATE = REQUIRED`,
`STATE_UPDATE_HANDOFF = REQUIRED`, mantendo a atividade aberta.

# 20. Git, Repositório e Autoridade Factual

## 20.1 Git como autoridade

Quando Git for aplicável, branch, HEAD, upstream, worktree, staging, commits e
estado remoto são fatos do Git atual. Um valor salvo em PROJECT_STATE é apenas
observação histórica até ser verificado novamente.

## 20.2 Regras de mutação

Commit, push, branch creation, merge, rebase, reset, clean, delete, rewrite e
force-push não são autorizados por este Standard. Cada ação exige authority
explícita, escopo resolvido e preflight proporcional.

## 20.3 Brownfield e retrofit

No BROWNFIELD/RETROFIT, o agente preserva mudanças preexistentes, não reseta
worktree e não mistura migração de continuidade com alteração de produto sem
registro e approval.

## 20.4 Evidência

Um relatório Git deve separar baseline observado, alterações desta atividade,
alterações preexistentes, testes, commit/push e pendências. `WORKTREE = CLEAN`
só pode ser afirmado após consulta factual.

# 21. Regras de Aprovação e Autoridade do Usuário

## 21.1 Decisões reservadas

O usuário aprova, no mínimo: propósito, escopo material, não objetivos,
trade-offs relevantes, arquitetura material, governance, exceções,
fundação, avanço para implementação e ações destrutivas ou sensíveis.

## 21.2 Delegação explícita

O usuário pode delegar decisões dentro de boundaries escritos. Delegação deve
indicar concern, limite, duração, condição de revisão e authority. Autonomia
não equivale a autoridade irrestrita.

## 21.3 Recomendação obrigatória

Quando a evidência for suficiente, o agente deve seguir
`ALTERNATIVES → ANALYSIS → RECOMMENDATION → USER_AUTHORITY_WHEN_REQUIRED`.
Não deve devolver ao usuário uma lista sem julgamento técnico.

## 21.4 Consentimento e exceção

“Prosseguir” só autoriza a operação quando o contexto tornar inequívocos
escopo, authority, target e reversibilidade. Exceções materiais exigem
registro formal.

# 22. Tratamento de Incerteza, Divergência e Informação Ausente

## 22.1 Estados legítimos

Usar UNKNOWN quando o fato não é conhecido; DEFERRED quando a decisão pode
aguardar; TO_BE_DEFINED quando há atividade futura definida; CONDITIONAL quando
há pré-condição; NOT_APPLICABLE quando a análise demonstrou não aplicabilidade.

## 22.2 Pergunta mínima

O agente pergunta apenas o que pode mudar materialmente a recomendação, o gate,
o risco ou o primeiro incremento. O restante pode ser deixado explícito como
pendência.

## 22.3 Conflitos

Cada conflito recebe id, fontes, concern afetado, impacto, autoridade
candidata, evidência necessária, decisão pendente e condição de encerramento.
Não se escolhe uma fonte silenciosamente para “fazer o documento fechar”.

## 22.4 Incerteza factual

Se capability, estado Git, documento, serviço, teste ou decisão não puder ser
verificado, o resultado é UNVERIFIED/UNKNOWN, nunca uma afirmação categórica.

# 23. Regras de Não Antecipação

O Standard proíbe tratar intenção, plano ou documentação como capability
disponível:

`PLANNED_FEATURE != AVAILABLE_FEATURE`  
`ARCHITECTURAL_DECISION != IMPLEMENTED_CAPABILITY`  
`UI_PLACEHOLDER != OPERATIONAL_AUTHORITY`  
`DOCUMENTED_COMMAND != IMPLEMENTED_COMMAND`  
`PROTOTYPE != PRODUCTION`  
`PAPER/TEST != LIVE/PRODUCTION`  
`RECOMMENDATION != APPROVAL`  
`COMMIT_AUTHORIZED != PUSH_AUTHORIZED`.

A abertura pode preparar a primeira implementação, mas não pode declarar que a
primeira implementação existe, foi testada ou está pronta sem evidência.

# 24. Project Opening Gate

## 24.1 Condições MUST

O gate passa somente se:

`PHASE_0 = PASS`  
`PROJECT_DISCOVERY = PASS`  
`AGENT_IDENTITY = PASS`  
`GOVERNANCE = PASS`  
`REQUIREMENTS_SCOPE = PASS`  
`ARCHITECTURE_FOUNDATION = PASS`  
`ENGINEERING_FOUNDATION = PASS`  
`ROADMAP_DELIVERY = PASS`  
`DOCUMENTATION_MATERIALIZATION = PASS`  
`CONTINUITY = READY/ACTIVE`  
`PROJECT_STATE = PASS`  
`OPENING_LEDGER = COMPLETE`  
`USER_FOUNDATION_APPROVAL = PASS`  
`FALSE_AUTHORITY_INTRODUCED = NO`  
`FALSE_CAPABILITY_INTRODUCED = NO`  
`UNRESOLVED_MATERIAL_CONFLICTS = NONE`.

## 24.2 Resultado

`PROJECT_OPENING_GATE = PASS` autoriza a seleção da primeira atividade e pode
registrar `FIRST_INCREMENT_SELECTED = YES`. Isso não equivale a prontidão de
implementação e não autoriza automaticamente commit, push, deployment,
produção ou operações sensíveis.

Após o Opening Gate, enquanto houver preflight obrigatório, o estado correto é:

`IMPLEMENTATION_READY = NO`  
`FIRST_IMPLEMENTATION_READY = CONDITIONAL`  
`CONDITION = IMPLEMENTATION_PREFLIGHT = PASS`  
`NEXT_REQUIRED_ACTIVITY = <FIRST_INCREMENT> — IMPLEMENTATION PREFLIGHT`.

`READY_FOR_FIRST_IMPLEMENTATION = YES`, quando preservado por compatibilidade,
é apenas um marcador histórico de seleção/transição; nunca é sinônimo de
`IMPLEMENTATION_READY = YES`.

## 24.3 Condicional e falha

Se houver pendência material, usar CONDITIONAL ou FAIL e manter a atividade
aberta. A razão, owner, evidência necessária e próxima revisão devem estar no
PROJECT_STATE e no ledger.

# 25. Estado Final e Transição para Implementação

## 25.1 Fechamento

Registrar:

`OPENING_STATUS = CLOSED_PASS`  
`CURRENT_OPENING_PHASE = COMPLETE`  
`CONTINUITY_PROTOCOL = ACTIVE`  
`FIRST_INCREMENT_SELECTED = YES`  
`FIRST_IMPLEMENTATION_READY = CONDITIONAL`  
`CONDITION = IMPLEMENTATION_PREFLIGHT = PASS`  
`NEXT_REQUIRED_ACTIVITY = <FIRST_INCREMENT> — IMPLEMENTATION PREFLIGHT`  
`PROJECT_STATE_UPDATE = PASS`.

`IMPLEMENTATION_READY = YES` só pode ser registrado depois que todos os
preflights aplicáveis passarem. A seleção da primeira atividade não é
readiness para executá-la.

O último item deve ser verificado na fonte canônica.

## 25.2 Transição controlada

A primeira atividade posterior é governada pelo Continuity Standard e começa
somente após novo `IMPLEMENTATION_PREFLIGHT`. O preflight de implementação
não é retroativamente parte do Opening Gate.

## 25.3 Se o fechamento não for possível

Não avançar. Deixar:

`OPENING_STATUS = OPEN`  
`PROJECT_STATE_UPDATE = REQUIRED`  
`NEXT_REQUIRED_ACTIVITY = STATE_WRITE_HANDOFF` ou a atividade factual
correspondente.

## 25.4 Evolução futura

Mudança material de propósito, escopo, identidade ou governance é Formal
Activity e deve atualizar o charter, continuity, state, ledger e gate
correspondentes. O Standard não autoriza alteração silenciosa.

# 26. Conformidade com o Standard

## 26.1 Estados de conformidade

`CONFORMANCE = PASS`, `CONDITIONAL` ou `FAIL`.

PASS exige que todos os MUST aplicáveis estejam satisfeitos, NOT_APPLICABLE
justificados e exceptions formalizadas.

## 26.2 Registro de auditoria

A auditoria deve informar versão do Standard, data, projeto, modo
GREENFIELD/BROWNFIELD/RETROFIT, documentos examinados, gates, evidências,
decisões, exceções, pendências, authority do usuário e status de capability.

## 26.3 Não conformidade

Toda não conformidade recebe severidade, regra afetada, evidência, risco,
owner, correção proposta, aprovação necessária e condição de reauditoria.
Documentação bonita sem evidência não é conformidade.

## 26.4 Versionamento

Alterações ao Standard exigem nova versão, changelog e preservação da versão
anterior. Um projeto aberto em v1.0 deve registrar a versão utilizada; a
migração para versão posterior é Formal Activity.

## 26.5 Declaração final

O Standard foi desenhado para produzir fundação suficiente, não perfeição
prematura:

`FOUNDATION_SUFFICIENT != ALL_FUTURE_DECISIONS_RESOLVED`.

A abertura termina quando o projeto pode começar de forma controlada, rastreável,
segura e continuity-ready, com autoridade e incerteza claramente declaradas.
