# GOV-09 — Inventário de Canonicalização

`REVIEW_MODE = CONTROLLED_READ_ONLY`

`PROMOTION_EXECUTION = NOT_AUTHORIZED`

`POLICY_WRITE = PROHIBITED`

`VIGENTE_WRITE = PROHIBITED`

`PACKAGE_WRITE = PROHIBITED`

`MANIFEST_WRITE = PROHIBITED`

`HASH_REGISTRY_WRITE = PROHIBITED`

## 1. Identidade das fontes

Os hashes abaixo foram recalculados no filesystem local em 2026-09-06.

| Artefato | Papel | Representação observada | SHA256 esperado | SHA256 observado | Gate |
|---|---|---|---|---|---|
| `Politica-Prompts-Agente-v1.6.md` | candidata transversal aprovada | `Protocolos em Atualização/GOV-07 - Prompt Policy v1.6/` | `F9EC62AF541766E95C5A52115977C8AEDE27E93DCF61037D2F18DB3A5C0FF8B5` | `F9EC62AF541766E95C5A52115977C8AEDE27E93DCF61037D2F18DB3A5C0FF8B5` | PASS |
| `Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | candidata especializada aprovada | `Protocolos em Atualização/GOV-05 - Skills Policy v1.1/` | `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` | `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` | PASS |
| `Politica-Prompts-Agente-v1.4.md` | authority vigente atual | duas cópias extraídas; duas cópias dentro dos ZIPs | não aplicável | `8006DB0B5161B6CAC1604203BA5EAC09AAE964C5E65BCA6B00C3194B387AD069` | PASS |
| `Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | authority especializada vigente atual | duas cópias extraídas; duas cópias dentro dos ZIPs | não aplicável | `C0D657C673B93719F250DCB52F2DA5853E1C33ECA202D769570A8EF742D5D695` | PASS |
| `Politica-Prompts-Agente-v1.5.md` | draft intermediário histórico | `Protocolos em Atualização/GOV-02 - Prompt Policy v1.5/` | não aplicável | `D59CC8BCCB5DC675907A774D65278A8516ECB8543C68F41A30A9089FDE4CC53B` | PRESERVE |

Não há divergência de hash entre as duas cópias extraídas de cada policy
vigente. Não foi encontrada uma cópia candidata v1.6 ou v1.1 dentro de
`Protocolos para Projetos - Vigente`.

## 2. Authority lógica e representações

O modelo aprovado é `ONE_LOGICAL_AUTHORITY = YES` e
`MULTIPLE_REPRESENTATIONS = ALLOWED`.

| Logical authority ID | Authority vigente atual | Representações vigentes atuais | Target futuro após promoção |
|---|---|---|---|
| `PROMPT_POLICY_TRANSVERSAL` | Prompt v1.4 | v1.4 em duas árvores extraídas e nos dois ZIPs | v1.6 no caminho ativo equivalente de cada árvore, no ZIP de continuidade e no ZIP de abertura; v1.4 somente em histórico/provenance |
| `SKILLS_PLUGINS_POLICY_TRANSVERSAL_SPECIALIZED` | Skills v1.0 | v1.0 em duas árvores extraídas e nos dois ZIPs | v1.1 no caminho ativo equivalente de cada árvore, no ZIP de continuidade e no ZIP de abertura; v1.0 somente em histórico/provenance |

Os arquivos aprovados em GOV-05 e GOV-07 são fontes de conteúdo aprovadas e
devem permanecer imutáveis. A futura canonicalização deve gerar artefatos
canônicos a partir dessas fontes, sem transformar a cópia draft aprovada em
uma segunda authority lógica.

## 3. Inventário físico de `Protocolos para Projetos - Vigente`

### 3.1 Cópias de policies

As duas cópias extraídas de cada authority atual são:

| Policy | Caminho 1 | Caminho 2 | Hash comum |
|---|---|---|---|
| Prompt v1.4 | `Protocolo - Inicio de Abertura de Projeto - Final/Agent-Continuity-Standard-v1.0/policies/Politica-Prompts-Agente-v1.4.md` | `Protocolo - Continuidade de Projeto em Andamento Com Novo Agente - Final/Agent-Continuity-Standard-v1.0/policies/Politica-Prompts-Agente-v1.4.md` | `8006DB0B...7AD069` |
| Skills v1.0 | `Protocolo - Inicio de Abertura de Projeto - Final/Agent-Continuity-Standard-v1.0/policies/Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | `Protocolo - Continuidade de Projeto em Andamento Com Novo Agente - Final/Agent-Continuity-Standard-v1.0/policies/Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | `C0D657C6...D5D695` |

