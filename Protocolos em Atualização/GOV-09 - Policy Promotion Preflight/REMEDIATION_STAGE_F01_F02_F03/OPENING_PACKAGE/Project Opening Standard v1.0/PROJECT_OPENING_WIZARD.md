# Project Opening Wizard v1.0

STATUS = CANONICAL
WIZARD_TYPE = CONVERSATIONAL_OPERATIONAL_PROTOCOL
PROJECT_OPENING_STANDARD_VERSION = 1.0
NORMATIVE_AUTHORITY = PROJECT_OPENING_STANDARD.md
WIZARD_MUST_CONFORM_TO_STANDARD = YES
STANDARD_WINS = YES
POLICY_SINGLE_SOURCE = PRESERVED
PRODUCTIVE_IMPLEMENTATION_AUTHORIZED = NO

## 1. Propósito e limites

Este Wizard é o protocolo conversacional operacional derivado do Project Opening Standard v1.0. Ele conduz uma ideia expressa em linguagem natural até uma fundação de projeto compreendida, delimitada, governada, arquitetada, tecnicamente fundamentada, documentada, planejada e continuity-ready.

Não é questionário estático, form dump, resumo do Standard, código executável, gerador automático de decisões nem substituto do raciocínio do agente. O Standard é a authority normativa; o Wizard deve conformar-se a ele e nunca o substitui ou altera.

## 2. Uso conversacional

O agente começa pela fala natural do usuário. Extrai o que já foi informado, classifica conservadoramente e identifica somente gaps materiais. Depois pergunta, analisa, recomenda, registra decisões e pendências, avança por gates, materializa a fundação, obtém aprovação explícita e transfere o controle ao Continuity Standard.

HUMAN_AND_INTUITIVE_FIRST → TECHNICAL_STATE_SECOND.

No encerramento de cada phase material, apresentar: compreensão, decisões, itens abertos, recomendação e gate; depois, um snapshot técnico compacto.

## 3. Hierarquia, authority e capability

Não existe uma hierarchy linear universal. A authority é separada por concern:

    NORMATIVE_AUTHORITY_HIERARCHY:
    PROJECT_OPENING_STANDARD.md
    → SPECIALIZED_ACTIVE_POLICIES
    → PROJECT_SPECIFIC_CANONICAL_GOVERNANCE

    USER_DECISION_AUTHORITY:
    USER_APPROVED_DECISION = binding within valid authority boundaries
    USER_APPROVED_DECISION must not silently override MANDATORY_STANDARD_OR_POLICY
    EXCEPTION = EXPLICIT + AUTHORIZED + SCOPED + TRACEABLE

    FACTUAL_SOURCE_HIERARCHY:
    CURRENT_FACTUAL_SOURCE
    → CURRENT_CANONICAL_PROJECT_RECORD
    → LAST_OBSERVED_OR_HISTORICAL_RECORD

Active project documents governam seus próprios concerns. Historical reference nunca substitui authority normativa nem fato atual. STANDARD_WINS = YES apenas em conflitos dentro de seu concern normativo; ele não substitui uma source factual apropriada de Git, runtime, filesystem, API ou equivalente.

Em contradição, registrar fontes, concern, impacto, evidence necessária, owner e condição de encerramento. O Wizard não modifica o Standard para caber no seu fluxo.

AUTHORITY_CONCERNS_SEPARATED = YES
USER_FINAL_AUTHORITY = PRESERVED
SILENT_STANDARD_OVERRIDE_BY_USER_DECISION = NO
FACTUAL_SOURCE_SEMANTICS = PASS

Preservar sempre:

    PREFERENCE != REQUIREMENT
    PROPOSAL != DECISION
    RECOMMENDATION != USER_APPROVAL
    APPROVED != IMPLEMENTED
    IMPLEMENTED != VERIFIED
    VERIFIED != AVAILABLE
    TOOL_AVAILABLE != ACTION_AUTHORIZED
    STATE_WRITE_PREFLIGHT != IMPLEMENTATION_PREFLIGHT
    SELECTION != READINESS
    NO_FALSE_AUTHORITY = REQUIRED
    NO_FALSE_CAPABILITY = REQUIRED

