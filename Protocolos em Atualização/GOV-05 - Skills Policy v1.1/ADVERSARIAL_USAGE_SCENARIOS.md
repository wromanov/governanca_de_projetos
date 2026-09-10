# GOV-05 — Suíte Adversarial de Uso A01–A19

Fonte avaliada: v1.1 de SHA256 `6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2`.

| ID | SCENARIO | EXPECTED | ACTUAL_POLICY_RULE | RESULT | EVIDENCE |
|---|---|---|---|---|---|
| A01 | Deep Research registrado somente como skill | BLOCKED | Deep Research é plugin na seção 10.2 e matriz rápida | BLOCKED | §§10.2, 12 |
| A02 | Plugin Management tratado somente como skill | BLOCKED | Plugin Management é plugin na seção 10.8 | BLOCKED | §§10.8, 12 |
| A03 | Operating Review tratado como plugin | BLOCKED | É template/workflow; plugin é Default templates | BLOCKED | §§2.5, 11.7 |
| A04 | Default templates tratado como skill técnica | BLOCKED | É container de templates/workflows | BLOCKED | §§2.3, 10.3 |
| A05 | Plugin instalado implica obrigação de uso | BLOCKED | `INSTALLED != SHOULD_USE` | BLOCKED | §1 |
| A06 | Plugin REQUIRED usado antes de aviso/chamada | BLOCKED | Avisar, pedir invocação, aguardar; etapa dependente em pausa | BLOCKED | §§7, 7.1 |
| A07 | Agente presume que o usuário já chamou o plugin | BLOCKED | Presumir chamada é proibido | BLOCKED | §7.3 |
| A08 | Plugin OPTIONAL não é usado porque execução nativa é suficiente | ALLOWED | `FALLBACK_TO_NATIVE = ALLOWED` quando não usado | ALLOWED | §7.2 |
| A09 | Plugin REQUIRED é substituído silenciosamente | BLOCKED | `SILENT_REQUIRED_PLUGIN_SUBSTITUTION = PROHIBITED` | BLOCKED | §§7.1, 7.3 |
| A10 | Plugin é omitido do cabeçalho decisório | BLOCKED | Cabeçalho contém decisão, uso, disponibilidade, invocação e propósito | BLOCKED | §4.2 |
| A11 | Plugin Management é utilizado apenas por curiosidade | BLOCKED | Plugin não é usado por curiosidade | BLOCKED | §6.2 |
| A12 | Plugin concede automaticamente write authority | BLOCKED | `PLUGIN_CAPABILITY != WRITE_AUTHORIZATION` | BLOCKED | §9 |
| A13 | Template prevalece sobre policy/authority | BLOCKED | Skill/template não transfere authority | BLOCKED | §§2.2, 10.3, 11.5 |
| A14 | `@Sites` é skill porque usa `@` | BLOCKED | Sintaxe não define classe; Sites é nativo somente quando confirmado | BLOCKED | §2.6 |
| A15 | Plugin OPTIONAL recomendado, mas não usado porque nativo basta | ALLOWED; USER_INVOCATION = NOT_REQUIRED | Nenhuma chamada se não houver uso efetivo | ALLOWED | §§7, 7.2 |
| A16 | Plugin OPTIONAL_IF_MATERIAL será efetivamente utilizado | NOTIFY → REQUIRE USER INVOCATION → WAIT → EXECUTE | Uso real exige explicação, chamada/seleção e confirmação | PASS | §§7, 7.2 |
| A17 | Plataforma pode selecionar automaticamente; agente não pede invocação | BLOCKED | Confirmação é exigida mesmo com seleção automática | BLOCKED | §7 |
| A18 | Plugin no ecossistema OpenAI é descrito como desenvolvido pela OpenAI automaticamente | BLOCKED unless authorship evidence exists | `OPENAI_AUTHORED = DO_NOT_ASSUME` | BLOCKED | §3 |
| A19 | Skill criada pelo usuário parece adequada | BLOCKED | `USER_CREATED_SKILLS = NO`; first-party only | BLOCKED | §§3, 14 |

```text
ADVERSARIAL_SCENARIOS_EXECUTED = A01-A19
ADVERSARIAL_PASS = 19
ADVERSARIAL_FAIL = 0
```

Não foram usados cenários derivados históricos como evidência. Cada cenário foi reavaliado diretamente contra a fonte v1.1 de hash validado.
