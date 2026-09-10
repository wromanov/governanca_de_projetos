# GOV-08 — Matriz Integrada de Consistência entre Policies

## Escopo e identidade das fontes

`REVIEW_MODE = CONTROLLED_READ_ONLY`

Esta matriz registra a revisão integrada das duas candidatas, sem promover,
canonicalizar ou editar qualquer policy. Os documentos de evidência GOV-07 e
GOV-05 foram usados como material de rastreabilidade; a authority normativa
permanece nas policies e na autoridade especializada de independência analítica.

| Fonte | Papel | SHA256 verificado | Status observado |
|---|---|---|---|
| `Protocolos para Projetos - Vigente/.../Politica-Prompts-Agente-v1.4.md` | Prompt Policy canônica | `8006DB0B5161B6CAC1604203BA5EAC09AAE964C5E65BCA6B00C3194B387AD069` | `CANONICAL` |
| `Protocolos em Atualização/GOV-07 - Prompt Policy v1.6/Politica-Prompts-Agente-v1.6.md` | Candidata transversal consolidada | `F9EC62AF541766E95C5A52115977C8AEDE27E93DCF61037D2F18DB3A5C0FF8B5` | `PROPOSED / DRAFT` |
| `Protocolos em Atualização/GOV-05 - Skills Policy v1.1/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | Candidata especializada | `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` | `PROPOSED / DRAFT` |
| `Protocolos para Projetos - Vigente/.../Independencia-Analitica-Agente-v1.md` | Authority transversal especializada | `1692764FDCD3B0DA1171D77BCC41270E1EC3126BFD8EB263BFA9E0C0A83C8988` | vigente no conjunto fornecido |

As duas cópias localizadas da v1.4 e as duas cópias da Independência Analítica
possuem hashes idênticos entre si. O GOV-02 v1.5 existe como `PROPOSED / DRAFT`
e não é necessário como autoridade vigente para a coexistência das candidatas.

## Matriz de consistência

| REQUIREMENT | PROMPT_POLICY_v1.6 | SKILLS_PLUGINS_v1.1 | INDEPENDENCE_POLICY | CONSISTENT | CONFLICT | AUTHORITY_OWNER | NOTES |
|---|---|---|---|---|---|---|---|
| Native-first | §5: `NATIVE_EXECUTION = PREFERRED_WHEN_SUFFICIENT`; nativo suficiente resulta em `SKILL = NONE` e `PLUGIN = NONE` | §§1, 2.1, 5.2: mesma regra e fallback nativo | Compatível: independência avalia alternativas, não exige ferramenta | YES | NO | Prompt v1.6 para integração; Skills v1.1 para seleção operacional | Disponibilidade não supera suficiência nativa. |
| Skill selection | §§3, 5: skill só com alinhamento, disponibilidade confirmada/`VERIFY_AT_RUNTIME` e benefício material | §§2.2, 3, 5: workflow/procedimento; first-party only; checklist de seleção | Compatível: workflow não substitui julgamento | YES | NO | Skills v1.1 especializada | `SKILL_AVAILABLE != SKILL_REQUIRED`. |
| Plugin selection | §§3, 5: plugin aprovado só quando acrescenta capability material | §§2.3, 6: ecossistema OpenAI, governança, fit do projeto e benefício material | Compatível | YES | NO | Skills v1.1 especializada | `PLUGIN_INSTALLED != PLUGIN_REQUIRED`. |
| Availability | §§3, 5: classificar por runtime/docs/catálogo; sem confirmação, verificar | §§2.5, 2.6, 8: instalação, superfície, conexão e conhecimento são distintos | Compatível | YES | NO | Skills v1.1 especializada | `VERIFY_AT_RUNTIME` impede inferência silenciosa. |
| Invocation | §6: `NONE`, `OPTIONAL_IF_MATERIAL` e `REQUIRED` determinam invocação e espera | §§7, 7.1–7.3: aviso, chamada/seleção consciente, confirmação e pausa | Compatível | YES | NO | Skills v1.1 especializada; v1.6 integra o contrato | Seleção automática da plataforma não elimina confirmação do usuário. |
| Authority | §§2–6: agente principal mantém decisão; capability/skill/plugin não transferem authority | §§1–3, 9: `PLUGIN != AUTHORITY`, `SKILL != AUTHORITY`, `CAPABILITY != PERMISSION` | §§1, 5, 14: independência de julgamento sem autorização para agir fora do escopo | YES | NO | Usuário e authorities do projeto; policies apenas delimitam execução | Nenhum recurso substitui decisão explícita ou policy superior. |
| Write permission | §6: plugin não autoriza commit, push, merge, deploy, delete, migration, produção, mensagens, billing, banco ou secrets | §§2.4, 9, 18: conexão e capability não são write authorization; confirmação precede write | Compatível | YES | NO | Usuário/governança específica | `CAPABILITY_AVAILABILITY != WRITE_AUTHORIZATION`. |
| Multiagent independence | §§2–2.1: execução direta padrão; subagente depende de benefício material verificável; modelo, skill e plugin não implicam subagente | §20: alinhamento com Prompt Policy sem atribuir dependência causal | Independência permite discordar, não cria delegação | YES | NO | Prompt v1.6 / GOV-02 | `REVIEW_PASS != INDEPENDENT_AGENT_REVIEW`. |
| Escalation | §2.1: `SAFE_BOUNDARY → STOP → REPORT EVIDENCE → RECOMMEND ESCALATION → USER DECISION`; autoescalada proibida | §6.2 e §8: parar quando requisito real não puder ser atendido; não simular | Compatível | YES | NO | Prompt v1.6 / GOV-02 | Indisponibilidade não autoriza substituição silenciosa ou subagente simulador. |
| Analytical independence | §2 mantém decisão e validação final no principal; §7 exige relatar conflito real | Objetivo e §§2.2, 9 preservam independência analítica | §§1–14: testar hipóteses, discordar e explicitar incerteza | YES | NO | Independencia-Analitica-Agente-v1.md para julgamento | `USER_FINAL_AUTHORITY` não equivale a obrigação de concordar. |
| User authority | §§2.1, 6–7: decisão do usuário para escalada, invocação e ações externas | §§2.2, 7, 9, 20: autorização humana/confirmada permanece necessária | §14 prioriza qualidade da decisão sem remover responsabilidades e objetivos | YES | NO | Usuário; policies não promovem a si mesmas | A independência autoriza recomendar/discordar, não executar contra decisão explícita. |
| Project-specific governance | §7: authorities e escopo autorizado; parar diante de conflito ou mudança fora do escopo | §§2.2, 3, 9, 18, 20: contratos, gates, governança e project fit permanecem | Compatível | YES | NO | Governança específica do projeto, quando mais restritiva | Governança transversal não substitui regra específica. |
| Source of truth | §3 declara v1.1 como authority especializada para detalhes operacionais e mantém o contrato transversal | §20 reconhece v1.4 vigente e exige sincronização futura, sem promoção silenciosa | Independência é authority especializada de decisão analítica, não catálogo de skills/plugins | YES | NO | Cada documento em seu domínio | Duplicação de integração é limitada e semanticamente compatível; não há source of truth concorrente. |
| Header contract | §4 contém model, effort, category, skill, plugin, availability, invocation, native, multiagent, implementation e escalation | §§4.1–4.2 contém o mesmo contrato e ordem semântica | Não aplicável como schema; compatível quanto ao julgamento | YES | NO | Prompt v1.6 para contrato transversal; v1.1 para campos operacionais de skill/plugin | Identidade textual não é exigida; compatibilidade normativa é satisfeita. |
| Temporal/version model | Cabeçalho v1.6: `PROPOSED`, `DRAFT`, baseline canônica v1.4, v1.5 proposta/congelada | Cabeçalho v1.1: `PROPOSED`, `DRAFT`, sem canonicalização | Não altera versionamento | YES | NO | Prompt v1.6 para sua cadeia; v1.1 para sua cadeia | v1.5 pode permanecer não canônica; nenhuma dependência operacional exige promovê-la. |

## Findings integrados

- `BLOCKING_CONTRADICTION = 0`.
- Não foi observada inversão de authority, expansão oculta de permissão,
  semantic drift material ou dependência de source of truth concorrente.
- A repetição dos campos de cabeçalho e das regras de invocação é integração
  normativa limitada e necessária; a v1.6 remete os detalhes operacionais à
  v1.1 especializada.
- Os findings de sincronização já registrados pelo GOV-05 permanecem
  não-bloqueantes e não representam defeito de coexistência das candidatas.

## Resultado da matriz

`CROSS_POLICY_CONSISTENCY = PASS`

`DUPLICATION_FOR_INTEGRATION = LIMITED_AND_ACCEPTABLE`

`COMPETING_SOURCE_OF_TRUTH = NO`

