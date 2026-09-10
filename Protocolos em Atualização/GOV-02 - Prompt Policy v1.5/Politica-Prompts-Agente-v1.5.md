# Política de Geração de Prompts Multiagente — v1.5

```text
STATUS = PROPOSED
LIFECYCLE = DRAFT
BASELINE = Politica-Prompts-Agente-v1.4.md
SCOPE = TRANSVERSAL
DOMAIN_SPECIFIC_CONTENT = PROHIBITED
HISTORICAL_DEPENDENCY_REQUIRED = NO
F03_MULTIAGENT_GOVERNANCE_HARDENING = INCORPORATED
V1_4_MODIFICATION = NO
CANONICALIZATION = NO
PACKAGE_PROPAGATION = NO
PROJECT_PROPAGATION = NO
USER_REVIEW_REQUIRED = YES
```

> Esta é uma proposta controlada. A v1.4 permanece preservada como autoridade
> histórica/canônica do baseline. Este documento não entra em vigor por sua
> criação e não autoriza canonicalização, atualização de pacote ou propagação.

## 0. Finalidade, escopo e versionamento

Esta política define como preparar prompts de atividade para Work ou Codex,
incluindo escolha de modelo, esforço, estratégia multiagente e
skills/capabilities especializadas. Ela é transversal e self-contained: regras
vigentes devem ser compreendidas sem arquivo histórico.

O objetivo é otimizar qualidade, custo, latência, uso de contexto, risco de
regressão e complexidade de coordenação. A existência de subagentes ou skills
disponíveis não implica que devam ser usados.

Os nomes Luna, Terra e Sol representam modelos configurados no aplicativo.
Leve, Médio, Alto e Extra Alto representam níveis de esforço/deliberação. A
disponibilidade exata deve ser confirmada no seletor atual do ambiente.

## 1. Modelo, esforço e categoria

Modelo é a capacidade-base necessária para a decisão; esforço é a deliberação
necessária para investigar, planejar, revisar e validar. São eixos
independentes.

```text
Sol    -> decisões difíceis, sistêmicas ou críticas
Terra  -> julgamento técnico e integração moderada
Luna   -> tarefas delimitadas, repetitivas e observáveis

Leve       -> decisão direta e verificações simples
Médio      -> planejamento e cruzamento de contexto
Alto       -> investigação, comparação e revisão aprofundadas
Extra Alto -> deliberação excepcional para problemas críticos ou incertos
```

Use a menor combinação de capacidade-base e deliberação suficiente:

| Categoria | Modelo | Esforço | Perfil |
|---|---|---|---|
| A | Luna | Leve | trivial e localizada |
| B | Luna | Médio | simples com algum cruzamento |
| C | Luna | Alto | clara, extensa e repetitiva |
| C+ | Terra | Leve | clara, tecnicamente exigente |
| D | Terra | Médio | desenvolvimento normal |
| E | Terra | Alto | debug, integração ou julgamento elevado |
| E+ | Terra | Extra Alto | investigação excepcional limitada |
| F | Sol | Alto | arquitetural, sistêmica ou crítica |
| F+ | Sol | Extra Alto | crítica e excepcionalmente ambígua |

Terra Leve e Terra Médio são escolhas de primeira classe. Terra Alto, Sol e
esforço Extra Alto exigem evidência de risco, ambiguidade, impacto ou
dificuldade de validação. Não escalar por ansiedade, tamanho aparente ou
preferência.

## 2. Multiagentes

Execução direta é o padrão. Quando não houver benefício material e verificável
de coordenação, declarar:

```text
EXECUTION_MODE = DIRECT
SUBAGENTS_ALLOWED = NO
```

O uso opcional ou preventivo de subagente é proibido. Não usar subagente apenas
porque a tarefa é importante, grande, crítica, porque existe uma capacidade
disponível ou porque uma revisão parece prudente.

Um subagente somente pode ser considerado quando houver benefício material e
verificável associado a pelo menos uma condição:

```text
PARALLEL_INDEPENDENT_FRONTS = YES
DISTINCT_SPECIALIZATION_REQUIRED = YES
MATERIAL_DECOMPOSITION_GAIN = YES
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION = YES
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = YES
```

Essas condições são alternativas: ao menos uma deve ser verdadeira e a
justificativa deve descrever o ganho material, o entregável delimitado, a
capacidade de consolidação e a ausência de sobreposição de escrita. Keywords,
tamanho, criticidade ou intenção genérica de “ter cobertura” não constituem
prova suficiente.

O agente principal mantém decisão, integração, inventário, autoridade sobre o
escopo e validação final. Não delegar decisões arquiteturais, contratos,
invariantes ou ampliação de escopo sem autorização explícita e fronteira de
responsabilidade documentada.