O usuário é a autoridade final de decisão material. O agente analisa e recomenda, decidindo apenas dentro de boundaries aprovados. AUTO delega análise técnica, não authority final irrestrita. TBD é TO_BE_DEFINED, com BLOCKING_NOW = YES|NO; capability desejada sem authority é DEFERRED_NO_AUTHORITY.

As policies de independência analítica, prompts/modelo/esforço, skills e o Agent-Continuity-Standard-v1.0 são referenciados, não reproduzidos. POLICY_SINGLE_SOURCE = PRESERVED.

## 4. Motor adaptativo e classificações

Em cada interação, o agente deve:

1. Extrair e classificar as entradas já recebidas.
2. Registrar a evidência no Opening Ledger.
3. Identificar somente gaps que alterem requisito, scope, arquitetura, risco, authority, gate, documentação, roadmap ou primeiro incremento.
4. Perguntar normalmente três a seis questões de alto valor, ou menos quando menos for suficiente.
5. Analisar alternativas e recomendar a menor solução suficiente.
6. Pedir aprovação somente para decisão reservada.
7. Atualizar Ledger, gate e próxima necessidade de discovery.

DO_NOT_REASK_RESOLVED_INPUT = YES. Reabrir uma entrada apenas por contradição, mudança material, insuficiência superveniente, solicitação do usuário ou reabertura formal.

Classificar origem como FIXED, CONFIGURABLE, DISCOVER_WITH_AGENT, CONDITIONAL ou DERIVED. Classificar conteúdo como FACT, EVIDENCE, REQUIREMENT, CONSTRAINT, PREFERENCE, HYPOTHESIS, PROPOSAL, RECOMMENDATION, DECISION, DEFERRED, UNKNOWN ou NOT_APPLICABLE. Ambiguidade material requer esclarecimento; a não material permanece explicitamente UNKNOWN ou DEFERRED.

## 5. Opening Ledger, state e persistência

OPENING_LEDGER é working foundation state; PROJECT_STATE é o snapshot operacional canônico. Um não substitui o outro.

O Ledger preserva, quando aplicável: PROJECT_IDENTITY, AGENT_IDENTITY, FIXED_BASELINE, REQUIREMENTS, PREFERENCES, CONSTRAINTS, HYPOTHESES, PROPOSALS, RECOMMENDATIONS, DECISIONS, DEFERRED_ITEMS, UNKNOWN_ITEMS, OPEN_ITEMS, CONTRADICTIONS, RISKS, REQUIRED_DOCUMENTS, CONDITIONAL_DOCUMENTS, CURRENT_PHASE, CURRENT_GATE e NEXT_DISCOVERY_NEED.

Cada entrada relevante contém ID, fonte, classificação, afirmação, evidência, impacto, decision owner, status, target canônico e data. Antes do state canônico, OPENING_LEDGER_RECONCILED = YES e gate PASS ou CONDITIONAL aceitável podem fechar uma phase. Em aberturas longas, persistir diretivas de origem, Ledger, decision records, research notes ou recovery snapshot, marcados DRAFT, WORKING, PROPOSED ou FOUNDATION_SOURCE.

EARLY_PERSISTENCE != FINAL_CANONICALIZATION.

## 6. Máquina de estados e contrato de phase

PROJECT_OPENING_ENTRY_GATE → PHASE_0 → PHASE_1 → PHASE_2 → PHASE_3 → PHASE_4 → PHASE_5 → PHASE_6 → PHASE_7_DOCUMENTATION_MATERIALIZATION → PHASE_8_FOUNDATION_REVIEW → USER_FOUNDATION_APPROVAL → PROJECT_OPENING_GATE → CLOSED_PASS.

INTERMEDIATE_USER_REVIEW pode ocorrer como loop auxiliar antes da materialização para validar decisões, drafts ou foundation proposals. INTERMEDIATE_USER_REVIEW != USER_FOUNDATION_APPROVAL e nunca a substitui.

USER_FOUNDATION_APPROVAL = PASS somente pode ocorrer após DOCUMENTATION_MATERIALIZATION e FOUNDATION_REVIEW, e antes da avaliação final de PROJECT_OPENING_GATE.

Estados alternativos: CONDITIONAL, BLOCKED, FAIL e CANCELLED. A próxima phase não começa com a anterior aberta, exceto STATE_WRITE_PREFLIGHT auxiliar para persistir e fechar a atividade corrente.

