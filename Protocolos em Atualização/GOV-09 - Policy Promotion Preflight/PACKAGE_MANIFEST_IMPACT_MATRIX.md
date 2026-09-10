# GOV-09 — Matriz de Impacto de Manifestos e Packages

`REVIEW_MODE = CONTROLLED_READ_ONLY`

Nenhuma linha dos arquivos abaixo foi alterada nesta atividade. `UPDATE_REQUIRED`
descreve a mudança necessária em uma futura promoção autorizada.

## 1. Policies aprovadas e históricas

| Arquivo | UPDATE_REQUIRED | UPDATE_TYPE | Tratamento futuro |
|---|---|---|---|
| `Protocolos em Atualização/GOV-07 - Prompt Policy v1.6/Politica-Prompts-Agente-v1.6.md` | NO | — | fonte aprovada imutável; `APPROVED_CONTENT_HASH` permanece `F9EC62AF...FF8B5` |
| `Protocolos em Atualização/GOV-05 - Skills Policy v1.1/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | NO | — | fonte aprovada imutável; `APPROVED_CONTENT_HASH` permanece `6C67CDA7...DDA2` |
| `Protocolos em Atualização/GOV-02 - Prompt Policy v1.5/Politica-Prompts-Agente-v1.5.md` | NO | — | preservar como `HISTORICAL INTERMEDIATE DRAFT`, nunca como canonical |
| evidências GOV-02, GOV-05, GOV-07 e GOV-08 | NO | — | preservar como revisão histórica; referências a drafts e baselines não são references ativas |

As fontes aprovadas não devem ser editadas para virar canônicas. A
canonicalização futura deve produzir uma representação final separada, com
hash final próprio.

## 2. Representações ativas e árvores extraídas

| Arquivo/representação atual | UPDATE_REQUIRED | UPDATE_TYPE | Dependência futura |
|---|---|---|---|
| `Protocolo - Inicio ... - Final/Agent-Continuity-Standard-v1.0/policies/Politica-Prompts-Agente-v1.4.md` | YES | `FILENAME`, `VERSION_REFERENCE`, `SHA256`, `MANIFEST_ENTRY`, `PROVENANCE` | substituir a representação ativa pela v1.6; preservar v1.4 em snapshot/histórico |
| `Protocolo - Continuidade ... - Final/Agent-Continuity-Standard-v1.0/policies/Politica-Prompts-Agente-v1.4.md` | YES | `FILENAME`, `VERSION_REFERENCE`, `SHA256`, `MANIFEST_ENTRY`, `PROVENANCE` | substituir a representação ativa pela v1.6; preservar v1.4 em snapshot/histórico |
| `Protocolo - Inicio ... - Final/Agent-Continuity-Standard-v1.0/policies/Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | YES | `FILENAME`, `VERSION_REFERENCE`, `SHA256`, `MANIFEST_ENTRY`, `PROVENANCE` | substituir a representação ativa pela v1.1; preservar v1.0 em snapshot/histórico |
| `Protocolo - Continuidade ... - Final/Agent-Continuity-Standard-v1.0/policies/Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | YES | `FILENAME`, `VERSION_REFERENCE`, `SHA256`, `MANIFEST_ENTRY`, `PROVENANCE` | substituir a representação ativa pela v1.1; preservar v1.0 em snapshot/histórico |
| `Protocolo - Continuidade ... - Final/START_HERE.md` | YES | `PACKAGE_INVENTORY`, `PROVENANCE`, `STATUS` | restaurar o entrypoint de Continuidade nesta árvore |
| `Protocolo - Inicio ... - Final/START_HERE.md` | YES | `PACKAGE_INVENTORY`, `PROVENANCE`, `STATUS` | restaurar o entrypoint de Início de Abertura nesta árvore |
| `Protocolo - Continuidade ... - Final/Agent-Continuity-Standard-v1.0/README.md` | YES | `PACKAGE_INVENTORY`, `PROVENANCE` | alinhar a árvore com `CONTINUITY_MANIFEST`/ZIP correspondente |
| `Protocolo - Inicio ... - Final/PROJECT_SPECIFIC_PAYLOAD/README.md` | YES | `PACKAGE_INVENTORY`, `PROVENANCE` | alinhar a árvore com o package de Continuidade, não com o package de Abertura |
| `Protocolo - Inicio ... - Final/CONTINUITY_MANIFEST.md` | YES | `PACKAGE_INVENTORY`, `PROVENANCE` | alinhar localização física e representação do package de Continuidade |

Os três últimos itens são impactos de composição já existentes. Nenhum será
movido ou corrigido no preflight.

## 3. Manifests e state

| Arquivo | UPDATE_REQUIRED | UPDATE_TYPE | Razão |
|---|---|---|---|
| `Protocolo - Inicio ... - Final/STARTER_MANIFEST.md` | YES | `VERSION_REFERENCE`, `FILENAME`, `SHA256`, `MANIFEST_ENTRY`, `PACKAGE_INVENTORY`, `STATUS`, `PROVENANCE` | trocar entries de v1.4/v1.0 por v1.6/v1.1, registrar hashes finais, corrigir composição e atualizar hashes transitivos |
| `Protocolo - Inicio ... - Final/CONTINUITY_MANIFEST.md` | YES | `VERSION_REFERENCE`, `FILENAME`, `SHA256`, `MANIFEST_ENTRY`, `PACKAGE_INVENTORY`, `STATUS`, `PROVENANCE` | mesma troca para o package de Continuidade e correção da localização/composição |
| `Protocolo - Inicio ... - Final/Project Opening Standard v1.0/PACKAGE_MANIFEST.md` | YES | `SHA256`, `MANIFEST_ENTRY` | seu entry de `PROJECT_STATE.md` deve mudar se `PROJECT_STATE.md` registrar os novos package hashes |
| `Protocolo - Inicio ... - Final/Project Opening Standard v1.0/PROJECT_STATE.md` | YES | `SHA256`, `PACKAGE_INVENTORY`, `STATUS`, `PROVENANCE` | atualizar hashes dos ZIPs após rebuild, preservando os hashes anteriores como histórico |

Não foi encontrado hash registry separado. Os manifests e `PROJECT_STATE.md`
formam o registry observado nesta árvore.

### 3.1 Cadeia de hashes futura

```text
canonical artifact final hash
  -> policy entry em STARTER_MANIFEST / CONTINUITY_MANIFEST
  -> manifest hash
  -> PACKAGE_MANIFEST/PROJECT_STATE conforme inventory
  -> ZIP interno
  -> ZIP package hash
  -> PROJECT_STATE package hash