```text
TASK_IMPORTANT = YES  does not imply SUBAGENT_ALLOWED = YES
TASK_LARGE = YES      does not imply SUBAGENT_ALLOWED = YES
TASK_CRITICAL = YES   does not imply SUBAGENT_ALLOWED = YES
REVIEW_REQUIRED = YES does not imply REVIEWER_SUBAGENT_REQUIRED = YES
```

## 2.1 Taxonomia de revisão

```text
REVIEW_PASS != INDEPENDENT_AGENT_REVIEW
```

O modelo principal pode realizar, sem criar outro agente:

```text
SELF_REVIEW
CONSISTENCY_CHECK
ADVERSARIAL_PASS
FINAL_SELF_REVIEW
```

Uma revisão independente somente é admissível quando o benefício material for
demonstrável ou quando um gate de governança exigir explicitamente essa
independência. “Reviewer por segurança”, “explorer preventivo”, “worker
preventivo” e “architect preventivo” não são justificativas autônomas.

## 2.2 Autoridade de escalonamento

```text
AUTO_ESCALATION = NO
```

Se, durante a execução direta, surgir necessidade real de escalonamento, a
execução deve permanecer na fronteira segura e retornar ao usuário:

```text
SAFE_BOUNDARY
→ STOP
→ REPORT EVIDENCE
→ RECOMMEND ESCALATION
→ USER DECISION
```

Não criar novo agente automaticamente. Usar este registro conceitual:

```text
ESCALATION_REQUIRED = YES
REASON =
EVIDENCE =
WHY_CURRENT_EXECUTION_IS_INSUFFICIENT =
RECOMMENDED_MODEL =
RECOMMENDED_ROLE =
SUBAGENT_STARTED = NO
USER_AUTHORIZATION_REQUIRED = YES
```

## 2.3 Decision gate verificável

Antes de escolher execução multiagente, avaliar cada condição com evidência:

```text
PARALLEL_INDEPENDENT_FRONTS = [YES | NO]
DISTINCT_SPECIALIZATION_REQUIRED = [YES | NO]
MATERIAL_DECOMPOSITION_GAIN = [YES | NO]
IDENTIFIED_CONFLICT_REQUIRES_ADJUDICATION = [YES | NO]
GOVERNANCE_REQUIRES_INDEPENDENT_REVIEW = [YES | NO]
MATERIAL_VERIFIABLE_BENEFIT = [YES | NO]
```

Quando todas as cinco condições materiais forem `NO`, ou quando não houver
benefício verificável, o resultado obrigatório é:

```text
EXECUTION_MODE = DIRECT
SUBAGENTS_ALLOWED = NO
```

O gate representa condições materiais e não keyword matching. Uma condição
marcada `YES` sem evidência suficiente deve ser tratada como `NO`.

## 2.4 Não criar policy separada nesta versão

```text
SEPARATE_MULTIAGENT_DELEGATION_POLICY = NO
```

O concern permanece sob esta Prompt Policy:

```text
PROMPT_POLICY
├── MODEL
├── EFFORT
├── MULTIAGENT
└── SKILLS / CAPABILITIES
```

Uma extração futura somente deve ser discutida se o domínio crescer para
concerns como lifecycle de agentes, delegação aninhada, autoridade de escrita
delegada, ownership de recursos, locking entre agentes, fronteiras de
segurança delegadas, trilha de proveniência/auditoria ou protocolo de
arbitragem. Nenhuma policy adicional é criada nesta atividade.

## 3. Skills / Capabilities — bloco obrigatório

Todo prompt preparado para Work ou Codex deve conter explicitamente:

```text
🧩 SKILLS / CAPABILITIES

AMBIENTE = [Work | Codex]
🌐 SITE/UI TASK = [YES | NO]
SKILL PRINCIPAL RECOMENDADA = [skill | NONE]
SKILLS AUXILIARES RECOMENDADAS = [skills | NONE]
MOTIVO:
[...]
CATÁLOGO/AVAILABILITY CHECK = [REQUIRED | NOT_REQUIRED]
```

`NONE` é decisão explícita e correta quando não há ganho material de
especialização. O catálogo é `REQUIRED` quando a skill necessária depende de
disponibilidade não confirmada. Nunca inventar, simular ou presumir uma skill.

## 4. UI, Sites e revisão visual

As marcas de UI/Sites são complementares ao bloco geral. Para implementação ou
evolução de interface:

```text
SITE/UI TASK = YES
SKILL PRINCIPAL RECOMENDADA = Sites
```

Para atividade não-UI, declarar `SITE/UI TASK = NO`. Para revisão visual
read-only, declarar a revisão sem inferir que uma skill transfere authority.
Skills podem auxiliar composição, responsividade, hierarquia e fidelidade, mas
não decidem domínio, contrato, segurança, lifecycle ou approval.

## 5. Parcimônia e separação de responsabilidades

Use a menor combinação de skills que produza ganho material real. Não usar por
ornamentação, hábito, disponibilidade ou ausência de necessidade.

