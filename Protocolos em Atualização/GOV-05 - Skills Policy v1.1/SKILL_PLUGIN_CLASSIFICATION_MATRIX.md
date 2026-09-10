# GOV-05 — Matriz de Classificação Skill / Plugin / Capability

Base: v1.1 com SHA256 `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2`, catálogo operacional com SHA256 `7F6B23E943C92CC96F72DBE990368038B0B274FDC1A37181C4A1A9DE7AA0C5D6` e Prompt Policy v1.4 vigente.

| ITEM | CLASSIFICATION | SOURCE_OR_CONTAINER | ROLE | AVAILABILITY_RULE | INVOCATION_RULE | AUTHORITY_IMPACT | V1_1_CONFORMANCE |
|---|---|---|---|---|---|---|---|
| Capacidade nativa | Native capability | Codex/Work surface | Executa trabalho diretamente | Confirmar a superfície quando necessário | Nenhuma invocação de plugin | Não transfere authority nem permission | PASS |
| Codex | Native capability / product surface | Superfície Codex | Engenharia, repositório, código e execução | Runtime atual | Não é plugin | Não transfere authority | PASS |
| Work | Product surface / native work environment | Superfície Work | Trabalho estruturado e artefatos | Runtime atual | Não é plugin | Não transfere authority | PASS |
| Skill oficial OpenAI | Skill/workflow | First-party OpenAI | Método, procedimento e orientação | Confirmar runtime; senão `VERIFY_AT_RUNTIME` | Não requer invocação de plugin se independente | Não transfere authority | PASS |
| Deep Research | Plugin | Ecossistema OpenAI; catálogo | Pesquisa multi-pass com evidência e citações | Verificar disponibilidade/superfície | Se uso efetivo: avisar, pedir invocação, aguardar confirmação | Capability não é write authorization | PASS |
| Plugin Management | Plugin | Ecossistema OpenAI; catálogo | Descoberta, disponibilidade, permissões e dependências | Usar para verificar alegação de indisponibilidade quando disponível | Uso efetivo segue aviso/invocação/confirmação | Não concede authority | PASS |
| Default templates | Plugin container | Ecossistema OpenAI; catálogo | Disponibiliza templates/workflows de artefato | Confirmar container e template no runtime | Uso efetivo segue aviso/invocação/confirmação | Template não é authority | PASS |
| Operating Review | Template/workflow | Pode ser fornecido por Default templates | Estrutura artefato de revisão operacional | Não presumir disponibilidade pelo nome | Não é plugin; se o container for usado, aplicar regra do plugin | Não substitui auditoria técnica, policy ou gate | PASS |
| System Design / Strategy Memorandum / Experiment Analysis | Skills/workflows condicionais | Superfície atual ou Default templates | Estrutura especializada | `VERIFY_AT_RUNTIME` sem prova atual | Regra de plugin somente se fornecido/efetivamente usado via container | Não transfere authority | PASS |
| ChatGPT Sites / `@Sites` | Native product capability quando confirmado | Superfície/documentação/catálogo | Sites, dashboards e apps leves | Não inferir pelo nome/sintaxe; confirmar superfície | Não é plugin automaticamente | Não autoriza publicação, dados ou deploy | PASS |
| `@name`, `$name`, `/name` | Sintaxe, não classe | N/A | Nenhum papel próprio | Classificar por runtime/docs/catálogo | Depende da classe provada | Nenhum | PASS |
| Plugin do ecossistema OpenAI | Plugin, autoria indeterminada | Ecossistema OpenAI | Capability adicional | Requer disponibilidade, aprovação e fit do projeto | Uso real exige notificação e confirmação do usuário | Não equivale a autoria OpenAI ou authority | PASS |
| Skill custom/local/criada pelo usuário | Proibida | Fora da policy de fonte | Nenhum uso autorizado nesta fase | Não selecionar | Não aplicável | Não cria exceção de authority | PASS |

## Regras transversais verificadas

```text
CAPABILITY != SKILL
SKILL != PLUGIN
PLUGIN_MAY_CONTAIN_SKILLS = YES
SKILL_MAY_EXIST_WITHOUT_PLUGIN = YES
NAME_SYNTAX_DOES_NOT_DEFINE_CLASS = YES
PLUGIN_CAPABILITY != WRITE_AUTHORIZATION
```

Classificação em dúvida: `CLASSIFICATION = VERIFY_AT_RUNTIME`; nunca inferir apenas pelo nome, `@`, `$`, `/`, marca de produto, template ou nome de plugin.
