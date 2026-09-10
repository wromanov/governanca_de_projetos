# Políticas em Atualização

Esta pasta contém cópias de distribuição das versões candidatas atualmente em revisão, sincronização, adjudicação ou preparação para promoção.

Estas versões:

- não substituem automaticamente a policy vigente;
- não devem ser apresentadas como canônicas;
- podem ser fornecidas deliberadamente a um agente quando o usuário quiser utilizar/testar a candidata.

Não editar policies nesta pasta. Alterações devem ocorrer na fonte formal e depois ser sincronizadas.

## Inventário

| POLICY_FAMILY | CURRENT_CANONICAL | CANDIDATE | CANDIDATE_STATUS | FORMAL_SOURCE | SHA256_SOURCE | SHA256_MIRROR | SYNC_STATUS |
|---|---|---|---|---|---|---|---|
| Prompt Policy | v1.4 | v1.6 | APPROVED CANDIDATE / PENDING CANONICALIZATION; fonte marcada PROPOSED / DRAFT | `Protocolos em Atualização/GOV-07 - Prompt Policy v1.6/Politica-Prompts-Agente-v1.6.md` | `F9EC62AF541766E95C5A52115977C8AEDE27E93DCF61037D2F18DB3A5C0FF8B5` | `F9EC62AF541766E95C5A52115977C8AEDE27E93DCF61037D2F18DB3A5C0FF8B5` | PASS |
| Skills & Plugins Policy | v1.0 | v1.1 | APPROVED CANDIDATE / NOT YET PROMOTED; fonte marcada PROPOSED / DRAFT | `Protocolos em Atualização/GOV-05 - Skills Policy v1.1/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` | `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` | PASS |
| Multiagent Policy | v1.6 formal baseline | v1.7 | CURRENT REVIEW CANDIDATE / NOT CANONICAL | `Protocolos em Atualização/GOV-03 - Politica Mult Agentes/AGENTS-Multiagente-Generico-v1.7.md` | `6B9F1E3DFDFFF5E830ACF720510A4746202D9B803216BD5A2D0DB27C57F21238` | `6B9F1E3DFDFFF5E830ACF720510A4746202D9B803216BD5A2D0DB27C57F21238` | PASS |

## Regra de promoção

ANY_POLICY_PROMOTION
OR
ANY_NEW_POLICY_CANDIDATE

MUST_BE_FOLLOWED_BY

POLICY_QUICK_REFERENCE_SYNC

A promoção continua ocorrendo na estrutura formal. A pasta de consulta rápida apenas reflete o estado posterior.

