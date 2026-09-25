# Política Matriz de Governança de Projetos v1.0

```text
POLICY_ID = PM-00
VERSION = 1.0
STATUS = CANONICAL
LIFECYCLE = ACTIVE
CANONICALIZATION = YES
USER_REVIEW_REQUIRED = NO
DOCUMENT_TYPE = GOVERNANCE_SYSTEM_MATRIX
GOVERNANCE_CONTRACT_VERSION = 1
NORMATIVE_OWNER = GOVERNANCE_SYSTEM_ARCHITECTURE
PROJECT_GOVERNANCE_ROOT_AUTHORITY = Politica-Matriz-de-Governanca-de-Projetos-v1.0.md
```

## 1. Finalidade e limites

Esta matriz define a arquitetura normativa transversal para governança de projetos: identidade, domínios, precedência, dependências, carregamento seletivo, conflitos e controle do registry. Ela é o entrypoint do sistema e não replica o conteúdo das policies subordinadas.

```text
MATRIX_POLICY != COPY_OF_ALL_SUBPOLICIES
MATRIX_DEFINES_SYSTEM
SUBPOLICY_DEFINES_ITS_DOMAIN
POLICY = WHAT_MUST_BE_TRUE
PROTOCOL = HOW_TO_EXECUTE_A_SPECIFIC_PROCESS
```

Protocols permanecem fora desta pasta e consomem a matriz. Authorities específicas de cada projeto permanecem no próprio projeto e governam seu domínio local conforme a precedência abaixo.

## 2. Invariantes de governança

```text
ONE_NORMATIVE_OWNER_PER_RULE = REQUIRED
SINGLE_SOURCE_OF_TRUTH = REQUIRED
DETAIL_ONCE_REFERENCE_EVERYWHERE_ELSE = REQUIRED
SELECTIVE_POLICY_LOADING = REQUIRED
```

Cada regra normativa tem uma única authority proprietária. Outros documentos podem resumir e apontar para ela, sem criar uma segunda versão normativa. O `POLICY_REGISTRY.json` identifica policies, versões, status, responsabilidades, dependências e proveniência; não substitui o conteúdo normativo.

## 3. Responsibility map

| ID | Policy | Responsabilidade normativa |
|---|---|---|
| PM-01 | `policies/PM-01-Conducao-de-Projetos-v1.0.md` | Condução de projetos: roadmap, phases, delivery units, slices, activities, integração incremental, DoR, DoD, progresso, avanço, continuidade, rastreabilidade e handoff. |
| PM-02 | `policies/Politica-Prompts-Agente-v1.7-R2.5.md` | Geração de prompts, seleção de modelo e esforço, Card A/Card B, payload do executor e recomendação de roteamento. |
| PM-03 | `policies/AGENTS-Multiagente-Generico-v1.7-R2.2-Roteamento-Economico.md` | Execução DIRECT vs MULTIAGENT, papéis, delegação, roteamento econômico, perfis registrados e gates multiagente. |
| PM-04 | `policies/Politica-de-Uso-de-Skills-e-Plugins-Codex-Work-v1.2.md` | Execução nativa, skills, plugins, disponibilidade, invocação e permissões. |
| PM-05 | `policies/Independencia-Analitica-Agente-v1.md` | Independência analítica, evidência e lógica, qualidade decisória e disciplina epistêmica. |

Os IDs PM-02 a PM-05 são identificadores desta matriz. Seus nomes de arquivo e conteúdo canônicos permanecem preservados. Atribuir responsabilidade não amplia o escopo declarado em uma subpolicy.

## 4. Precedência

Aplicar a seguinte ordem, respeitando o escopo de cada authority e as condições abaixo:

1. Instrução explícita e atual do usuário, dentro dos limites da governança obrigatória e dos mecanismos de exceção autorizados por ela.
2. Authority canônica específica do projeto, para fatos, contratos e decisões locais do projeto.
3. Esta matriz, para a arquitetura e as regras do sistema global de governança.
4. Subpolicy aplicável, dentro de seu domínio normativo.
5. Protocol operacional aplicável.
6. Convenção, template ou exemplo.