Não há cópia solta adicional dessas duas policies fora das árvores e dos
packages listados abaixo. Os ZIPs também contêm as duas policies antigas.

### 3.2 Arquivos de índice, entrada e estado

Foram localizados:

- `START_HERE.md`: uma cópia em cada árvore extraída;
- `STARTER_MANIFEST.md`: somente na árvore de abertura;
- `CONTINUITY_MANIFEST.md`: fisicamente na árvore de abertura;
- `Project Opening Standard v1.0/PACKAGE_MANIFEST.md`: somente na árvore de abertura;
- `Project Opening Standard v1.0/PROJECT_STATE.md`: somente na árvore de abertura;
- `PROJECT_SPECIFIC_PAYLOAD/README.md`: somente na árvore de abertura;
- `Agent-Continuity-Standard-v1.0/README.md`: somente na árvore de continuidade;
- não foi encontrado um hash registry separado por filename dedicado;
- os hashes também aparecem nos manifests, em `PROJECT_STATE.md` e nas
  evidências históricas GOV-02/GOV-05/GOV-07/GOV-08.

### 3.3 Desalinhamento dos entrypoints

Os hashes e conteúdos dos dois `START_HERE.md` estão cruzados em relação às
árvores:

| Árvore física | Hash observado | Conteúdo observado | Hash esperado pelo artefato de package |
|---|---|---|---|
| `Protocolo - Continuidade ... - Final/START_HERE.md` | `D1CF542E61B7266CC7A5210BCB9247E1E858F7F96AF2E95A409A2F70BFA45D2B` | entrypoint de Início de Abertura de Projeto | `CONTINUITY_MANIFEST` não está nessa árvore para fornecer o expected hash |
| `Protocolo - Inicio ... - Final/START_HERE.md` | `526763B472386396831DD159E37FC1EF86887229A5DD0BC7BF9474653C33712F` | entrypoint de Continuidade de Projeto | `STARTER_MANIFEST` espera `D1CF542E...F45D2B` |

O `STARTER_MANIFEST.md` registra `START_HERE.md` com tamanho 1101 e hash
`D1CF542E...F45D2B`; a árvore de abertura observada contém o arquivo de 1673
bytes e hash `526763B4...33712F`. Isso confirma `OPENING-F01`.

### 3.4 Composição das árvores extraídas

| Árvore | Arquivos observados | Diferenças relevantes em relação ao ZIP correspondente |
|---|---:|---|
| Continuidade extraída | 7 | falta `CONTINUITY_MANIFEST.md` e `PROJECT_SPECIFIC_PAYLOAD/README.md`; contém `Agent-Continuity-Standard-v1.0/README.md` que não está no ZIP de continuidade; `START_HERE.md` também está cruzado |
| Abertura extraída | 43 | contém `CONTINUITY_MANIFEST.md` e `PROJECT_SPECIFIC_PAYLOAD/README.md` extras; falta `Agent-Continuity-Standard-v1.0/README.md` que está no ZIP de abertura; `START_HERE.md` está cruzado |

As diferenças não são apenas de policy; são divergências de composição e de
entrypoint. A correção física não foi executada.

## 4. Packages e manifests internos

Os dois ZIPs observados contêm as policies antigas e referências nominais e
hashes às versões antigas:

| Package | Hash observado | Conteúdo | Referência antiga | Manifest interno | Rebuild futuro |
|---|---|---|---|---|---|
| `Protocolo-Continuidade-Projeto-Em-Andamento-Com-Novo-Agente-FINAL-AUDIT.zip` | `65FF5FE2A8F02F8D391B60E3D868C417A36B949FF7147E62F2B8831BBE5E2F88` | `YES` | `YES`, nas policies e em `CONTINUITY_MANIFEST.md` | `CONTINUITY_MANIFEST.md` consistente com os bytes internos, excluindo o self-hash | YES |
| `Protocolo-Inicio-de-Abertura-de-Projeto-FINAL-AUDIT.zip` | `AF831FEA999E01B020DB3E920291998A43EE4F84626C1DE0BC20E754BC170840` | `YES` | `YES`, nas policies e em `STARTER_MANIFEST.md` | `STARTER_MANIFEST.md` consistente com os bytes internos, excluindo o self-hash | YES |

