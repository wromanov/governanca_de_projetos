# GOV-09 — Evidência de remediação F01/F02/F03

```text
REMEDIATION_DATE = 2026-09-06
REMEDIATION_MODE = ISOLATED_STAGING_ONLY
STAGE = REMEDIATION_STAGE_F01_F02_F03_R3
ACTIVE_VIGENTE_REPRESENTATIONS_CHANGED = NO
POLICY_SOURCE_CHANGED = NO
CANONICALIZATION_EXECUTED = NO
PROMOTION_EXECUTED = NO
STAGE_COMMIT_EXECUTED = NO
PUSH_EXECUTED = NO
```

## Resultado

```text
F01_STATUS = PASS
F02_STATUS = PASS
F03_STATUS = PASS
REMEDIATION_STATUS = PASS_IN_STAGING
```

## F01 — Entrypoints e provenance

Os entrypoints foram reconciliados com suas árvores sem trocar a identidade
dos packages:

| Package | `START_HERE.md` | Tamanho | SHA256 |
|---|---|---:|---|
| Continuidade | `CONTINUITY_PACKAGE/START_HERE.md` | 1101 | `D1CF542E61B7266CC7A5210BCB9247E1E858F7F96AF2E95A409A2F70BFA45D2B` |
| Abertura | `OPENING_PACKAGE/START_HERE.md` | 1673 | `526763B472386396831DD159E37FC1EF86887229A5DD0BC7BF9474653C33712F` |

Cada entrypoint está presente no tree e no ZIP correspondente. O entrypoint
de Continuidade não aparece no package de Abertura e vice-versa.

## F02 — Composição, manifests e packages

```text
CONTINUITY_TREE_FILES = 8
CONTINUITY_ZIP_FILES = 8
OPENING_TREE_FILES = 42
OPENING_ZIP_FILES = 42
TREE_ZIP_CONTINUITY_EQUAL = YES
TREE_ZIP_OPENING_EQUAL = YES
CONTINUITY_MANIFEST_MISMATCHES = 0
STARTER_MANIFEST_MISMATCHES = 0
PACKAGE_MANIFEST_MISMATCHES = 0
```

O package de Continuidade contém o `CONTINUITY_MANIFEST.md` e o
`PROJECT_SPECIFIC_PAYLOAD/`, sem o `Agent-Continuity-Standard-v1.0/README.md`
que pertence ao package de Abertura. O package de Abertura contém o
`STARTER_MANIFEST.md`, o `Project Opening Standard v1.0/` e o README do
standard, sem os artifacts específicos de Continuidade.

## F03 — Registry de hashes

```text
CONTINUITY_ZIP_SHA256 = C220BB050D0E70E6FB487A63690438B527E57C66FBAD14A38B006DADA4DE4C55
OPENING_ZIP_SHA256 = 8A8B2E5E3902B6B4812043CE2579D64AFE605936CA6D75A5BDC38B159DAD04BD
PROJECT_STATE_CONTINUITY_HASH_MATCH = YES
OPENING_HASH_REGISTRY = THIS_ARTIFACT
```

O `PROJECT_STATE.md` permanece dentro do ZIP de Abertura. Portanto, registrar
o hash integral do próprio ZIP dentro desse arquivo criaria uma dependência
autorreferencial não convergente. A remediação torna isso explícito:

```text
OPENING_ZIP_SHA256 = EXTERNAL_PACKAGE_AUDIT_REGISTRY
OPENING_ZIP_SHA256_NOTE = PROJECT_STATE is inside the opening archive; the full archive hash is recorded out of band to avoid a self-referential hash.
```

O hash integral do ZIP é registrado acima neste artifact externo, enquanto o
hash do ZIP de Continuidade permanece verificável diretamente no state porque
esse ZIP não contém o `PROJECT_STATE.md`.

## Limite operacional

Este registro fecha F01/F02/F03 apenas para o staging reproduzível indicado
acima. As representações em `Protocolos para Projetos - Vigente/` permanecem
inalteradas. A substituição coordenada das trees, manifests e ZIPs continua
dependente de validação final do package e de autorização física separada.

```text
READY_FOR_STAGING_PACKAGE_AUDIT = YES
READY_FOR_PROMOTION_EXECUTION = NO
PROMOTION_AUTHORIZED = NO
```
