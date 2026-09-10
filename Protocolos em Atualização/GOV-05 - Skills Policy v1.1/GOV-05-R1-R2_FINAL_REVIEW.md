# GOV-05-R1-R2 — Final Normative Review

## Escopo controlado

`REVIEW_MODE = CONTROLLED_READ_ONLY`  
`POLICY_WRITE = PROHIBITED`  
`EVIDENCE_ARTIFACT_WRITE = ALLOWED`

Foram usadas como fontes mandatórias: baseline v1.0, candidata v1.1, Prompt Policy v1.4 vigente e catálogo operacional v1.0. A v1.5 foi lida somente como fonte de apoio/draft. Artefatos derivados históricos não foram usados como evidência de conformidade atual.

## Source gates e identidade

| Gate/fonte | Resultado | Evidência |
|---|---|---|
| Mandatory source 01 — v1.0 | PASS | presente; SHA256 `C0D657C673B93719F250DCB52F2DA5853E1C33ECA202D769570A8EF742D5D695` |
| Mandatory source 02 — v1.1 | PASS | presente, cabeçalho confirmado (`Política de Uso de Skills e Plugins OpenAI — Codex + Work`; versão 1.1; `STATUS = PROPOSED`; `LIFECYCLE = DRAFT`) e SHA256 esperado confirmado |
| Mandatory source 03 — Prompt Policy v1.4 | PASS | presente; `STATUS = CANONICAL`; SHA256 `8006DB0B5161B6CAC1604203BA5EAC09AAE964C5E65BCA6B00C3194B387AD069` |
| Mandatory source 04 — catálogo docx | PASS | presente; SHA256 esperado confirmado |
| Source identity v1.1 | PASS | esperado e obtido: `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` |
| Reference source catalog | PASS | esperado e obtido: `7F6B23E943C92CC96F72DBE990368038B0B274FDC1A37181C4A1A9DE7AA0C5D6` |
| v1.0 distinto da v1.1 | PASS | hashes distintos |
| Modificação inesperada de policy durante a revisão | NO | hashes de fontes mandatórias preservados na validação final |

## Resultado normativo

`INTEGRAL_SOURCE_COMPARISON = PASS`

A comparação integral está detalhada em `NORMATIVE_DIFF_v1.0_TO_v1.1.md`.

| Controle | Resultado |
|---|---|
| Minimum sufficient capability | PRESERVED |
| Native first | PRESERVED |
| No skill by availability only | PRESERVED |
| No plugin by installation only | PRESERVED |
| Authority not transferred | PRESERVED |
| Capability is not permission | PRESERVED |
| No silent decision replacement | PRESERVED e reforçado |
| Runtime availability matters | PRESERVED e reforçado |
| No tool sprawl | PRESERVED |
| Critical gates | PRESERVED |
| `CAPABILITY != SKILL` e `SKILL != PLUGIN` | PASS |
| `PLUGIN_MAY_CONTAIN_SKILLS` e `SKILL_MAY_EXIST_WITHOUT_PLUGIN` | PASS |
| Classificação por fonte, não sintaxe | PASS |
| Política de fonte de skills/plugins | PASS |
| Cabeçalho decisório completo | PASS |
| Disposição e invocação de plugins | PASS |
| Preservação de authority e write control | PASS |

## Taxonomia conferida

Deep Research e Plugin Management são plugins. Default templates é container de plugin; Operating Review é template/workflow, não plugin. ChatGPT Sites/`@Sites` é capacidade nativa de produto somente quando a superfície e documentação atuais confirmarem a classe. Codex é capacidade nativa; Work é superfície/ambiente nativo. Nome, sintaxe `@`/`$`/`/`, marca de produto e nome de template não determinam a classe.

## Prompt Policy sync findings

| Item | Resultado |
|---|---|
| Prompt Policy v1.4 disponível | YES |
| Prompt Policy v1.4 sync required | YES |
| Prompt Policy v1.5 disponível | YES |
| Prompt Policy v1.5 sync required | YES |
| Sync action authorized | NO |

O v1.4 ainda tem bloco de `Skills / Capabilities` sem decisão normativa equivalente de plugin, disponibilidade, invocação e confirmação. A v1.5 existe como `PROPOSED / DRAFT`, mas seu bloco correspondente também não absorve os campos/regras específicos de plugins da v1.1. São findings de sincronização; não constituem falha da candidata v1.1.

## Adversarial acceptance

`ADVERSARIAL_SCENARIOS_EXECUTED = A01-A19`  
`ADVERSARIAL_PASS = 19`  
`ADVERSARIAL_FAIL = 0`

Evidência individual: `ADVERSARIAL_USAGE_SCENARIOS.md`.

## Findings e decisão

1. **SYNC-F01 (não bloqueante):** Prompt Policy v1.4 requer sincronização estrutural após eventual canonicalização da v1.1.
2. **SYNC-F02 (não bloqueante):** Prompt Policy v1.5 está disponível, porém ainda exige sincronização antes de qualquer promoção coordenada.

Não foi encontrado conflito material de authority. Não houve mudança de policy, canonicalização, promoção, atualização de pacote/manifest/hash registry, stage, commit, push ou tag.

```text
SOURCE_IDENTITY_GATE = PASS
REFERENCE_SOURCE_GATE = PASS
CAPABILITY_SKILL_PLUGIN_MODEL = PASS
PLUGIN_INVOCATION_POLICY = PASS
HEADER_POLICY = PASS
SOURCE_POLICY = PASS
AUTHORITY_PRESERVATION = PASS
UNRELATED_NORMATIVE_CHANGES = 0
READY_FOR_USER_ADJUDICATION = YES
FINAL_DECISION = PASS_WITH_FINDINGS
```

## Artefatos desta execução

- `NORMATIVE_DIFF_v1.0_TO_v1.1.md`
- `SKILL_PLUGIN_CLASSIFICATION_MATRIX.md`
- `ADVERSARIAL_USAGE_SCENARIOS.md`
- `GOV-05-R1-R2_FINAL_REVIEW.md`

```text
CANONICALIZATION = NO
PROMOTION_TO_VIGENTE = NO
STAGE_EXECUTED = NO
COMMIT_EXECUTED = NO
PUSH_EXECUTED = NO
```