O conteúdo de cada ZIP é internamente consistente com o próprio manifest:
foram observados zero mismatches de tamanho/hash nos entries listados. Isso
não elimina a divergência de composição entre ZIP e árvore extraída nem a
divergência entre `PROJECT_STATE.md` e os hashes físicos dos ZIPs.

`PROJECT_STATE.md` registra `CONTINUITY_ZIP_SHA256 =
6FDCB2B26EFCCF09C33BBDEA68A637B9AD64604683556F029A4495FDAED9E74E` e
`OPENING_ZIP_SHA256 = F26799CB688191A99A6C4E1D1BAFAC561F67E5A6B04CC447F55FFE68849076A9`.
Ambos divergem dos ZIPs observados. Isso confirma `OPENING-F03`.

## 5. Referências antigas e classificação

As referências antigas foram encontradas em:

1. as quatro cópias físicas das policies vigentes e os dois ZIPs;
2. `STARTER_MANIFEST.md`, com nomes, tamanhos e hashes de v1.4/v1.0;
3. `CONTINUITY_MANIFEST.md`, com nomes, tamanhos e hashes de v1.4/v1.0;
4. `Politica-Prompts-Agente-v1.5.md` e suas evidências GOV-02, como
   provenance histórica;
5. evidências GOV-05/GOV-07/GOV-08, como rastreabilidade histórica e de
   aprovação;
6. `Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md`, especialmente a
   seção de alinhamento, como baseline e referência histórica.

As referências em GOV-02 a GOV-08 não devem ser reescritas: são evidências
imutáveis do estado de revisão. Uma referência histórica não é uma referência
ativa concorrente.

## 6. Preservação histórica

| Versão | Classificação obrigatória | Destino lógico futuro |
|---|---|---|
| Prompt v1.4 | `HISTORICAL CANONICAL PREDECESSOR` | snapshot imutável de pre-promotion e arquivo histórico fora do caminho ativo de policy |
| Prompt v1.5 | `HISTORICAL INTERMEDIATE DRAFT`; `NEVER_CANONICAL` | manter o artefato GOV-02 e seu hash sem reclassificação |
| Skills v1.0 | `HISTORICAL CANONICAL PREDECESSOR` | snapshot imutável de pre-promotion e arquivo histórico fora do caminho ativo de policy |

O destino físico definitivo do arquivo histórico deve ser materializado somente
durante uma promoção explicitamente autorizada, com snapshot e rollback
registrados. Este preflight não cria, move, copia, renomeia ou apaga nenhum
histórico.

## 7. Findings de Project Opening

| Finding | Evidência local | Impacto na promoção |
|---|---|---|
| `OPENING-F01` | `STARTER_MANIFEST.md` espera hash/content de um `START_HERE` e a árvore de abertura contém o outro entrypoint; os dois `START_HERE` estão cruzados | `BLOCKING` |
| `OPENING-F02` | ZIPs e árvores extraídas têm conjuntos distintos de arquivos; há manifest/payload ausentes de uma árvore, README ausente de outra e entrypoints trocados | `BLOCKING` |
| `OPENING-F03` | hashes registrados em `PROJECT_STATE.md` não são os hashes dos dois ZIPs observados | `BLOCKING` |

Os findings não foram corrigidos. Eles impedem declarar que todos os
representations atuais são a mesma distribuição coordenada.

## 8. Conclusão do inventário

`VIGENTE_INVENTORY_COMPLETE = YES`

`LOGICAL_AUTHORITY_MODEL = ONE_LOGICAL_AUTHORITY_WITH_MULTIPLE_REPRESENTATIONS`

`HISTORICAL_PRESERVATION_MODEL = READY_WITH_EXPLICIT_SNAPSHOT_REQUIRED`

`STOP_AT_SAFE_BOUNDARY = YES`

`READY_FOR_PROMOTION_EXECUTION = NO`