Em todas as Phases 0–8, declarar objetivo, entry conditions, evidência a obter/analisar, derivações sem pergunta, perguntas potenciais e adaptação, classificações para o Ledger, decisões permitidas e prematuras, open items, blockers, síntese humana, snapshot técnico, exit gate, retorno e próxima phase.

## 7. Phases operacionais
### Project Opening Entry Gate

Antes da Phase 0, avaliar PROJECT_OPENING_ENTRY_GATE = PASS. Ele requer NEW_PROJECT_INTENT = CONFIRMED, PROJECT_OPENING_STANDARD_AVAILABLE = YES, USER_ACCEPTS_GUIDED_OPENING_PROCESS = YES e KNOWN_EXISTING_PROJECT_CONFLICT = NO.

Quando houver sinais de projeto existente, avaliar GREENFIELD, BROWNFIELD ou RETROFIT; não sobrescrever fundação existente. Repositório vazio, isoladamente, não define BROWNFIELD. Blocker no entry gate impede a Phase 0. DO_NOT_ASK_USER_WHAT_CAN_BE_DERIVED = YES: confirmar com o usuário somente o que não puder ser derivado da intenção, fontes e ambiente.


### Phase 0 — Transversal Baseline Load

Objetivo: carregar realmente Standard, Continuity Standard, policies e entrypoints antes do discovery.

Entry conditions: intenção recebida e fontes localizáveis, ou ausência explicitamente verificável.

Obter/analisar: versão e status do Standard, capability inventory proporcional, authority baseline, productive implementation lock, availability de dependências e contamination check. Derivar regras FIXED e inicializar Ledger.

Perguntas: por padrão, nenhuma pergunta de projeto; perguntar apenas por blocker não resolvível nas fontes ou ambiente.

Ledger e limites: registrar baseline, dependências, capability, conflitos e opening mode UNKNOWN quando necessário. Propósito, scope e arquitetura são prematuros.

Saída: TRANSVERSAL_BASELINE_GATE = PASS|CONDITIONAL|BLOCKED|FAIL. Com PASS, READY_FOR_PROJECT_DISCOVERY = YES e segue à Phase 1. Conflito material retorna à authority ou termina em FAIL_CLOSED.

### Phase 1 — Project Discovery

Objetivo: converter a intenção em compreensão suficiente sem decidir stack, banco, arquitetura, roadmap ou sprints.

Entry conditions: baseline carregado e Ledger inicializado.

Obter/analisar: extrair primeiro nome de trabalho, propósito, problema, usuários, valor, sucesso, solução atual, materiais existentes, constraints, preferências, non-goals, domínio e criticidade. Classificar GREENFIELD, BROWNFIELD ou RETROFIT; nunca assumir GREENFIELD. Para BROWNFIELD/RETROFIT, descobrir estado existente, código, arquitetura, dados, integrações, documentação, constraints legados, migration risk e authority existente.

Perguntas: somente itens ainda materiais, como público, problema, sucesso, fronteiras e artefatos atuais.

Ledger e limites: registrar identidade, objetivos, scope inicial, riscos, hipóteses, conflitos e gaps. Síntese e recomendação de discovery são permitidas; decisões de tecnologia, arquitetura, roadmap e sprints são prematuras.

Saída: fecha quando há informação para governance e requirements. Lacuna material bloqueia; premissa alterada mantém ou retorna à discovery. PASS segue à Phase 2.

### Phase 2 — Agent Identity & Governance

Objetivo: definir o que é específico ao projeto, sem repetir baseline FIXED.

Entry conditions: discovery suficiente.

Obter/analisar: nome e papel operacional, responsabilidades, comunicação, modelo de decisão arquitetural, regras de scope-change, planejamento, advancement, commit, push e escalonamento. Derivar o que já for FIXED.

Perguntas: somente boundary material ainda aberto.

Ledger e limites: preservar USER_ROLE = FINAL_AUTHORITY e AGENT_ROLE = INDEPENDENT_TECHNICAL_PARTNER. O agente recomenda regras concretas; não autoconcede authority, aprova scope material ou relaxa segurança.

Saída: exige USER_VALIDATION. Conflito com baseline retorna à Phase 0; mudança de propósito/scope retorna à Phase 1. PASS segue à Phase 3.

### Phase 3 — Requirements & Scope

