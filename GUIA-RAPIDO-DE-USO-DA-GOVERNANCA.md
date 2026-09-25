# Guia rápido de uso da governança

~~~text
DOCUMENT_TYPE = OPERATIONAL_USER_GUIDE
NORMATIVE_AUTHORITY = NO
SOURCE_OF_TRUTH = CANONICAL GOVERNANCE DOCUMENTS
GUIDE_STATUS = NON_NORMATIVE
~~~

Este guia ajuda a entregar o contexto certo ao agente. Ele não cria policies, gates, protocolos ou authorities. Em caso de dúvida, consulte os documentos canônicos e o POLICY_REGISTRY.json.

## O que entregar ao agente?

| Situação | Entregar ou deixar acessível | Protocolo inicial | Resultado esperado |
|---|---|---|---|
| Projeto novo | Matriz e Registry; PM-01 e policies aplicáveis; contexto e objetivo do projeto; pacotes Opening 3.0 e Continuity 3.0. | Opening 3.0 | Fundação revisada, artefatos de continuidade aplicáveis e handoff preparado. |
| Projeto em andamento, novo agente ou chat | Instruções do projeto e pasta docs/continuity/ — ou equivalente governado — incluindo binding, estado, mapa de authorities e registros atuais. Disponibilize também a governança global e o pacote Continuity 3.0. | Continuity 3.0, no modo apropriado | Estado conferido em modo de recuperação, contradições reportadas e SAFE_RESUME_POINT baseado em evidência. |
| Internalização de policies | Matriz e Registry, PM-01, somente as policies aplicáveis e o protocolo operacional da atividade. | O protocolo da atividade; VP-01 quando requerido | Evidência de que o agente identificou as authorities certas e sabe aplicar seus efeitos à tarefa. |

## 1. Abertura de projeto novo

### O que disponibilizar

- **Governança global:** Matriz Unificada de Políticas/Politica-Matriz-de-Governanca-de-Projetos-v1.0.md e POLICY_REGISTRY.json.
- **Condução do projeto:** PM-01 v1.0, sempre que a atividade envolver abertura, planejamento, execução ou continuidade.
- **Policies aplicáveis:** resolva as versões e o status pelo Registry. Por exemplo, PM-02 e PM-03 para prompts ou roteamento multiagente; PM-04 quando skills/plugins forem pertinentes; PM-05 em decisões técnicas materiais. Não é necessário despejar todas as policies em toda conversa.
- **Abertura:** Protocolo Inicio de Abertura de Projeto 3.0/START_HERE.md, OPENING_PROTOCOL.md e OPENING_WIZARD.md.
- **Continuidade:** deixe disponível Protocolo Continuidade Projeto Em Andamento Com Novo Agente 3.0/, em especial CONTINUITY_PROTOCOL.md e schemas/PROJECT_GOVERNANCE_BINDING.schema.json. Opening reutiliza esse schema para o binding.
- **Contexto do projeto:** objetivo, restrições conhecidas, materiais existentes e instruções do repositório, se houver.
- **Validação:** VP-01 v2.0 quando exigido pela authority de validação ou pelo protocolo aplicável.

Se o agente já tiver acesso ao diretório de governança e ao projeto, informe os caminhos e peça que ele localize as authorities. Se não tiver, anexe esses arquivos ou disponibilize os diretórios. Peça para confirmar identidade, versão, status e aplicabilidade antes de usá-los.

### O que o agente deve fazer

Peça que o agente internalize as policies aplicáveis **antes de tomar decisões de abertura**, seguindo a seção 3 deste guia. Depois, deve operar o Opening 3.0 pela sequência de descoberta, requisitos, governança, arquitetura, fundação de engenharia, roadmap, plano de entrega, documentação, estado, revisão e gate. A sequência se adapta ao projeto; nem todo artefato ou sprint se aplica.

O Opening pode criar ou organizar, conforme necessário:

- **PROJECT_GOVERNANCE_BINDING.json**, validado com o schema do Continuity 3.0 e contendo as authorities adotadas pelo projeto;
- **PROJECT_STATE**, o registro factual atual do projeto;
- **ACTIVE_AUTHORITY_MAP** e **CONTINUITY_RECORD**;
- **NEW_AGENT_BOOTSTRAP** e uma página **START_HERE** que indique onde os registros vivem;
- **ROADMAP** e **EXECUTION_PLAN** ou registros de sprint, quando aplicáveis;
- registros de abertura, revisão da fundação e **PROJECT_OPENING_GATE_RECORD**;
- **SAFE_RESUME_POINT** com base em evidência, mantendo prontidão e autorização em campos separados.

