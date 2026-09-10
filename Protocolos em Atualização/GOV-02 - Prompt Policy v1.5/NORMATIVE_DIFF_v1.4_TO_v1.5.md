# Diff Normativo — v1.4 → v1.5

```text
STATUS = PROPOSED / DRAFT
SOURCE_BASELINE = Politica-Prompts-Agente-v1.4.md
TARGET = Politica-Prompts-Agente-v1.5.md
CHANGE_SCOPE = F03_MULTIAGENT_GOVERNANCE_HARDENING_ONLY
V1_4_MODIFIED = NO
CANONICALIZATION = NO
PROPAGATION = NO
USER_REVIEW_REQUIRED = YES
```

## 1. Preflight de versão e authority

O preflight recuperado do Governance Control Room registrou:

```text
EXISTING_TRANSVERSAL_PROMPT_POLICY_v1_5 = NO
EXISTING_NAMED_AGENT_PROMPT_ARTIFACT_v1_5 = YES
EXISTING_MULTIAGENT_TEMPLATE_v1_5 = YES
EXACT_VERSION_COLLISION = NO
VERSION_COLLISION = NO
BLOCKING_AUTHORITY_COLLISION = NO
SAFE_TO_USE_VERSION_v1_5 = YES
```

Os artefatos existentes com nomenclatura própria ou pertencentes a outra
família documental não são sobrescritos, reconciliados nem propagados por esta
proposta. A nova policy mantém identidade transversal e não introduz nomes
próprios de agentes ou projetos.

## 2. Resumo executivo

| Classificação | Quantidade | Escopo |
|---|---:|---|
| ADDED | 4 blocos normativos | decisão multiagente, revisão, escalonamento e gate |
| CHANGED | 2 regras | default direto e critério de admissibilidade |
| REMOVED/RESTRICTED | 1 permissividade | cobertura/revisão genérica não bastam sozinhas |
| UNCHANGED | demais seções | modelo, esforço, skills, UI, prompt e relatório |

Nenhuma alteração não relacionada foi introduzida.

```text
UNRELATED_NORMATIVE_CHANGES = 0
```

## 3. Mudanças materiais

### 3.1 Default e subagente opcional

```text
CLASSIFICATION = CHANGED
SECTION = 2. Multiagentes
V1_4_BEHAVIOR = Execução direta era o padrão quando não havia benefício verificável; subagentes eram permitidos em condições amplas.
V1_5_BEHAVIOR = Execução direta é o padrão; uso opcional ou preventivo é proibido e o resultado pode ser explicitamente DIRECT/SUBAGENTS_ALLOWED=NO.
REASON = Remover a ambiguidade entre “permitido” e “necessário”.
F03_GAP_ADDRESSED = OPTIONAL_SUBAGENT e delegação preventiva.
BACKWARD_COMPATIBILITY_IMPACT = Restringe interpretações permissivas; não altera seleção de modelo, esforço ou skills.
```

### 3.2 Critério material e verificável

```text
CLASSIFICATION = CHANGED
SECTION = 2. Multiagentes
V1_4_BEHAVIOR = Frentes independentes, especialização clara, paralelismo, cobertura ou revisão podiam justificar subagente.
V1_5_BEHAVIOR = Pelo menos uma de cinco condições materiais deve ser verdadeira, acompanhada de benefício material verificável e evidência.
REASON = Transformar a régua em decisão auditável e impedir justificativas genéricas.
F03_GAP_ADDRESSED = Falta de limiar explícito e risco de keyword matching.
BACKWARD_COMPATIBILITY_IMPACT = Casos anteriormente aceitos apenas por cobertura/revisão genérica passam a DIRECT.
```

As cinco condições são:

```text
PARALLEL_INDEPENDENT_FRONTS
DISTINCT_SPECIALIZATION_REQUIRED
MATERIAL_DECOMPOSITION_GAIN
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW
```

### 3.3 Tamanho, importância e criticidade

```text
CLASSIFICATION = ADDED
SECTION = 2. Multiagentes
V1_4_BEHAVIOR = Não havia negações textuais específicas para tamanho, importância ou criticidade.
V1_5_BEHAVIOR = TASK_IMPORTANT, TASK_LARGE e TASK_CRITICAL não implicam SUBAGENT_ALLOWED.
REASON = Fechar atalhos de escalonamento por aparência da tarefa.
F03_GAP_ADDRESSED = Reviewer/subagente preventivo por criticidade ou tamanho.
BACKWARD_COMPATIBILITY_IMPACT = Torna explícita uma restrição compatível com o princípio de parcimônia já existente.
```

### 3.4 Taxonomia de revisão

```text
CLASSIFICATION = ADDED
SECTION = 2.1 Taxonomia de revisão
V1_4_BEHAVIOR = Revisão aparecia como possível benefício, sem separar self-review de revisão independente.
V1_5_BEHAVIOR = REVIEW_PASS != INDEPENDENT_AGENT_REVIEW; self-review, consistency check e adversarial pass podem ser feitos diretamente.
REASON = Evitar criação automática de reviewer.
F03_GAP_ADDRESSED = REVIEW_REQUIRED não deve implicar REVIEWER_SUBAGENT_REQUIRED.
BACKWARD_COMPATIBILITY_IMPACT = Preserva revisão; restringe somente a inferência de que ela exige outro agente.
```

### 3.5 Escalonamento

