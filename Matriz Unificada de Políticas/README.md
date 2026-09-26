# Matriz Unificada de Políticas

Governance Baseline V1 é a baseline canônica e ativa para governança global de projetos. GOVERNANCE_CONTRACT_VERSION = 1.

Este README é uma visão descritiva; as authorities normativas permanecem na Matriz e no POLICY_REGISTRY.

## Authorities operacionais

- PM-00 v1.0: matriz canônica de arquitetura da governança.
- PM-01 v1.0: condução, integração, avanço, continuidade e rastreabilidade de projetos.
- PM-02 R2.6: geração de prompts e recomendação de roteamento.
- PM-03 R2.3: execução DIRECT vs MULTIAGENT e delegação.
- PM-04 v1.2: uso de capacidades, skills e plugins; alinhamento operacional com PM-02 R2.6.
- PM-05 v1: independência analítica, evidência e qualidade decisória.
- VP-01 v2.0: protocolo canônico de validação, com AUTHORITY_SCOPE = VALIDATION_ONLY.

PM-04 v1.1 e VP-01 v1.0 estão SUPERSEDED / HISTORICAL. Suas versões históricas permanecem registradas; não são carregadas como authority global atual. Há uma versão operacional atual por ID.

## Estrutura

- policies/ contém as policies operacionais atuais e as versões históricas supersedidas.
- validation/ contém VP-01 v2.0, separado das subpolicies; é read-only e não cria policies nem promove candidates.
- POLICY_REGISTRY.json registra identidade, estado, proveniência, supersession, baseline e hashes.
- MATRIX_BUILD_REPORT.md registra GOV-01C como evidência de entrada e os resultados desta canonicalização.
- PREWRITE_AUDIT.md é evidência histórica da revisão anterior à canonicalização.

Protocolos operacionais continuam fora de policies/. Opening 2.0 e Continuity 2.0 são versões PRESERVED LEGACY ROLLBACK / SUPERSEDED. Cópias embutidas de policies e VP-01 v1.0 são PACKAGE_LOCAL_LEGACY_SNAPSHOTS e não representam a authority global atual. Durante GOV-01D, os pacotes 2.0 ainda eram preservados sem modificação; essa nota é histórica. Opening 3.0 e Continuity 3.0 são CANONICAL / ACTIVE, nativos ao Governance Contract Version 1. GOV-04 está COMPLETE e o DOCUMENTATION_GOVERNANCE_PROGRAM está CLOSED. Nenhum projeto real foi migrado automaticamente.