```

Cada nível deve ser recalculado em staging. Não é seguro alterar somente o
nome do arquivo ou somente o hash no manifest.

## 4. Packages

| Package | CONTAINS_OLD_POLICY | REFERENCES_OLD_POLICY | REBUILD_REQUIRED | UPDATE_TYPE |
|---|---|---|---|---|
| `Protocolos para Projetos - Vigente/Protocolo-Continuidade-Projeto-Em-Andamento-Com-Novo-Agente-FINAL-AUDIT.zip` | YES | YES | YES | `FILENAME`, `VERSION_REFERENCE`, `SHA256`, `MANIFEST_ENTRY`, `PACKAGE_INVENTORY`, `STATUS`, `PROVENANCE` |
| `Protocolos para Projetos - Vigente/Protocolo-Inicio-de-Abertura-de-Projeto-FINAL-AUDIT.zip` | YES | YES | YES | `FILENAME`, `VERSION_REFERENCE`, `SHA256`, `MANIFEST_ENTRY`, `PACKAGE_INVENTORY`, `STATUS`, `PROVENANCE` |

Os manifests internos atuais são byte-consistentes com seus próprios entries,
mas os ZIPs têm composição diferente das árvores extraídas e os hashes dos
ZIPs divergem do `PROJECT_STATE.md`. Isso mantém o rebuild bloqueado até a
adjudicação da baseline física.

## 5. Impacto em referências antigas

| Fonte da referência | UPDATE_REQUIRED | Decisão |
|---|---|---|
| policies v1.4/v1.0 em caminho ativo | YES | substituir representation ativa; referência histórica fica fora do caminho ativo |
| manifests de distribuição | YES | atualizar nomes, hashes, entries e estado |
| `PROJECT_STATE.md` | YES | atualizar package hashes somente depois de package rebuild validado |
| ZIPs | YES | reconstruir os dois packages coordenadamente |
| GOV-02/GOV-05/GOV-07/GOV-08 | NO | imutáveis; são evidência histórica, não source of truth vigente |
| referências de baseline dentro das candidatas | NO | preservar como provenance; não remover a genealogia |

## 6. Gate da matriz

`MANIFEST_FILES_REQUIRING_UPDATE = STARTER_MANIFEST.md; CONTINUITY_MANIFEST.md; PACKAGE_MANIFEST.md; PROJECT_STATE.md`

`PACKAGE_REBUILD_SCOPE_KNOWN = YES`

`MANIFEST_IMPACT_KNOWN = YES`

`CURRENT_HASH_REGISTRY_IS_DISTRIBUTED = YES`

`MANIFEST_WRITE = PROHIBITED`
