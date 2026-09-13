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
| Prompt Policy | v1.4 | v1.7-R1 | CURRENT TEST CANDIDATE / NOT CANONICAL; v1.7 superseded draft preserved in formal source | `Protocolos em Atualização/GOV-02 - Prompt Policy v1.7/Politica-Prompts-Agente-v1.7-R1.md` | `42A747D415C152C5627B75348F0666FB2688D70A4BC15EF1DC2C3A294FBEE051` | `42A747D415C152C5627B75348F0666FB2688D70A4BC15EF1DC2C3A294FBEE051` | PASS |
| Skills & Plugins Policy | v1.0 | v1.1 | APPROVED CANDIDATE / NOT YET PROMOTED; fonte marcada PROPOSED / DRAFT | `Protocolos em Atualização/GOV-05 - Skills Policy v1.1/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | `9CD554E1279E2AFE229316F31F768FF80E70EA3566C1DF4971F1BBDA5C4D03A0` | `9CD554E1279E2AFE229316F31F768FF80E70EA3566C1DF4971F1BBDA5C4D03A0` | PASS |
| Multiagent Policy | v1.6 formal baseline | v1.7 | CURRENT REVIEW CANDIDATE / NOT CANONICAL | `Protocolos em Atualização/GOV-03 - Politica Mult Agentes/AGENTS-Multiagente-Generico-v1.7.md` | `CF4E35F9D99B4752C6C83AF89A8FCA15F67E15E22F7ECEEAC7E5490629A2A2F7` | `CF4E35F9D99B4752C6C83AF89A8FCA15F67E15E22F7ECEEAC7E5490629A2A2F7` | PASS |

## Regra de promoção

ANY_POLICY_PROMOTION
OR
ANY_NEW_POLICY_CANDIDATE

MUST_BE_FOLLOWED_BY

POLICY_QUICK_REFERENCE_SYNC

A promoção continua ocorrendo na estrutura formal. A pasta de consulta rápida apenas reflete o estado posterior.