Objetivo: converter discovery e governance em requirements verificáveis e fronteiras explícitas.

Entry conditions: identidade e governance validadas.

Obter/analisar: classificar requisitos FUNCTIONAL, NON_FUNCTIONAL, QUALITY, SECURITY, SAFETY, DATA, OPERATIONAL, COMPLIANCE e INTERFACE. Para cada requisito material: ID, fonte, classe, prioridade, acceptance criteria, dependências, risco e status.

Perguntas: apenas onde comportamento, qualidade, dados, integração ou risco ainda puder mudar a decisão.

Ledger e limites: delimitar IN_SCOPE, OUT_OF_SCOPE, CONDITIONAL_SCOPE, FUTURE_SCOPE e NON_GOALS. Scope creep é explícito; scope material não é alterado sem authority.

Saída: PASS exige primeira unidade de valor suficientemente especificada e sem conflito material oculto. Premissa nova retorna à Phase 1; PASS segue à Phase 4.

### Phase 4 — Technical & Architecture Discovery

Objetivo: derivar arquitetura de requirements, constraints, risco, qualidade, segurança e operação.

Entry conditions: requirements e scope suficientes para comparar alternativas.

Obter/analisar: mapear proporcionalmente contexts, components, boundaries, dados, interfaces, dependências, execução, falhas, recuperação, observabilidade, implicações de entrega e custos. Seguir:

PROBLEM → REQUIREMENTS → CONSTRAINTS → ALTERNATIVES → EVIDENCE → TRADE_OFFS → RISKS → AGENT_RECOMMENDATION → USER_AUTHORITY_WHEN_REQUIRED → DECISION.

Perguntas: apenas constraints ou prioridades que alterem alternativas.

Ledger e limites: registrar alternativas, evidências, recomendação, decisão, consequência, reversibilidade e authority. Criar ADR somente quando houver valor material. Preferência isolada não define arquitetura.

Saída: ARCHITECTURE_FOUNDATION = PASS somente quando o primeiro incremento puder ser construído sem inventar boundary, contrato ou invariante crítico. Requirement novo retorna à Phase 3; risco novo pode retornar à Phase 5. PASS segue à Phase 5 e libera roadmap na Phase 6.

### Phase 5 — Engineering, Quality, Security & Safety

Objetivo: definir controles proporcionais ao risco.

Entry conditions: arquitetura suficiente e riscos conhecidos.

Obter/analisar: convenções, testes, análise estática, integração, E2E quando aplicável, review, CI, observabilidade, logs, métricas, erro, migração, rollback, manutenção, autenticação, autorização, segredos, dados sensíveis, ações destrutivas, serviços externos, safety e sinais regulatórios.

Perguntas: somente risco, dados, operação ou compliance que não possa ser derivado. NOT_APPLICABLE exige applicability assessment.

Ledger e limites: para cada requisito material, registrar evidência esperada. Ausência de teste necessário é lacuna, não PASS; não declarar teste, segurança ou capability sem evidence.

Saída: ENGINEERING_FOUNDATION = PASS exige controles para riscos materiais e qualidade verificável. Ameaça ou requisito novo retorna à Phase 3 ou 4. PASS segue à Phase 6.

### Phase 6 — Roadmap & Delivery Model

Objetivo: derivar entrega por valor, dependências, risco, boundaries e testabilidade.

Entry conditions: ARCHITECTURE_FOUNDATION = PASS e foundation de engenharia suficiente.

Obter/analisar: escolher proporcionalmente entre SPRINT, MILESTONE, CONTINUOUS_FLOW, EXPERIMENT, RESEARCH_CAMPAIGN, ITERATION ou combinação. Cada incremento responde WHY_THIS_INCREMENT_NOW? e registra valor, dependências, risco, saída, aceite e gate.

Perguntas: somente prioridade, cadência ou dependência que altere a sequência.

Ledger e limites: registrar primeiro incremento e o que não será feito. FIRST_INCREMENT_SELECTED não é readiness; não inventar número de sprints.

Saída: ROADMAP = DEFINED e DELIVERY_MODEL = DEFINED. Mudança arquitetural retorna à Phase 4; risco de execução retorna à Phase 5. PASS segue à Phase 7.

### Phase 7 — Documentation Materialization

