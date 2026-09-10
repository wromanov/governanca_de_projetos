# Diff Normativo — v1.5 → v1.6

```text
SOURCE = Politica-Prompts-Agente-v1.5.md
TARGET = Politica-Prompts-Agente-v1.6.md
SOURCE_STATUS = PROPOSED / DRAFT / FROZEN
NEW_CHANGES = SKILLS_PLUGINS_SYNC_ONLY + STRICTLY_REQUIRED_INTEGRATION
MULTIAGENT_CONTENT = PRESERVED
UNAUTHORIZED_GOV_02_DRIFT = 0
```

| Área v1.6 | Classificação | Evidência de origem | Resultado |
|---|---|---|---|
| Cabeçalho/provenance | SHARED_INTEGRATION | decisão GOV-07 e baseline v1.5 | v1.6 é draft; v1.4 continua canônica |
| Seções 1 e 2 | GOV_02_MULTIAGENT | v1.5 §§1–2.4 | preservadas sem mudança normativa |
| Seções 3–6 | GOV_05_SKILLS_PLUGINS | Skills/Plugins v1.1 §§2–9 | taxonomia, fontes, cabeçalho, native-first, invocação e authority sincronizados |
| Seção 7 | SHARED_INTEGRATION | v1.5 §8 + GOV-05 §§4–9 | fluxo integra decisões independentes |

## Verificação de preservação GOV-02

Os controles v1.5 permanecem: execução direta padrão; subagente opcional
proibido; cinco gates materiais; responsabilidade do agente principal;
`REVIEW_PASS != INDEPENDENT_AGENT_REVIEW`; autoescalonamento proibido;
sequência `SAFE_BOUNDARY → STOP → REPORT EVIDENCE → RECOMMEND ESCALATION →
USER DECISION`; e resultado direto quando os gates são `NO`.

Não foi acrescentada condição de delegação, alterado threshold, nem inferida
delegação a partir de modelo, skill ou plugin.

## Mudanças novas autorizadas

1. Provenance separa autoridade v1.4 e baseline de conteúdo v1.5.
2. Taxonomia explicita capability, skill e plugin.
3. Fonte restringe skills a first-party OpenAI e plugins a ecossistema OpenAI
   com aprovação de governança; autoria OpenAI não é presumida.
4. Cabeçalho introduz campos mínimos de skill, plugin e execução nativa.
5. Native-first, benefício material, invocação humana e limite de authority de
   plugin são materializados sem catálogo duplicado.

```text
UNRELATED_NORMATIVE_CHANGES = 0
THIRD_NORMATIVE_CHANGE_DETECTED = NO
```
