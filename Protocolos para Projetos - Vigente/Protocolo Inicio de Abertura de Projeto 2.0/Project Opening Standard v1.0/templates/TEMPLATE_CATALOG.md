# Project Opening Templates — Catalog

CATALOG_ID = PROJECT_OPENING_TEMPLATE_CATALOG
CATALOG_VERSION = 1.0
CATALOG_STATUS = CANONICAL
DOCUMENT_STATUS = CANONICAL
CATALOG_TYPE = TEMPLATE_NAVIGATION_AND_APPLICABILITY_GUIDE
NORMATIVE_AUTHORITY = PROJECT_OPENING_STANDARD.md
OPERATIONAL_AUTHORITY = PROJECT_OPENING_WIZARD.md
CATALOG_DOES_NOT_CREATE_AUTHORITY = YES
POLICY_SINGLE_SOURCE = PRESERVED

> Este catálogo orienta seleção e navegação. O template existir não torna seu output obrigatório; aplicabilidade vem do Standard, do Wizard, do contexto factual e das decisões autorizadas.

| Arquivo | Classe | Output canônico | Quando usar | Quando não usar | Phase | Concern | Dependência | Ativação | Incorporação | Gate consumidor |
|---|---|---|---|---|---|---|---|---|---|---|
| PROJECT_ORIGIN_DIRECTIVES.template.md | CORE / REQUIRED | PROJECT_ORIGIN_DIRECTIVES.md | preservar intenção | origem N/A justificada | 0–7 | provenance | — | intenção recebida | não | discovery/materialization |
| PROJECT_CHARTER.template.md | CORE / REQUIRED | PROJECT_CHARTER.md | toda abertura | nunca sem justificativa | 1–7 | foundation | — | discovery | concern pequeno | foundation gate |
| AGENTS.template.md | CORE / REQUIRED | AGENTS.md | todo projeto | cópia de policy | 2–7 | entrypoint | policies | governance | não | continuity |
| AGENT_CONTINUITY.template.md | CORE / REQUIRED | AGENT_CONTINUITY.md | todo projeto | cópia do Standard | 2–7 | continuity | Agent-Continuity-Standard-v1.0 | governance | não | continuity |
| PROJECT_STATE.template.md | CORE / REQUIRED | PROJECT_STATE.md | todo projeto | histórico integral | 0–7 | current state | — | state write | não | project state |
| OPENING_LEDGER.template.md | CORE / REQUIRED | OPENING_LEDGER.md | todo projeto | substituir state | 0–7 | opening process | — | phase 0 | não | opening ledger |
| NEW_CHAT_BOOTSTRAP_PROMPT.template.md | CORE / REQUIRED | NEW_CHAT_BOOTSTRAP_PROMPT.md | continuidade | substituir bootstrap universal | 2–7 | recovery | Agent-Continuity-Standard-v1.0 | continuity | equivalente autorizado | continuity |
| USER_APPROVAL_RECORD.template.md | CORE / REQUIRED | USER_APPROVAL_RECORD.md / EMBEDDED_RECORD | decisão reservada | silêncio | 2–8 | approval | — | approval | sim | user approval |
| PROJECT_OPENING_GATE_RECORD.template.md | CORE / REQUIRED | PROJECT_OPENING_GATE_RECORD.md / EMBEDDED_RECORD | fechamento | sem evidência | 8 | gate | — | review | sim | opening gate |
| REQUIREMENTS.template.md | CONDITIONAL | REQUIREMENTS.md | detalhe material | charter suficiente | 3–7 | requirements | — | assessment | sim | requirements/scope |
| ARCHITECTURE.template.md | CONDITIONAL | ARCHITECTURE.md | decisão arquitetural | sem concern material | 4–7 | architecture | — | assessment | sim | architecture |
| ADR.template.md | CONDITIONAL | adr/<id>-<slug>.md | decisão material | decisão trivial | 4–7 | decision | — | material | não | architecture |
| DECISION_RECORD.template.md | CONDITIONAL | decision record / seção equivalente | decisão rastreável | sem decisão material | 2–7 | decision | — | material | sim | gate aplicável |
| TESTING_STRATEGY.template.md | CONDITIONAL | TESTING_STRATEGY.md | risco/quality material | documento compacto suficiente | 5–7 | verification | — | assessment | sim | engineering |
| ROADMAP.template.md | CONDITIONAL | ROADMAP.md | após architecture foundation | antes de foundation PASS | 6–7 | sequencing | — | architecture pass | sim | roadmap/delivery |
| DELIVERY_PLAN.template.md | CONDITIONAL | DELIVERY_PLAN.md | delivery material | roadmap compacto suficiente | 6–7 | delivery | — | assessment | sim | roadmap/delivery |
| SECURITY_MODEL.template.md | CONDITIONAL | SECURITY_MODEL.md | security surface | N/A justificado | 5–7 | security | — | assessment | sim | engineering |
| SAFETY_CASE.template.md | CONDITIONAL | SAFETY_CASE.md | hazards/irreversibility | N/A justificado | 5–7 | safety | — | assessment | sim | engineering |
| DATA_POLICY.template.md | CONDITIONAL | DATA_POLICY.md | data material | N/A justificado | 5–7 | data | — | assessment | sim | engineering |
| OPERATIONS.template.md | CONDITIONAL | OPERATIONS.md | operação material | N/A justificado | 5–7 | operations | — | assessment | sim | engineering |
| DEPLOYMENT.template.md | CONDITIONAL | DEPLOYMENT.md | deployment material | N/A justificado | 5–7 | deployment | — | assessment | sim | engineering |
| THREAT_MODEL.template.md | CONDITIONAL | THREAT_MODEL.md | threat analysis | N/A justificado | 5–7 | threat | — | assessment | sim | engineering |
| API_CONTRACT.template.md | CONDITIONAL | API_CONTRACT.md | API boundary material | sem contrato | 4–7 | interface | — | assessment | sim | architecture |
| DESIGN_SYSTEM.template.md | CONDITIONAL | DESIGN_SYSTEM.md | UI justificada | sem UI | 4–7 | UI | — | UI assessment | sim | architecture |
| FOUNDATION_REVIEW.template.md | SUPPORTING | FOUNDATION_REVIEW.md / EMBEDDED_REVIEW_RECORD | review separada | embedded suficiente | 8 | review | — | review | sim | opening gate |
| OPENING_RECOVERY_SNAPSHOT.template.md | SUPPORTING / TEMPORARY | OPENING_RECOVERY_SNAPSHOT.md | pause/handoff | state suficiente | 0–7 | recovery | — | pause | não | continuity |

CORE / REQUIRED é materializado salvo NOT_APPLICABLE justificado; CONDITIONAL depende de applicability assessment; SUPPORTING reduz risco de perda de estado ou ambiguidade. ROADMAP só é materializado após ARCHITECTURE_FOUNDATION = PASS. Nenhum item impõe tecnologia, arquitetura, sprints ou decisão de domínio.