```text
MODELO / ESFORÇO = capacidade cognitiva e deliberação necessárias
MULTIAGENTE = estratégia de execução e decomposição
SKILLS / CAPABILITIES = especialização ou workflow auxiliar

SKILL != ARCHITECTURAL_AUTHORITY
SKILL != PRODUCT_AUTHORITY
SKILL != USER_AUTHORITY
CAPABILITY != AUTHORITY
CAPABILITY != PERMISSION
```

## 6. Disponibilidade e authority

O catálogo de capabilities pode variar entre Work e Codex. O prompt nomeia
somente skills realmente disponíveis ou solicita verificação. Inexistência de
skill não autoriza simular seu uso.

Skills auxiliam execução, mas a authority continua definida por documentos
canônicos, contratos, regras de domínio, segurança, usuário e agente principal
dentro de suas responsabilidades.

## 7. Estrutura obrigatória dos prompts

Todo prompt começa com este preâmbulo:

```text
RECOMENDAÇÃO DE EXECUÇÃO

Modelo principal recomendado: [...]
Esforço recomendado: [...]
Categoria: [...]
Motivo da escolha: [...]
Estratégia multiagente: [...]
Responsabilidade pela implementação: [...]
Critério de escalonamento: [...]

IDIOMA OBRIGATÓRIO:
RESPONDA SEMPRE EM PORTUGUÊS DO BRASIL (pt-BR).
```

Depois, incluir o bloco Skills/Capabilities e, quando aplicável, objetivo,
escopo, não escopo, contexto, authorities, invariantes, arquivos relevantes,
critérios de aceite, validações, regra de Git, limites de delegação,
comportamento diante de ambiguidade e formato de relatório final.

O prompt não altera o modelo por instrução textual. Commit, push, publicação
ou ação externa exigem autorização explícita. Não ampliar escopo nem ignorar
falhas.

## 8. Fluxo de execução e escalonamento

1. enquadrar objetivo, restrições, risco, categoria, modelo, esforço,
   multiagente e skills;
2. investigar authorities, arquivos, testes, disponibilidade e hipóteses;
3. consolidar evidências antes da primeira escrita relevante;
4. aplicar o decision gate multiagente e decidir o que é fechado, dependente de
   decisão ou arquitetural;
5. implementar dentro do escopo autorizado;
6. executar validações proporcionais ao risco;
7. revisar e revalidar após cada escrita material.

Escalar somente com evidência de insuficiência. Parar e relatar diante de
conflito normativo real, authority ausente, capability crítica indisponível ou
mudança fora do escopo. O escalonamento descoberto durante a execução segue a
sequência `STOP → REPORT → RECOMMEND → USER DECISION`.

## 9. Exemplos normativos

### Exemplo A — interface

```text
🧩 SKILLS / CAPABILITIES
AMBIENTE = Codex
SITE/UI TASK = YES
SKILL PRINCIPAL RECOMENDADA = Sites
SKILLS AUXILIARES RECOMENDADAS = NONE
MOTIVO: alteração de composição e responsividade.
CATÁLOGO/AVAILABILITY CHECK = REQUIRED
```

### Exemplo B — implementação direta

```text
🧩 SKILLS / CAPABILITIES
AMBIENTE = Codex
SITE/UI TASK = NO
SKILL PRINCIPAL RECOMENDADA = NONE
SKILLS AUXILIARES RECOMENDADAS = NONE
MOTIVO: implementação localizada sem ganho material de especialização.
CATÁLOGO/AVAILABILITY CHECK = NOT_REQUIRED
EXECUTION_MODE = DIRECT
SUBAGENTS_ALLOWED = NO
```

## 10. Relatório final

O relatório informa arquivos alterados, resumo, testes e validações, achados,
correções, pendências, riscos, confirmação de ausência de mudanças fora do
escopo, modelo/esforço, estratégia multiagente, resultado do decision gate e
decisão de skills.

## 11. Princípios finais

1. Modelo é capacidade-base; esforço é deliberação.
2. Execução direta é o padrão; multiagente exige benefício material verificável.
3. Multiagente é coordenação, não authority.
4. Review pass não equivale a independent-agent review.
5. Escalonamento automático é proibido; a decisão retorna ao usuário.
6. Skills são especialização opcional, não decoração nem authority.
7. Todo prompt Work/Codex declara Skills/Capabilities e idioma.
8. `NONE` é uma decisão válida quando aplicável.
9. Disponibilidade deve ser verificada sem inventar capabilities.
10. Use a menor configuração suficiente.
11. Escalone por evidência e pare diante de conflito ou mudança não autorizada.

```text
PROPOSED_POLICY_REVIEW = REQUIRED
POLICY_EFFECTIVE = NO
CANONICALIZATION_AUTHORIZED = NO
PROPAGATION_AUTHORIZED = NO
```
