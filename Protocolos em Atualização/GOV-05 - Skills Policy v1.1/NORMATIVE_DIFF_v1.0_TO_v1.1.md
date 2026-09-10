# GOV-05 — Diff Normativo Integral v1.0 → v1.1

## Escopo e identidade das fontes

| Fonte | Papel | SHA256 |
|---|---|---|
| `Politica-de-Uso-de-Skills-Codex-Work-v1.0.md` | baseline vigente | `C0D657C673B93719F250DCB52F2DA5853E1C33ECA202D769570A8EF742D5D695` |
| `Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | candidata sob revisão | `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2` |

Revisão executada contra a v1.1 de hash validado. A cópia vigente localizada da v1.0 possui o mesmo hash do baseline usado nesta comparação.

## ADDED

1. Taxonomia explícita e separada para capacidade nativa, skill, plugin, app/integração e template/workflow.
2. Regra de classificação por runtime/metadata, documentação oficial e catálogo operacional, com `VERIFY_AT_RUNTIME` quando a prova não existir.
3. Política de proveniência: skills somente first-party OpenAI; plugins do ecossistema OpenAI somente com aprovação de governança e aderência ao projeto; autoria OpenAI não é presumida.
4. Cabeçalho decisório único com modelo, esforço, categoria, skill, plugin, disponibilidade, propósito, suficiência nativa e estratégia multiagente.
5. Disposições formais `NONE`, `OPTIONAL_IF_MATERIAL` e `REQUIRED` para plugins.
6. Protocolo obrigatório de aviso, invocação consciente pelo usuário, confirmação e pausa antes de etapa dependente de plugin efetivamente usado.
7. Proibições expressas de uso silencioso, substituição silenciosa de plugin REQUIRED e presunção de disponibilidade/invocação.
8. Controles explícitos para apps, permissões, side effects e autoridade de escrita.
9. Registro obrigatório no relatório final sobre seleção, uso real e confirmação de invocação de plugin.
10. Sincronização declarada, porém não autorizada, com as Prompt Policies v1.4 e v1.5.

## CHANGED

1. O escopo evolui de política de skills para política integrada de capacidades nativas, skills e plugins, sem alterar a prioridade da capacidade nativa quando suficiente.
2. A escolha deixa de depender de uma enumeração textual presumida de nomes e passa a exigir classificação verificada na superfície atual.
3. A disponibilidade deixa de ser um detalhe operacional de skills e passa a ser gate explícito, distinto de instalação, conexão de app e autorização de escrita.
4. A autonomia de seleção é preservada, mas limitada por provenance, disponibilidade, governança e confirmação do usuário quando houver uso efetivo de plugin.
5. A matriz e os fluxos de decisão passam a distinguir o container plugin do workflow/template e da capacidade nativa.
6. A manutenção passa a tratar o snapshot operacional como não normativo e incapaz de substituir a verificação atual.

## RECLASSIFIED

| Item v1.0 | Classificação v1.1 | Base da reclassificação |
|---|---|---|
| Deep Research | Plugin | Catálogo adotado e seção 10.2 da v1.1; não é skill isolada. |
| Plugin Management | Plugin | Catálogo adotado e seção 10.8 da v1.1; sua função é descoberta/disponibilidade de plugins. |
| Default templates | Plugin container | Catálogo adotado e seção 10.3 da v1.1; contém templates/workflows. |
| Operating Review | Template/workflow, não plugin | Seções 2.5 e 11.7 da v1.1. |
| `@document`, `@spreadsheet`, `@presentation`, `@pdf` | Não presumidos como skills por sintaxe | Regra geral de classificação por superfície da seção 2.6. |
| ChatGPT Sites / `@Sites` | Capacidade nativa de produto quando confirmada | Catálogo adotado e seção 2.6 da v1.1; não inferir do `@`. |
| Codex | Capacidade nativa / ambiente de engenharia | Taxonomia de capacidade nativa e catálogo adotado. |
| Work | Superfície de produto / ambiente nativo de trabalho | Taxonomia e catálogo adotado. |

## REMOVED

1. Catálogo normativo extenso de nomes tratados como skills por padrão, inclusive famílias sem confirmação de disponibilidade atual.
2. Recomendação para criação de novas skills e modelo para skills personalizadas.
3. Permissão operacional para tratar diretamente os nomes de templates, artefatos ou produtos como skills com base no nome.
4. Prioridades/Tiers normativos baseados em inventário de nomes não verificado no runtime.

As remoções são materiais e intencionais: eliminam classificação não comprovada e criação local/customizada incompatíveis com a política de fonte da v1.1.

## PRESERVED

| Princípio do baseline | Estado na v1.1 |
|---|---|
| Minimum sufficient capability | PRESERVED |
| Native first | PRESERVED |
| No skill by availability only | PRESERVED |
| No plugin by installation only | PRESERVED |
| Authority not transferred | PRESERVED |
| Capability is not permission | PRESERVED |
| No silent decision replacement | PRESERVED, reforçado para plugins REQUIRED |
| Runtime availability matters | PRESERVED, explicitado como gate |
| No tool sprawl | PRESERVED |
| Critical gates preserved | PRESERVED |
| Proporcionalidade, rastreabilidade e não duplicação de source of truth | PRESERVED |
| Decisão baseada em evidência, não em template | PRESERVED |

## UNRELATED_NORMATIVE_CHANGES

`0`

Cada alteração material identificada responde à correção de modelo de fonte/classificação, à separação capability-skill-plugin, à governança de invocação e à preservação de authority. Não foi encontrada alteração normativa material sem relação com esses objetivos.

## CONCLUSION

`INTEGRAL_SOURCE_COMPARISON = PASS`

A v1.1 é uma evolução controlada da v1.0: preserva os princípios operacionais centrais e corrige as classificações e controles que a baseline não distinguia. A proposta ainda não é vigente; canonicalização e promoção continuam fora de escopo.