Objetivo: persistir somente decisões vigentes em fontes canônicas, com a menor estrutura documental suficiente.

Entry conditions: decisões, gates e documentos requeridos/condicionais identificados no Ledger.

Obter/analisar: materializar, quando aplicável, PROJECT_ORIGIN_DIRECTIVES.md, PROJECT_CHARTER.md, AGENTS.md, AGENT_CONTINUITY.md, PROJECT_STATE.md, OPENING_LEDGER.md, bootstrap, user approval record, Project Opening Gate record e documentos condicionais justificados.

Perguntas: somente se a escrita revelar decisão material ausente. Nesse caso, MATERIALIZATION_PAUSED = YES e retorno à phase competente.

Ledger e limites: cada claim exige REAL_WRITE + CANONICAL_TARGET + VERIFICATION. Não criar documento condicional sem necessidade nem decisão nova durante redação.

Saída: PASS exige documentos MUST aplicáveis, status, version, source-of-truth e referências coerentes, além de state persistido ou handoff real. Sem capability: PROJECT_STATE_UPDATE_PROPOSED = READY, PROJECT_STATE_UPDATE = REQUIRED e STATE_UPDATE_HANDOFF = REQUIRED. PASS segue à Phase 8.

### Phase 8 — Foundation Review & Project Opening Gate

Objetivo: executar review transversal e obter aprovação antes do Opening Gate.

Entry conditions: materialização concluída e evidências disponíveis.

Obter/analisar: revisar identidade, propósito, requirements, scope, governance, arquitetura, engenharia, qualidade, segurança, safety, roadmap, documentação, continuidade, PROJECT_STATE, Ledger, authority, capability, Git quando aplicável e riscos.

Perguntas: somente sobre finding material, contradição, exceção ou decisão reservada pendente.
Antes de fechar FOUNDATION_REVIEW, avaliar INDEPENDENT_FOUNDATION_REVIEW = REQUIRED | RECOMMENDED | NOT_REQUIRED a partir de criticality, financial impact, sensitive data, security surface, operações irreversíveis, production impact, regulatory concerns, architecture complexity, autonomy, external integrations e cost of failure.

Se REQUIRED, PROJECT_OPENING_GATE não recebe PASS antes da review aplicável. Se RECOMMENDED e não executada, registrar rationale e risk treatment conforme governance. Se NOT_REQUIRED, registrar a avaliação proporcional que fundamentou a não aplicabilidade. UNIVERSAL_INDEPENDENT_REVIEW_REQUIREMENT = NO.


Ledger e limites: findings bloqueadores impedem PASS; correção material exige rereview proporcional. Antes do gate, apresentar o que o projeto é, o que será e não será construído, arquitetura, decisões, qualidade, segurança, roadmap, primeiro incremento, riscos e open items não bloqueantes. Solicitar explicitamente USER_FOUNDATION_APPROVAL; silêncio não é aprovação.

Saída: PASS transfere o controle ao Continuity Standard. Finding retorna à phase correspondente.

## 8. Pausa, retomada e fail-closed

Em PAUSE, registrar o ponto material alcançado. Antes do state canônico, manter OPENING_RECOVERY_SNAPSHOT com PROJECT_NAME_OR_WORKING_NAME, OPENING_MODE, CURRENT_PHASE, COMPLETED_PHASES, APPROVED_DECISIONS, OPEN_ITEMS, CONTRADICTIONS, REQUIRED_DOCUMENTS e NEXT_REQUIRED_ACTIVITY.

Em RESUME ou NEW_CHAT_HANDOFF, carregar Ledger e snapshot, verificar fontes factuais e retomar o primeiro ponto material não concluído; nunca reiniciar por conveniência. CANCEL preserva estado cancelado sem declarar fundação PASS. BLOCKED registra razão, owner, evidence necessária e próxima revisão.

Contradição normativa material, ausência de componente MUST ou tentativa de inventar authority/capability exige:

    WIZARD_MATERIALIZATION = FAIL
    NORMATIVE_CONFLICTS_FOUND = <n>
    PROJECT_OPENING_WIZARD = DRAFT_BLOCKED
    READY_FOR_WIZARD_AUDIT = NO
    READY_FOR_TEMPLATES = NO

## 9. Project Opening Gate e continuidade