```text
USER_FINAL_AUTHORITY = PRESERVED
USER_INSTRUCTION != SILENT_POLICY_OVERRIDE
EXCEPTION_TO_MANDATORY_GOVERNANCE =
EXPLICIT
+ SCOPED
+ AUTHORIZED
+ TRACEABLE
+ ALLOWED_BY_POLICY
```

A autoridade final do usuário sobre objetivo, escopo e decisões autorizáveis é preservada. Uma instrução atual não derroga nem enfraquece silenciosamente uma regra obrigatória. Uma exceção só se aplica quando os cinco critérios acima forem atendidos pela policy competente; sem isso, não tratar o conflito como autorização. Se necessário, interromper somente a ação afetada e encaminhar a alteração da própria policy pelos mecanismos de revisão e canonicalização.

Authority específica do projeto pode definir fatos, contratos e decisões locais e especializar a aplicação da governança global dentro de seu domínio:

```text
PROJECT_SPECIFIC_AUTHORITY MAY_SPECIALIZE_GLOBAL_GOVERNANCE = YES
PROJECT_SPECIFIC_AUTHORITY MUST_NOT_SILENTLY_WEAKEN_GLOBAL_GOVERNANCE = YES
```

Uma authority de nível superior não apaga silenciosamente o domínio de outra. Se houver conflito material, identificar regras e escopos, interromper somente a atividade afetada e reconciliar com a authority competente. Não inferir supersession. Alteração de precedence ou canonicalização exige revisão explícita e atualização do registry.

## 5. Dependency e load map

```text
ALWAYS_LOAD = PROJECT_GOVERNANCE_MATRIX
LOAD_BY_ACTIVITY = APPLICABLE_SUBPOLICIES_ONLY
```

| Classe de atividade | Conjunto requerido |
|---|---|
| Planejamento de roadmap ou sprint | Matriz + PM-01 |
| Execução de projeto ou fechamento de slice | Matriz + PM-01 |
| Geração de prompt para Codex/Work | Matriz + PM-02 + PM-03; incluir PM-04 quando skills/plugins forem materialmente pertinentes |
| Roteamento multiagente | Matriz + PM-02 + PM-03 |
| Decisão sobre skill ou plugin | Matriz + PM-04; incluir PM-02 se a decisão integrar um prompt |
| Decisão técnica material | Matriz + PM-05 + policy de domínio aplicável; incluir PM-01 quando afetar execução, estado ou avanço do projeto |
| Continuidade ou handoff | Matriz + PM-01 + policies aplicáveis ao protocolo/atividade retomada |

O bootstrap ou protocolo determina a sequência de leitura e verificação. Carregar uma policy não autoriza a atividade. Aplicabilidade e autorização continuam sujeitas às authorities próprias.

## 6. Canonicalização, identidade e supersession

Uma policy só é current quando sua identidade, `STATUS`, `LIFECYCLE` e relações documentais sustentam essa condição. O registry registra evidências observadas; não promove documentos. Preservar nomes canônicos existentes. Registrar `supersedes` somente quando declarado ou demonstrado por relação documental explícita. `PREVIOUS_BASE`, `BASELINE`, `CONSOLIDATES` e alinhamentos são relações distintas e não devem ser convertidos automaticamente em `supersedes`.

Nova versão proposta não substitui a vigente antes de revisão e canonicalização autorizadas. Arquivos históricos não são carregados como atuais. Hashes verificam cópia e integridade de bytes, não autoridade normativa.

## 7. Conflitos e manutenção

Uma regra pertence a um único normative owner. Sobreposição aparente deve ser resolvida pelo escopo declarado e pelas relações de dependência. Se não for possível decidir sem alterar significado, registrar o conflito e bloquear a interpretação afetada; não duplicar regra em uma nova policy para contornar o conflito.

Mudanças de policy exigem atualização coerente de versão, status, registry, dependências e referências. A matriz e o registry devem concordar em IDs, arquivos, responsabilidades e estado de revisão. Atualizações de subpolicy não autorizam editar sua cópia canônica nesta pasta sem procedimento de revisão definido.