```text
CLASSIFICATION = ADDED
SECTION = 2.2 Autoridade de escalonamento
V1_4_BEHAVIOR = Escalonamento era tratado como decisão por evidência, sem sequência operacional explícita nem proibição textual de autoabertura.
V1_5_BEHAVIOR = AUTO_ESCALATION=NO; STOP → REPORT EVIDENCE → RECOMMEND ESCALATION → USER DECISION.
REASON = Preservar authority final do usuário quando a insuficiência só aparece durante a execução.
F03_GAP_ADDRESSED = Abertura automática de novo agente durante execução.
BACKWARD_COMPATIBILITY_IMPACT = Nenhuma execução válida é invalidada; a continuação passa a exigir decisão do usuário.
```

### 3.6 Decision gate

```text
CLASSIFICATION = ADDED
SECTION = 2.3 Decision gate verificável
V1_4_BEHAVIOR = Existiam critérios qualitativos, mas não um registro padronizado de decisão nem regra para evidência insuficiente.
V1_5_BEHAVIOR = Cada condição é registrada como YES/NO; condição sem evidência suficiente vale NO; todas NO obrigam DIRECT.
REASON = Produzir uma decisão reproduzível e auditável.
F03_GAP_ADDRESSED = Ambiguidade operacional e escalonamento por palavras-chave.
BACKWARD_COMPATIBILITY_IMPACT = Melhora enforcement sem alterar o concern governado.
```

### 3.7 Policy separada

```text
CLASSIFICATION = ADDED/CONFIRMED
SECTION = 2.4 Não criar policy separada nesta versão
V1_4_BEHAVIOR = O agrupamento multiagente existia dentro da Prompt Policy, sem decisão explícita contra extração imediata.
V1_5_BEHAVIOR = SEPARATE_MULTIAGENT_DELEGATION_POLICY=NO; possíveis limiares de extração futura são apenas registrados.
REASON = Evitar fragmentação de authority nesta correção.
F03_GAP_ADDRESSED = Confusão entre hardening da Prompt Policy e criação de nova authority.
BACKWARD_COMPATIBILITY_IMPACT = Nenhuma; preserva a família documental.
```

## 4. Seções preservadas sem mudança normativa

As seções abaixo foram mantidas substancialmente conforme a v1.4:

| Seção | Estado | Observação |
|---|---|---|
| 0. Finalidade, escopo e versionamento | UNCHANGED | Apenas metadados de proposta foram adicionados no cabeçalho |
| 1. Modelo, esforço e categoria | UNCHANGED | Tabela, níveis e regra de parcimônia preservados |
| 3. Skills / Capabilities | UNCHANGED | Bloco obrigatório e `NONE` preservados |
| 4. UI, Sites e revisão visual | UNCHANGED | Sem transferência de authority |
| 5. Parcimônia e separação | UNCHANGED | Separações MODEL/EFFORT/MULTIAGENT/SKILLS preservadas |
| 6. Disponibilidade e authority | UNCHANGED | Sem capabilities inventadas |
| 7. Estrutura obrigatória | UNCHANGED | Preâmbulo, idioma e limites de ação preservados |
| 8. Fluxo | CHANGED minimally | Apenas referência ao novo gate e à sequência de escalonamento |
| 9. Exemplos | CHANGED minimally | Exemplo B explicita o resultado já decorrente de execução direta |
| 10. Relatório final | CHANGED minimally | Inclui resultado do decision gate |
| 11. Princípios finais | CHANGED minimally | Reordena e explicita as regras adicionadas |

## 5. Compatibilidade retroativa

```text
MODEL_SELECTION_COMPATIBILITY = PRESERVED
EFFORT_SELECTION_COMPATIBILITY = PRESERVED
SKILLS_BLOCK_COMPATIBILITY = PRESERVED
UI_SITE_RULES_COMPATIBILITY = PRESERVED
DIRECT_EXECUTION_COMPATIBILITY = PRESERVED_AND_STRENGTHENED
MULTIAGENT_COMPATIBILITY = NARROWED_TO_MATERIAL_VERIFIABLE_CASES
USER_FINAL_AUTHORITY = PRESERVED
ANALYTICAL_INDEPENDENCE = PRESERVED
```

Prompts da v1.4 que já escolhem execução direta continuam compatíveis. Prompts
que inferem subagente somente por tamanho, importância, criticidade, cobertura
genérica ou “reviewer por segurança” exigem reavaliação sob o novo gate.

## 6. Controle de integridade e não propagação

```text
V1_4_FILE_EDITED = NO
PROJECT_OPENING_EDITED = NO
AGENT_CONTINUITY_EDITED = NO
MANIFEST_EDITED = NO
HASH_EDITED = NO
PACKAGE_REBUILT = NO
PROJECT_ARTIFACTS_UPDATED = NO
CANONICAL_AUTHORITY_REPLACED = NO
```

Esta proposta não atualiza manifests, hashes ou pacotes. Nenhum artefato
existente com outra família ou nomenclatura é sobrescrito.

## 7. Adjudicação da proposta

```text
GOV_02_STATUS = PASS_WITH_USER_REVIEW
VERSION_COLLISION = NO
SAFE_TO_USE_VERSION_v1_5 = YES
POLICY_DRAFT_COMPLETE = YES
NORMATIVE_DIFF_COMPLETE = YES
F03_FULLY_ADDRESSED_IN_PROPOSAL = YES
UNRELATED_NORMATIVE_CHANGES = 0
CANONICALIZATION_AUTHORIZED = NO
PACKAGE_PROPAGATION_AUTHORIZED = NO
PROJECT_PROPAGATION_AUTHORIZED = NO
USER_REVIEW_REQUIRED = YES
```