PROJECT_OPENING_GATE = PASS exige phases aplicáveis, discovery, identidade, governance, requirements/scope, arquitetura, engenharia, roadmap/delivery, documentação, continuidade, state, Ledger, approval explícita e ausência de conflito material, falsa authority ou falsa capability.
Durante toda a abertura, PRODUCTIVE_IMPLEMENTATION_AUTHORIZED = NO. Após PROJECT_OPENING_GATE = PASS, registrar PRODUCTIVE_IMPLEMENTATION_AUTHORIZED_BY_OPENING_STANDARD = RELEASED_FOR_NEXT_GATE.

RELEASED_FOR_NEXT_GATE significa somente que o Opening Standard não bloqueia mais implementação por ausência de fundação. Não significa IMPLEMENTATION_STARTED = YES, READY_FOR_FIRST_IMPLEMENTATION = YES, COMMIT_AUTHORIZED = YES, PUSH_AUTHORIZED = YES, DEPLOYMENT_AUTHORIZED = YES ou PRODUCTION_AUTHORIZED = YES. RELEASED_FOR_NEXT_GATE != IMPLEMENTATION_AUTHORIZATION.


Após PASS, FIRST_INCREMENT_SELECTED = YES quando aplicável. Isso não autoriza implementação. Se existir preflight obrigatório:

    IMPLEMENTATION_READY = NO
    FIRST_IMPLEMENTATION_READY = CONDITIONAL
    CONDITION = IMPLEMENTATION_PREFLIGHT = PASS
    NEXT_REQUIRED_ACTIVITY = <FIRST_INCREMENT> — IMPLEMENTATION PREFLIGHT

READY_FOR_FIRST_IMPLEMENTATION = YES só é possível quando todos os implementation preflights aplicáveis passarem. STATE_WRITE_PREFLIGHT fecha a escrita segura da atividade corrente; não substitui IMPLEMENTATION_PREFLIGHT nem inicia trabalho produtivo. Após o gate, CONTINUITY_PROTOCOL = ACTIVE e a próxima atividade é governada pelo Continuity Standard.

ALL_APPLICABLE_IMPLEMENTATION_PREFLIGHTS = PASS é a condição para READY_FOR_FIRST_IMPLEMENTATION = YES. Enquanto algum preflight aplicável estiver pendente, READY_FOR_FIRST_IMPLEMENTATION = CONDITIONAL.

## 10. Blocos terminais

    OPENING_STATUS = CLOSED_PASS | OPEN | CONDITIONAL | BLOCKED | FAIL | CANCELLED
    PROJECT_STATE_UPDATE = PASS | REQUIRED
    STATE_UPDATE_HANDOFF = NOT_REQUIRED | REQUIRED
    ACTIVITY_COMPLETE = YES | NO
    IMPLEMENTATION_READY = YES | NO | CONDITIONAL

ACTIVITY_COMPLETE = YES exige PROJECT_STATE_UPDATE = PASS. Nenhum estado terminal cria authority para commit, push, deployment, produção ou ação sensível.

## 11. Normative traceability

| Standard | Cobertura no Wizard |
|---|---|
| 1–3 | Propósito, limites, semântica e separação de estados. |
| 4 | Classificação, hierarchy e Opening Ledger. |
| 5 | Baseline FIXED e Phase 0. |
| 6 | Máquina de estados, serialização e gates. |
| 7–15 | Phases 0–8, incluindo rereview. |
| 16 | Documentação MUST e condicional proporcional. |
| 17 | Dependência e transição de continuidade. |
| 18 | State inicial, DoD e persistência. |
| 19 | Claims de escrita e preflights distintos. |
| 20 | Authority factual de Git e brownfield/retrofit. |
| 21 | Authority do usuário e consentimento explícito. |
| 22 | UNKNOWN, DEFERRED, contradição e escalation. |
| 23 | Não antecipação de capability/implementação. |
| 24 | Condições e semântica do Opening Gate. |
| 25 | Fechamento e transição controlada. |
| 26 | Conformance, findings e rereview. |

## 12. Declaração de conformance

Este Wizard é transversal e neutro de domínio. Não altera nem substitui o Project Opening Standard, não cria templates e não autoriza implementação produtiva. A materialização foi concluída; o Wizard está CANONICAL após revisão independente, remediação, rereauditoria e aprovação autorizada.