```text
GOVERNANCE_CONTRACT_VERSION = 1
SUBPOLICY_COMPATIBLE_REVISION != PROTOCOL_MAJOR_REVISION_REQUIRED
```

Incrementar `GOVERNANCE_CONTRACT_VERSION` quando uma mudança estrutural incompatível alterar o contrato global consumido por policies ou protocolos. Uma revisão compatível de subpolicy, por si só, não exige incremento da versão major do protocolo.

## 8. Relação com protocolos e projetos

Protocolos operacionalizam processos e devem referenciar a matriz e as subpolicies aplicáveis. Não devem redefinir silenciosamente policy global. Cada projeto mantém suas próprias authorities, estado factual e contratos; esta matriz não substitui tais documentos nem autoriza alterações em projetos.

## 9. Estado vigente da matriz

```text
MATRIX_STATUS = CANONICAL
LIFECYCLE = ACTIVE
CANONICALIZATION = YES
USER_REVIEW_REQUIRED = NO
```

Esta é a matriz canônica vigente da Governance Baseline V1. Alterações futuras seguem o processo de revisão e canonicalização registrado no registry.


## 10. Protocolos de validação

Protocolos de validação podem testar, por evidência, a compreensão e aplicação da matriz e das subpolicies. Eles não são subpolicies, não recebem IDs PM e não criam ownership normativo paralelo. Artefatos de validação associados a esta arquitetura ficam separados em `validation/`; protocols operacionais específicos continuam fora de `policies/`.

VP-01 v2.0 identifica validation/Gate-de-Internalizacao-Operacional-v2.0.md como protocolo canônico ativo, com DOCUMENT_ROLE = VALIDATION_PROTOCOL e AUTHORITY_SCOPE = VALIDATION_ONLY. Ele valida a matriz e PM-01 a PM-05 por evidência; não cria policies, não promove candidates e preserva SELF_DECLARED_COMPLIANCE != EVIDENCE e READ_ONLY_VALIDATION = PRESERVED.

VP-01 v1.0 está SUPERSEDED / HISTORICAL para a authority global; sua cópia embutida no pacote de abertura 2.0 é um snapshot local legado e não reativa a authority global. A v2.0 é a única versão operacional atual do protocolo.

## 11. Governance Baseline V1

GOVERNANCE_BASELINE = V1
GOVERNANCE_BASELINE_STATUS = CANONICAL
GOVERNANCE_BASELINE_LIFECYCLE = ACTIVE
GOVERNANCE_CONTRACT_VERSION = 1

| ID | Versão operacional atual |
|---|---|
| PM-00 | v1.0 |
| PM-01 | v1.0 |
| PM-02 | R2.5 |
| PM-03 | R2.2 |
| PM-04 | v1.2 |
| PM-05 | v1 |
| VP-01 | v2.0 — VALIDATION_ONLY |

ONE_OPERATIONAL_CURRENT_VERSION_PER_POLICY_ID = REQUIRED
ONE_OPERATIONAL_CURRENT_VERSION_PER_PROTOCOL_ID = REQUIRED

## 12. Pacotes de protocolo 2.0

PROTOCOL_2_0_PACKAGES = PRE_MATRIX_LEGACY_BASELINE
PROTOCOL_2_0_MUTATION_DURING_GOV01D = PROHIBITED
EMBEDDED_POLICY_OR_VALIDATION_COPIES_IN_PROTOCOL_2_0 = PACKAGE_LOCAL_LEGACY_SNAPSHOTS
EMBEDDED_LEGACY_COPY != CURRENT_GLOBAL_GOVERNANCE_AUTHORITY
FIRST_PROTOCOL_GENERATION_NATIVE_TO_GOVERNANCE_CONTRACT_V1 = 3.0

Pacotes 2.0 permanecem como baseline legado e rollback. Cópias de policies e do VP-01 v1.0 embutidas nesses pacotes são snapshots locais; não reativam authority global superseded. A migração dos protocolos ocorrerá em GOV-02 e GOV-03.