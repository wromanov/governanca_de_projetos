# F-03 — Matriz de Rastreabilidade

```text
STATUS = PROPOSED / DRAFT
FINDING = F-03
FINDING_CLASSIFICATION = REAL SYNCHRONIZATION GAP
BASELINE = Politica-Prompts-Agente-v1.4.md
TARGET = Politica-Prompts-Agente-v1.5.md
VALIDATION_SCOPE = NORMATIVE STATIC REVIEW
CANONICALIZATION = NO
PROPAGATION = NO
```

## 1. Finding e decisão aprovada

```text
PROBLEM_OBSERVED = A governança multiagente consolidada no Control Room é mais precisa e restritiva que a redação textual empacotada na v1.4.
EVIDENCE = A v1.4 declara execução direta como padrão e exige benefício verificável, mas não codifica explicitamente OPTIONAL_SUBAGENT=PROHIBITED, AUTO_ESCALATION=NO, o conjunto de cinco condições materiais ou REVIEW_PASS != INDEPENDENT_AGENT_REVIEW.
CAUSE = Ambiguidade de enforcement e ausência de um decision gate textual padronizado.
POLICY_CURRENT = Politica-Prompts-Agente-v1.4.md, especialmente seções 2, 5, 6, 8 e 11.
GAP = Interpretações permissivas podem transformar tamanho, criticidade, cobertura ou revisão genérica em justificativa para outro agente.
RECOMMENDATION = Criar v1.5 proposta, com hardening limitado ao concern multiagente.
USER_DECISION = GOV_01 ACCEPTED; GOV_02 drafting authorized, canonicalization/propagation not authorized.
```

## 2. Matriz

| ID | Requisito aprovado | Baseline v1.4 | Implementação na v1.5 proposta | Evidência de verificação | Resultado |
|---|---|---|---|---|---|
| F03-01 | `DIRECT_EXECUTION = DEFAULT` | Direto era padrão em certos casos | Seção 2 declara direto como padrão geral | Busca textual + cenário 1 | PASS |
| F03-02 | `OPTIONAL_SUBAGENT = PROHIBITED` | Existiam permissões condicionais amplas | Seção 2 proíbe uso opcional/preventivo | Busca textual + cenários 1–4 | PASS |
| F03-03 | Benefício material verificável | Benefício real era requerido, sem registro uniforme | Seções 2 e 2.3 exigem benefício e evidência | Gate padronizado | PASS |
| F03-04 | Frentes paralelas independentes | Frentes independentes eram critério qualitativo | `PARALLEL_INDEPENDENT_FRONTS` | Cenário 5 | PASS |
| F03-05 | Especialização distinta necessária | Especialização clara podia bastar | `DISTINCT_SPECIALIZATION_REQUIRED` | Seção 2 + revisão adversarial | PASS |
| F03-06 | Ganho material de decomposição | Decomposição não tinha campo explícito | `MATERIAL_DECOMPOSITION_GAIN` | Gate | PASS |
| F03-07 | Conflito real exige adjudicação | Conflito não tinha regra operacional dedicada | `IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION` | Cenário 6 | PASS |
| F03-08 | Gate de governança exige independência | Revisão podia ser lida como justificativa geral | `GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW` | Cenário 8 | PASS |
| F03-09 | Importante não implica subagente | Não havia negação textual específica | `TASK_IMPORTANT ... does not imply` | Cenário 3 | PASS |
| F03-10 | Grande não implica subagente | Não havia negação textual específica | `TASK_LARGE ... does not imply` | Cenário 2 | PASS |
| F03-11 | Crítica não implica subagente | Não havia negação textual específica | `TASK_CRITICAL ... does not imply` | Cenário 3 | PASS |
| F03-12 | Review pass distinto de review independente | Distinção não estava textual | `REVIEW_PASS != INDEPENDENT_AGENT_REVIEW` | Cenário 4 | PASS |
| F03-13 | Self-review permitido | Revisão era possível, sem taxonomia | `SELF_REVIEW`, `CONSISTENCY_CHECK`, `ADVERSARIAL_PASS`, `FINAL_SELF_REVIEW` | Cenário 4 | PASS |
| F03-14 | Escalonamento automático proibido | Escalonamento por evidência era genérico | `AUTO_ESCALATION = NO` | Cenário 7 | PASS |
| F03-15 | Necessidade durante execução retorna ao usuário | Não havia sequência completa | `STOP → REPORT → RECOMMEND → USER DECISION` | Cenário 7 | PASS |
| F03-16 | Sem policy separada nesta atividade | Concern permanecia na Prompt Policy | `SEPARATE_MULTIAGENT_DELEGATION_POLICY = NO` | Diff seção 2.4 | PASS |
| F03-17 | Neutralidade de nomes | Baseline transversal já era neutro | v1.5 não introduz nome próprio de agente/projeto | Inspeção lexical | PASS |

## 3. Rastreabilidade de preservação

| Área protegida | Regra de preservação | Resultado |
|---|---|---|
| Seleção de modelo | Não alterar escala nem tabela | PRESERVED |
| Seleção de esforço | Não alterar níveis nem limiares | PRESERVED |
| Skills/capabilities | Manter bloco obrigatório e `NONE` | PRESERVED |
| UI/Sites | Manter regra complementar | PRESERVED |
| Authority | Usuário e documentos canônicos permanecem authority | PRESERVED |
| Idioma | Manter pt-BR obrigatório | PRESERVED |
| Git/ações externas | Autorização explícita permanece necessária | PRESERVED |
| v1.4 | Não editar ou substituir | PRESERVED |
| Pacotes/manifests/hashes | Não atualizar | PRESERVED |

## 4. Limites da verificação

```text
RUNTIME_EXECUTION = NOT_PERFORMED
PROJECT_PROPAGATION_TEST = NOT_APPLICABLE_BY_SCOPE
CANONICAL_AUTHORITY_UPDATE = NOT_PERFORMED
STATIC_TRACEABILITY_REVIEW = COMPLETED
```

A matriz demonstra rastreabilidade documental da proposta; não demonstra
adoção, canonicalização, conformidade automática de prompts existentes ou
resultado operacional em projetos consumidores.
