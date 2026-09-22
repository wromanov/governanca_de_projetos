STATUS = HISTORICAL_SUPERSEDED
SUPERSEDED_BY = CANONICAL_POLICY_PACKAGE

# Política de Geração de Prompts Multiagente — v1.4

STATUS = CANONICAL
SCOPE = TRANSVERSAL
DOMAIN_SPECIFIC_CONTENT = PROHIBITED
HISTORICAL_DEPENDENCY_REQUIRED = NO
READY_FOR_CONTINUITY_AUTHORITY_REREAUDIT = YES
USER_FINAL_APPROVAL_FOR_REVISED_CONTINUITY_AUTHORITIES = PENDING

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

Execução direta é o padrão quando há uma única frente, contexto pequeno,
entregável acoplado ou ausência de benefício verificável de coordenação. Quando
não houver benefício, declarar:

```text
Execução direta; não utilizar subagentes.
```

Use subagentes somente com frentes independentes ou especialização clara,
entregáveis delimitados, benefício real de paralelismo, cobertura ou revisão,
capacidade de consolidação pelo agente principal e ausência de sobreposição de
escrita. O agente principal mantém decisão, integração, inventário e validação
final.

Papéis preferenciais incluem descoberta read-only, análise de testes,
trabalho fechado derivado, revisão técnica, segurança e arquitetura sistêmica.
Não delegar decisões arquiteturais, contratos, invariantes ou ampliação de
escopo.

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
4. decidir o que é fechado, dependente de decisão ou arquitetural;
5. implementar dentro do escopo autorizado;
6. executar validações proporcionais ao risco;
7. revisar e revalidar após cada escrita material.

Escalar somente com evidência de insuficiência. Parar e relatar diante de
conflito normativo real, authority ausente, capability crítica indisponível ou
mudança fora do escopo.

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
```

## 10. Relatório final

O relatório informa arquivos alterados, resumo, testes e validações, achados,
correções, pendências, riscos, confirmação de ausência de mudanças fora do
escopo, modelo/esforço, estratégia multiagente e decisão de skills.

## 11. Princípios finais

1. Modelo é capacidade-base; esforço é deliberação.
2. Multiagente é coordenação, não authority.
3. Skills são especialização opcional, não decoração nem authority.
4. Todo prompt Work/Codex declara Skills/Capabilities e idioma.
5. `NONE` é uma decisão válida quando aplicável.
6. Disponibilidade deve ser verificada sem inventar capabilities.
7. Use a menor configuração suficiente.
8. Escalone por evidência e pare diante de conflito ou mudança não autorizada.