O Opening deve materializar apenas o que se aplica e manter fatos e decisões do projeto nos registros do próprio projeto. O binding registra os pins adotados com id, versão e hash; ele não é uma cópia da governança global.

Ao final, o Opening Gate registra se a fundação foi aprovada pelo usuário, se os artefatos necessários estão localizáveis e se o handoff está pronto. O handoff segue os requisitos de PM-01 e entrega a recuperação operacional ao Continuity 3.0, que verifica o binding, os registros e estabelece o ponto seguro de retomada.

**Opening Gate PASS não autoriza implementação, publicação Git, deploy ou avanço.** A próxima atividade e sua autorização são decisões separadas, conforme PM-01 e as authorities aplicáveis.

## 2. Projeto em andamento, novo agente ou novo chat

### O que entregar primeiro

Disponibilize o repositório ou a pasta do projeto e, no início, estes itens:

1. **AGENTS.md** do projeto e o **START_HERE** da continuidade, se existirem. Eles indicam a raiz governada e onde buscar os registros.
2. A pasta **docs/continuity/** ou o equivalente declarado pelo projeto.
3. **PROJECT_GOVERNANCE_BINDING.json** e o schema do Continuity 3.0 para verificar sua estrutura.
4. **PROJECT_STATE**, **ACTIVE_AUTHORITY_MAP** e **CONTINUITY_RECORD**.
5. **ROADMAP** e **EXECUTION_PLAN**/sprints, quando relevantes para a retomada.
6. **NEW_AGENT_BOOTSTRAP** e **LAST_HANDOFF**, quando existirem ou forem aplicáveis.
7. As authorities específicas do projeto referenciadas pelo mapa, além dos documentos necessários à próxima atividade.

Entregue os registros atuais e seus links para as authorities. Não é preciso anexar todo o histórico se os registros atuais apontarem para as decisões e evidências importantes. Se não houver acesso ao repositório, anexe esses documentos ou forneça os caminhos exatos.

Disponibilize também a Matriz e o Registry globais, PM-01, as policies aplicáveis e o pacote **Continuity 3.0**. O agente deve resolver separadamente os pins do projeto e a governança global atual.

### Como deve começar a recuperação

Para um novo agente/chat, o modo usual é **FIRST_ADOPTION_OR_AGENT_CHANGE**. O agente deve:

- localizar o binding pelo caminho declarado pelo projeto e conferir sua estrutura com o schema;
- resolver cada authority adotada pelo id, versão e hash registrados;
- inspecionar os documentos do projeto por função semântica e verificar fatos disponíveis, usando Git somente para leitura quando estiver disponível;
- aplicar VP-01 quando o modo ou as authorities aplicáveis exigirem validação;
- relatar lacunas, divergências, hashes incompatíveis e fatos não verificados, sem adivinhar ou reconciliar silenciosamente;
- definir o **SAFE_RESUME_POINT** a partir do estado comprovado e indicar separadamente a próxima atividade e a autorização necessária.

A recuperação inicial é de leitura e conferência: não deve editar o estado do projeto. Se não houver binding ou existir uma situação legada, peça que o agente relate o bloqueio e a rota autorizada necessária. Não faça retrofit, troca de pins ou migração silenciosa para uma baseline/protocolo mais novo.

**Continuity Recovery Gate PASS não autoriza implementação, ações Git de publicação ou avanço.** O agente apresenta o estado recuperado e aguarda qualquer validação de continuidade requerida; a execução depende da autorização apropriada para a atividade.

## 3. Internalização das policies

“Internalizar” significa ler e compreender as authorities aplicáveis, resolver precedência e ownership e operar segundo elas durante a atividade. Não significa que o agente as guardará como memória permanente para outros chats.

Use esta ordem prática:

1. **Matriz e Registry:** identifique a arquitetura, a precedência e a versão/status de cada authority.
2. **PM-01 e policies aplicáveis:** carregue PM-01 para condução/continuidade; selecione outras policies pelo escopo da tarefa. A Matriz é sempre carregada e exige carregamento seletivo.
3. **Protocolo operacional:** leia o protocolo que executa o processo — Opening 3.0 para abertura ou Continuity 3.0 para recuperação.
4. **VP-01:** aplique o Gate de Internalização Operacional v2.0 quando a validação for exigida pelo modo, pela authority ou pelo protocolo aplicável. VP-01 tem escopo VALIDATION_ONLY; use seu procedimento canônico sem copiar sua suíte para este guia.
5. **Authorities do projeto:** consulte binding e mapa para resolver os pins adotados, fatos, contratos e decisões locais que regem aquele projeto.

