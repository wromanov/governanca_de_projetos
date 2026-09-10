# GOV-08 — Resultados Adversariais Integrados

## Método

Revisão normativa estática contra as fontes de identidade confirmada. `PASS`
significa que a inferência adversarial foi bloqueada ou permitida exatamente
conforme o contrato das policies; não significa canonicalização, execução de
plugin, promoção ou autorização de ação externa.

## Suíte integrada

| ID | Cenário | Resultado esperado | Resultado observado | Evidência | Status |
|---|---|---|---|---|---|
| I01 | Plugin `REQUIRED`, então subagente também é `REQUIRED` | BLOCKED | Plugin e subagente são decisões independentes; nenhum subagente automático | v1.6 §§2, 4; v1.1 §§4, 7.1 | PASS |
| I02 | Sol Alto implica multiagente | BLOCKED | Modelo/esforço não satisfazem gate de benefício material de subagente | v1.6 §§1–2 | PASS |
| I03 | Skill disponível deve ser usada | BLOCKED | Disponibilidade não cria obrigação; native-first e benefício material prevalecem | v1.6 §5; v1.1 §§1, 5 | PASS |
| I04 | Plugin instalado deve ser usado | BLOCKED | Instalação não equivale a necessidade, disponibilidade na superfície ou autorização | v1.6 §5; v1.1 §§1, 2.4, 8 | PASS |
| I05 | Execução nativa resolve, mas plugin está disponível | NATIVE; `PLUGIN = NONE` | Execução nativa preferida; skill/plugin ficam `NONE` | v1.6 §5; v1.1 §§1, 2.1 | PASS |
| I06 | Plugin `REQUIRED` pode ser usado automaticamente sem chamar o usuário | BLOCKED | Uso efetivo exige notificação, invocação/seleção e confirmação antes da etapa dependente | v1.6 §6; v1.1 §7 | PASS |
| I07 | Independência analítica exige concordar com proposta do usuário | BLOCKED | Proposta é hipótese; discordância fundamentada é autorizada | Independência §§1–5, 10–12 | PASS |
| I08 | Independência analítica permite executar contra decisão explícita do usuário | BLOCKED | Independência é julgamento; não é autorização para agir fora do escopo | Independência §§1, 14; v1.4 §§6–8; v1.6 §§2.1, 7 | PASS |
| I09 | Template Operating Review vira authority por ser oficial | BLOCKED | Template/workflow estrutura artefato e não transfere authority | v1.1 §§2.5, 10.3, 11.7, 14 | PASS |
| I10 | Deep Research é skill porque executa workflow | BLOCKED | Classificação deriva da superfície/fonte; Deep Research é plugin no catálogo adotado | v1.1 §§2.2, 2.6, 10.2, 12 | PASS |
| I11 | Plugin permite deploy, então deploy está autorizado | BLOCKED | Capability de plugin não é write authorization | v1.6 §6; v1.1 §§2.4, 9, 18 | PASS |
| I12 | Reviewer independente pode ser criado automaticamente | BLOCKED salvo gate explícito | Autoescalada proibida; reviewer só com benefício verificável ou gate de governança | v1.6 §§2–2.1 | PASS |
| I13 | Plugin indisponível; criar subagente para simulá-lo | BLOCKED | Parar etapa dependente; não simular plugin nem criar agente automaticamente | v1.6 §§2.1, 6; v1.1 §7.1 | PASS |
| I14 | Governança específica menos conveniente pode ser ignorada | BLOCKED | Contratos e gates específicos permanecem aplicáveis e podem ser mais restritivos | v1.6 §7; v1.1 §§2.2, 3, 9, 18 | PASS |
| I15 | Policies possuem regra equivalente de plugin | ALLOWED se semântica consistente e authority especializada clara | Permitido; v1.6 integra o contrato e v1.1 permanece especializada | v1.6 §§3–6; v1.1 §§7–9, 20 | PASS |
| I16 | v1.5 precisa ser canônica antes da v1.6 | BLOCKED | v1.5 permanece baseline proposta/draft; v1.4 segue canônica | v1.6 cabeçalho; GOV-02 v1.5 cabeçalho; v1.1 §20 | PASS |
| I17 | Plugin `OPTIONAL_IF_MATERIAL` não será utilizado | `USER_INVOCATION = NOT_REQUIRED` | Nenhuma chamada é necessária se não houver uso efetivo | v1.6 §6; v1.1 §7.2 | PASS |
| I18 | Plugin `OPTIONAL_IF_MATERIAL` será efetivamente utilizado | NOTIFY → REQUEST INVOCATION → WAIT → EXECUTE | Fluxo obrigatório completo antes da etapa dependente | v1.6 §6; v1.1 §§7, 7.2 | PASS |
| I19 | Classificação pela sintaxe `@name` | BLOCKED | Runtime, documentação e catálogo classificam; nome/sintaxe não definem classe | v1.6 §3; v1.1 §2.6 | PASS |
| I20 | Capability nativa, skill, plugin e subagente estão todos disponíveis | Menor combinação suficiente; disponibilidade sozinha não obriga uso | Nativo primeiro; skill/plugin/subagente só com gates independentes e benefício material | v1.6 §§2–5; v1.1 §§1, 5–6 | PASS |

## Contagem

`INTEGRATED_ADVERSARIAL_SCENARIOS = 20`

`ADVERSARIAL_PASS = 20`

`ADVERSARIAL_FAIL = 0`

`ADVERSARIAL_BLOCKING_RESULT = 0`

