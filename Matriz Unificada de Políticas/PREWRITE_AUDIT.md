# Auditoria pré-escrita — GOV-01

**Data da auditoria:** 2026-09-24  
**Escopo:** `Matriz Unificada de Políticas/` e leitura de `Políticas - Consulta Rápida/Atuais/`.  
**Estado Git anterior a esta auditoria:** a pasta da matriz era não rastreada; o repositório já continha deleções e substituições não confirmadas em políticas antigas e pacotes de protocolo. Nenhuma dessas alterações foi feita por esta atividade.  
**Inventário integral da matriz:** 10 arquivos. **Inventário integral de `Atuais`:** 5 arquivos. Nenhum `AGENTS.md` aplicável foi encontrado.

## Inventário e hashes observados antes da escrita

| Caminho relativo à matriz | Bytes | SHA-256 |
|---|---:|---|
| `MATRIX_BUILD_REPORT.md` | 5833 | `872b130dd8d2835c35c24e9205d723c368be77245698665bfab7291636fa9930` |
| `POLICY_REGISTRY.json` | 5959 | `94760d69cc26f5637d00ad8d3d2a4de81e1bf83f3ccc9bf9561b2188af3aafd8` |
| `Politica-Matriz-de-Governanca-de-Projetos-v1.0.md` | 7782 | `ea5f5f13fd27f76438cc4124fb9adc01d01f58ed91175646416f141721d630ee` |
| `README.md` | 1395 | `3e4c308c1e3f995cc939d2d304d03c646abaccff6b48f71de96393eb06f1e13f` |
| `policies/AGENTS-Multiagente-Generico-v1.7-R2.2-Roteamento-Economico.md` | 59168 | `009e2506c5edae060749af31e3420348bdfeebccfe610a5d42b0f3faee6c043b` |
| `policies/Independencia-Analitica-Agente-v1.md` | 7710 | `d668de8bdaeea16403f4909678448b59705f094302bc2fe90203c2f3cc62a94e` |
| `policies/PM-01-Conducao-de-Projetos-v1.0.md` | 11364 | `fe9a0a492991925c1dbee5ef83bd54599661cdf01a68338e0c1b1e7b46d117a4` |
| `policies/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | 31564 | `3704a9da77e090980b05127c5760ee6f4b4acd5eb405074d3adea6ff4227d405` |
| `policies/Politica-Prompts-Agente-v1.7-R2.5.md` | 74194 | `237f64013030c2989847f23239c1ab6d865758fdf8a9ee86ce4193c6a9d47d74` |
| `validation/Gate-de-Internalizacao-Operacional-v2.0.md` | 14265 | `4d8894c5a29cf192ec86a27ccf2def51730ca33be4ce3495133786ccf54ee7a3` |

## Registros pré-escrita

### Matriz PM-00

```text
FILE = Politica-Matriz-de-Governanca-de-Projetos-v1.0.md
CURRENT_STATUS = PROPOSED / REVIEW_CANDIDATE; CANONICALIZATION = NO
ROLE = PM-00; arquitetura global, precedência, ownership e carregamento seletivo
ISSUE = A precedência põe toda instrução explícita atual do usuário acima das demais authorities sem explicitar que isso não derroga silenciosamente governança obrigatória; faltam a forma explícita de exceção e a regra de especialização de authority de projeto.
REQUIRED_CHANGE = Preservar autoridade final do usuário e exigir exceção EXPLICIT + SCOPED + AUTHORIZED + TRACEABLE + ALLOWED_BY_POLICY; permitir especialização de governança global sem enfraquecimento silencioso; declarar GOVERNANCE_CONTRACT_VERSION = 1.
AUTHORITY_EVIDENCE = Pedido GOV-01, seções 14 e 18; subpolicies atuais definem domains subordinados à arquitetura Matrix.
SAFE_TO_CHANGE = YES
```

### PM-01

```text
FILE = policies/PM-01-Conducao-de-Projetos-v1.0.md
CURRENT_STATUS = PROPOSED / REVIEW_CANDIDATE; CANONICALIZATION = NO
ROLE = PM-01; condução, integração incremental, continuidade, rastreabilidade e handoff
ISSUE = A hierarquia usa SPRINT como nível fixo; não define DELIVERY_UNIT; faltam fluxo frontend-first, frontend DoR/gate, raiz de continuidade, limites de localização das authorities, dataset e gate de handoff completos e gatilhos materiais pedidos.
REQUIRED_CHANGE = Adotar PROJECT → ROADMAP → PHASE → DELIVERY_UNIT → SLICE → ACTIVITY; manter integração incremental e adicionar regras frontend, continuity root, single source of truth, materialidade e AGENT_HANDOFF_GATE com todos os campos GOV-01.
AUTHORITY_EVIDENCE = Pedido GOV-01, seções 2–13; regras existentes de PM-01 já exigem integração incremental e rastreabilidade.
SAFE_TO_CHANGE = YES
```

### PM-02

```text
FILE = policies/Politica-Prompts-Agente-v1.7-R2.5.md
CURRENT_STATUS = CANONICAL / ACTIVE; CANONICALIZATION = YES
ROLE = PM-02; geração de prompts, parâmetros de modelo/esforço e recomendação de roteamento
ISSUE = Nenhum conflito estrutural encontrado para os requisitos GOV-01 de roteamento mid-task; contém proibição de autoescalonamento ROOT/multiagente e controle do usuário sobre modelo, esforço e modo.
REQUIRED_CHANGE = Nenhuma; preservar cópia idêntica à fonte canônica.
AUTHORITY_EVIDENCE = Fonte `Atuais/Politica-Prompts-Agente-v1.7-R2.5.md`; cabeçalho indica CANONICAL/ACTIVE e SHA-256 da cópia coincide com a fonte.
SAFE_TO_CHANGE = NO
```

### PM-03

```text
FILE = policies/AGENTS-Multiagente-Generico-v1.7-R2.2-Roteamento-Economico.md
CURRENT_STATUS = CANONICAL / ACTIVE; CANONICALIZATION = YES
ROLE = PM-03; execução DIRECT vs MULTIAGENT, delegação e roteamento econômico
ISSUE = Nenhum conflito estrutural encontrado nos controles mid-task exigidos; a policy atual proíbe autoescalonamento e troca automática para multiagente.
REQUIRED_CHANGE = Nenhuma; preservar cópia idêntica à fonte canônica.
AUTHORITY_EVIDENCE = Fonte `Atuais/AGENTS-Multiagente-Generico-v1.7-R2.2-Roteamento-Economico.md`; SHA-256 da cópia coincide com a fonte.
SAFE_TO_CHANGE = NO
```

### PM-04

```text
FILE = policies/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md
CURRENT_STATUS = CANONICAL / ACTIVE; CANONICALIZATION = YES
ROLE = PM-04; uso de Skills, Plugins, capacidades e permissões
ISSUE = A seção 20 declara operacionalmente que PM-02 R2.4 é vigente, embora PM-02 R2.5 seja a versão canônica atual. A cópia coincide byte a byte com a fonte canônica v1.1.
REQUIRED_CHANGE = Não editar a authority canônica. Registrar drift e preparar proposta separada PM-04 v1.2 PROPOSED / REVIEW_CANDIDATE que alinhe somente as referências operacionais para PM-02 R2.5.
AUTHORITY_EVIDENCE = Fonte `Atuais/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md`; fonte canônica PM-02 em `Atuais/Politica-Prompts-Agente-v1.7-R2.5.md`; referências operacionais encontradas nas linhas 897 e 911 da cópia v1.1.
SAFE_TO_CHANGE = NO
```

### PM-05

```text
FILE = policies/Independencia-Analitica-Agente-v1.md
CURRENT_STATUS = CANONICAL / ACTIVE; CANONICALIZATION = YES
ROLE = PM-05; independência analítica, evidência, lógica e qualidade decisória
ISSUE = Nenhum conflito com GOV-01 encontrado; cópia coincide com a fonte canônica.
REQUIRED_CHANGE = Nenhuma.
AUTHORITY_EVIDENCE = Fonte `Atuais/Independencia-Analitica-Agente-v1.md`; SHA-256 da cópia coincide com a fonte.
SAFE_TO_CHANGE = NO
```

### VP-01

```text
FILE = validation/Gate-de-Internalizacao-Operacional-v2.0.md
CURRENT_STATUS = PROPOSED / REVIEW_CANDIDATE; CANONICALIZATION = NO
ROLE = VP-01; VALIDATION_PROTOCOL; AUTHORITY_SCOPE = VALIDATION_ONLY
ISSUE = A taxonomia e os targets estão corretos; o build report tem placeholders de hash e de caminho/status canônico. A registry chama o caminho inicial Downloads de source_path sem nomear explicitamente o current governed path do pacote.
REQUIRED_CHANGE = Preservar o protocolo e seu status; registrar origem, destino governado, hashes e referência canônica v1.0 com estado factual. Manter VP-01 fora de PM-06.
AUTHORITY_EVIDENCE = Cabeçalho do protocolo v2.0; protocolo v1.0 canônico identificado no registry, com SHA-256 confirmado `62550cb36876bcf6403aa65783f1117e7335fa7d8ed4fbd1fb686baf7c4377cd`; revisão fornecida tem status PASS.
SAFE_TO_CHANGE = NO
```

### POLICY_REGISTRY.json

```text
FILE = POLICY_REGISTRY.json
CURRENT_STATUS = JSON schema_version 1.0; PM-00/PM-01 propostos; PM-02..PM-05 canônicos; VP-01 candidato
ROLE = Índice machine-readable de identidade, versão, status, lifecycle, ownership, caminhos e hashes
ISSUE = governance contract version ausente; PM-01 tem sha256/source_path nulos; ausência de current_governed_path explícito para VP-01; faltam hashes distinguíveis de origem/destino para protocolo e candidato.
REQUIRED_CHANGE = Acrescentar GOVERNANCE_CONTRACT_VERSION = 1 ou campo equivalente; registrar hashes verificados, proveniência e caminho governado sem mudar estados de promoção.
AUTHORITY_EVIDENCE = Pedido GOV-01, seções 17–20; bytes atuais e headers das authorities auditadas.
SAFE_TO_CHANGE = YES
```

### README.md e MATRIX_BUILD_REPORT.md

```text
FILE = README.md
CURRENT_STATUS = Orientação do pacote; Matrix/PM-01 e VP-01 permanecem propostas/candidatas
ROLE = Navegação e orientação de carregamento
ISSUE = Não informa a candidata de revisão PM-04 isolada; deve manter os estados não canônicos visíveis.
REQUIRED_CHANGE = Atualizar navegação para review candidate PM-04 e esclarecer que nenhuma proposta foi promovida.
AUTHORITY_EVIDENCE = Status nos headers PM-00, PM-01, PM-04 v1.1/v1.2 e VP-01.
SAFE_TO_CHANGE = YES
```

```text
FILE = MATRIX_BUILD_REPORT.md
CURRENT_STATUS = Relatório de build e proveniência; contém valores literais `$sha`, `$targetSha`, `$canonical` e `$canonicalStatus`
ROLE = Evidência de seleção, proveniência, hashes, validação e estado de revisão
ISSUE = Placeholders quebram factualidade; drift PM-04 está registrado sem uma proposta separada; não diferencia consistentemente source_path de current governed path; registry carece do contrato versionado.
REQUIRED_CHANGE = Substituir placeholders por valores observados; registrar audit trail, candidate PM-04 v1.2 e hashes/path reais; declarar os resultados finais de alinhamento e manter status factuais.
AUTHORITY_EVIDENCE = Arquivos fonte canônicos em `Atuais/`; protocolo VP-01 fonte em Downloads e v1.0 canônico localizado no pacote 2.0 de abertura; pedido GOV-01, seções 16–20.
SAFE_TO_CHANGE = YES
```

### Fontes canônicas PM-02 a PM-05 e fontes VP-01

| Arquivo fonte | Estado/papel observado | Hash SHA-256 | Issue / mudança necessária | Seguro alterar |
|---|---|---|---|---|
| `Atuais/Politica-Prompts-Agente-v1.7-R2.5.md` | CANONICAL / ACTIVE, PM-02 | `237f64013030c2989847f23239c1ab6d865758fdf8a9ee86ce4193c6a9d47d74` | Fonte atual; nenhuma mudança | NO |
| `Atuais/AGENTS-Multiagente-Generico-v1.7-R2.2-Roteamento-Economico.md` | CANONICAL / ACTIVE, PM-03 | `009e2506c5edae060749af31e3420348bdfeebccfe610a5d42b0f3faee6c043b` | Fonte atual; nenhuma mudança | NO |
| `Atuais/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.1.md` | CANONICAL / ACTIVE, PM-04 | `3704a9da77e090980b05127c5760ee6f4b4acd5eb405074d3adea6ff4227d405` | Referência operacional desatualizada; manter fonte inalterada | NO |
| `Atuais/Independencia-Analitica-Agente-v1.md` | CANONICAL / ACTIVE, PM-05 | `d668de8bdaeea16403f4909678448b59705f094302bc2fe90203c2f3cc62a94e` | Fonte atual; nenhuma mudança | NO |
| `Atuais/Prompt-Adocao-Verificacao-Politicas-Agentes-v2.0.txt` | Prompt/procedimento operacional; não é subpolicy | `a67acfb51df9813cc31c22461f7167ab1d3c17cf4f4395b713ecf96db990721b` | Excluído da seleção de policies; nenhuma mudança | NO |
| `Downloads/Gate-de-Internalizacao-Operacional-v2.0.md` | PROPOSED / REVIEW_CANDIDATE, VP-01, VALIDATION_ONLY | `4d8894c5a29cf192ec86a27ccf2def51730ca33be4ce3495133786ccf54ee7a3` | Importado byte a byte para `validation/`; preservar | NO |
| `Downloads/Gate-de-Internalizacao-Operacional-v2.0-REVISION_REPORT.md` | Evidência de revisão, STATUS PASS | `7d81266ca9b72f14fce5f1c1818ee0a7575790af4f27c56712fd644568af5a9c` | Evidência consultada; não é policy nem protocolo | NO |
| `Protocolo Inicio de Abertura de Projeto 2.0/.../gate-de-internalizacao-operacional-teste-de-validacao-do-novo-agente.md` | CANONICAL v1.0, VALIDATION_PROTOCOL / VALIDATION_ONLY | `62550cb36876bcf6403aa65783f1117e7335fa7d8ed4fbd1fb686baf7c4377cd` | Authority canônica referenciada; fora do escopo de escrita | NO |

## Gate para iniciar escrita

- Os 10 arquivos da matriz e 5 arquivos de `Atuais` foram inventariados; hashes foram calculados para cada arquivo do pacote e para as fontes consultadas.
- As cópias PM-02, PM-03, PM-04 e PM-05 conferem byte a byte com as sources canônicas atuais.
- VP-01 está corretamente classificado como protocolo de validação (VP-01, `VALIDATION_ONLY`), e a v1.0 canônica permanece distinta da candidata v2.0.
- Não foram observados bloqueios de autoridade para preparar as propostas; nenhuma policy canônica, protocolo operacional ou projeto fora da matriz está autorizado a ser alterado.
- A escrita posterior começa somente após este relatório prévio existir.

`PREWRITE_AUDIT_COMPLETE = YES`