No início da atividade, o agente pode demonstrar internalização com evidência breve e verificável: quais arquivos leu; id, versão, status, owner e escopo identificados; quais policies são aplicáveis e por quê; e quais efeitos isso tem na tarefa e nos limites de autorização. Uma declaração “li e entendi”, sozinha, não é evidência de validação.

Carregue só as policies que a atividade exige. Por exemplo, roteamento multiagente pede PM-02 e PM-03; decisão de skills/plugins pede PM-04; decisão técnica material pede PM-05 e a policy de domínio relevante; execução ou continuidade pede PM-01 e as policies aplicáveis. O Registry é a referência para confirmar os nomes e versões atuais.

A governança global e o binding do projeto têm funções diferentes. A governança global informa as authorities atuais disponíveis; o binding registra o conjunto efetivamente adotado pelo projeto, com seus pins. Um status global mais novo não altera esses pins por conta própria. A adoção ou migração do projeto precisa seguir um caminho explícito e autorizado.

## Fluxo de bolso

- **Novo projeto:** governança global → Opening 3.0 → artefatos do projeto → handoff → Continuity 3.0.
- **Projeto existente:** docs/continuity + binding → Continuity 3.0 → recuperação → SAFE_RESUME_POINT → execução somente quando autorizada.

## Prompts reutilizáveis

### A) Iniciar um projeto novo

~~~text
Vamos abrir o projeto [nome/objetivo]. Localize a Matriz e o POLICY_REGISTRY.json canônicos; resolva PM-01 e somente as policies aplicáveis, conferindo id, versão e status. Leia o Opening 3.0 e use o schema de binding do Continuity 3.0. Antes das decisões de abertura, demonstre por evidência a internalização das policies aplicáveis e use VP-01 v2.0 quando requerido. Execute a abertura e materialize apenas os artefatos de projeto que se aplicarem, com revisão e aprovação explícitas da fundação. Prepare o handoff ao Continuity 3.0. Não comece implementação do produto sem o gate aplicável e autorização explícita; Opening Gate PASS, por si só, não autoriza implementação.
~~~

### B) Entregar um projeto em andamento a um novo agente

~~~text
Recupere o projeto [nome] como novo agente/chat. Comece por AGENTS.md, START_HERE e docs/continuity/ (ou raiz governada equivalente); examine binding, PROJECT_STATE, ACTIVE_AUTHORITY_MAP, CONTINUITY_RECORD, ROADMAP e plano/sprints aplicáveis, NEW_AGENT_BOOTSTRAP e LAST_HANDOFF quando existirem. Use Continuity 3.0 no modo FIRST_ADOPTION_OR_AGENT_CHANGE; verifique pins por id, versão e hash e consulte separadamente a Matriz/Registry atuais. Faça a recuperação inicial somente leitura, aplique VP-01 v2.0 quando requerido, relate lacunas e conflitos e estabeleça SAFE_RESUME_POINT com evidência. Não migre pins silenciosamente nem implemente ou publique Git antes do gate e da autorização específica.
~~~

## Authorities de referência

Os status abaixo foram conferidos nos artefatos atuais em 25/09/2026:

- Governance Baseline V1 e Matrix: **Matriz Unificada de Políticas/Politica-Matriz-de-Governanca-de-Projetos-v1.0.md** — **CANONICAL / ACTIVE**.
- Registry: **Matriz Unificada de Políticas/POLICY_REGISTRY.json**.
- PM-01: **Matriz Unificada de Políticas/policies/PM-01-Conducao-de-Projetos-v1.0.md** — **CANONICAL / ACTIVE**.
- VP-01 v2.0: **Matriz Unificada de Políticas/validation/Gate-de-Internalizacao-Operacional-v2.0.md** — **CANONICAL / ACTIVE**, **VALIDATION_ONLY**.
- Opening 3.0: **Protocolos para Projetos - Vigente/Protocolo Inicio de Abertura de Projeto 3.0/** — **CANONICAL / ACTIVE**.
- Continuity 3.0: **Protocolos para Projetos - Vigente/Protocolo Continuidade Projeto Em Andamento Com Novo Agente 3.0/** — **CANONICAL / ACTIVE**.

Use sempre o Registry atual para confirmar as versões operacionais e as policies aplicáveis.
