# Policy Distribution Manifest

Este manifest registra a origem formal e o mirror de distribuição de cada policy transversal incluída no escopo. Os hashes usam SHA256.

| POLICY_ID | FAMILY | FILENAME | CLASS | SOURCE_PATH | MIRROR_PATH | SOURCE_SHA256 | MIRROR_SHA256 | BYTE_IDENTICAL | STATUS |
|---|---|---|---|---|---|---|---|---|---|
| PROMPT_POLICY_V1_4 | PROMPT_POLICY | `Politica-Prompts-Agente-v1.4.md` | CURRENT | `Protocolos para Projetos - Vigente/Protocolo - Inicio de Abertura de Projeto - Final/Agent-Continuity-Standard-v1.0/policies/Politica-Prompts-Agente-v1.4.md` | `Atuais/Politica-Prompts-Agente-v1.4.md` | `8006DB0B5161B6CAC1604203BA5EAC09AAE964C5E65BCA6B00C3194B387AD069` | `8006DB0B5161B6CAC1604203BA5EAC09AAE964C5E65BCA6B00C3194B387AD069` | YES | CANONICAL / VIGENTE |
| SKILLS_POLICY_V1_0 | SKILLS_POLICY | `Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | CURRENT | `Protocolos para Projetos - Vigente/Protocolo - Inicio de Abertura de Projeto - Final/Agent-Continuity-Standard-v1.0/policies/Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | `Atuais/Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | `C0D657C673B93719F250DCB52F2DA5853E1C33ECA202D769570A8EF742D5D695` | `C0D657C673B93719F250DCB52F2DA5853E1C33ECA202D769570A8EF742D5D695` | YES | CURRENT CANONICAL SKILLS BASELINE |
| ANALYTICAL_INDEPENDENCE_POLICY_V1 | ANALYTICAL_INDEPENDENCE | `Independencia-Analitica-Agente-v1.md` | CURRENT | `Protocolos para Projetos - Vigente/Protocolo - Inicio de Abertura de Projeto - Final/Agent-Continuity-Standard-v1.0/policies/Independencia-Analitica-Agente-v1.md` | `Atuais/Independencia-Analitica-Agente-v1.md` | `1692764FDCD3B0DA1171D77BCC41270E1EC3126BFD8EB263BFA9E0C0A83C8988` | `1692764FDCD3B0DA1171D77BCC41270E1EC3126BFD8EB263BFA9E0C0A83C8988` | YES | CURRENT TRANSVERSAL ANALYTICAL INDEPENDENCE POLICY |
| PROMPT_POLICY_V1_6 | PROMPT_POLICY | `Politica-Prompts-Agente-v1.6.md` | UPDATE_CANDIDATE | `Protocolos em Atualização/GOV-07 - Prompt Policy v1.6/Politica-Prompts-Agente-v1.6.md` | `Em Atualização/Politica-Prompts-Agente-v1.6.md` | `F9EC62AF541766E95C5A52115977C8AEDE27E93DCF61037D2F18DB3A5C0FF8B5` | `F9EC62AF541766E95C5A52115977C8AEDE27E93DCF61037D2F18DB3A5C0FF8B5` | YES | APPROVED CANDIDATE / PENDING CANONICALIZATION |
| SKILLS_PLUGINS_POLICY_V1_1 | SKILLS_PLUGINS_POLICY | `Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | UPDATE_CANDIDATE | `Protocolos em Atualização/GOV-05 - Skills Policy v1.1/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | `Em Atualização/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` | `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` | YES | APPROVED CANDIDATE / NOT YET PROMOTED |
| MULTIAGENT_POLICY_V1_7 | MULTIAGENT_POLICY | `AGENTS-Multiagente-Generico-v1.7.md` | UPDATE_CANDIDATE | `Protocolos em Atualização/GOV-03 - Politica Mult Agentes/AGENTS-Multiagente-Generico-v1.7.md` | `Em Atualização/AGENTS-Multiagente-Generico-v1.7.md` | `6B9F1E3DFDFFF5E830ACF720510A4746202D9B803216BD5A2D0DB27C57F21238` | `6B9F1E3DFDFFF5E830ACF720510A4746202D9B803216BD5A2D0DB27C57F21238` | YES | CURRENT REVIEW CANDIDATE / NOT CANONICAL |

## Gate de integridade

Para cada policy materializada:

`SOURCE_SHA256 == MIRROR_SHA256`

Resultado da execução desta distribuição: `SOURCE_TO_MIRROR_HASH_GATE = PASS` para todos os seis mirrors materializados.

Durante o discovery, as três policies atuais também foram encontradas no pacote formal de continuidade com hashes idênticos às fontes selecionadas acima. Nenhuma fonte formal, policy vigente, ZIP, manifest externo, standard ou arquivo GOV fora desta pasta foi alterado.
