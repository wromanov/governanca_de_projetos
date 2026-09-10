# GOV-09 — Plano de Promoção Coordenada

`PROMOTION_EXECUTION = NOT_AUTHORIZED`

`STAGE = NOT_AUTHORIZED`

`COMMIT = NOT_AUTHORIZED`

`PUSH = NOT_AUTHORIZED`

## 1. Decisão de atomicidade

`COORDINATED_PROMOTION_REQUIRED = YES`

É inseguro promover uma policy antes da outra. A Prompt Policy v1.6 declara o
contrato transversal e a Skills/Plugins v1.1 é a authority especializada para
classificação, disponibilidade, provenance e invocação. Uma promoção parcial
criaria referências de versão e source-of-truth cruzadas, além de invalidar a
integração aprovada em GOV-08.

A promoção futura deve ser uma transação coordenada de representations,
manifests, árvores e ZIPs. Nenhuma policy deve ser declarada `CANONICAL` antes
da validação de todo o conjunto.

## 2. Modelo de canonicalização-only

### 2.1 Prompt Policy v1.6

`APPROVED_CONTENT_HASH = F9EC62AF541766E95C5A52115977C8AEDE27E93DCF61037D2F18DB3A5C0FF8B5`

Somente os seguintes metadados/effective-state references podem mudar na
representação final:

| Local lógico | Valor aprovado | Valor canônico futuro |
|---|---|---|
| `STATUS` | `PROPOSED` | `CANONICAL` |
| `LIFECYCLE` | `DRAFT` | `VIGENTE` |
| `CANONICALIZATION` | `NO` | `COMPLETED` |
| `PROMOTION` | `NO` | `COMPLETED` |
| `USER_REVIEW_REQUIRED` | `YES` | `NO` |
| `PROPOSED_POLICY_REVIEW` | `REQUIRED` | `COMPLETED` |
| `POLICY_EFFECTIVE` | `NO` | `YES` |
| `CANONICALIZATION_AUTHORIZED` | `NO` | `YES`, somente com autorização futura registrada |
| `PROMOTION_AUTHORIZED` | `NO` | `YES`, somente com autorização futura registrada |
| blockquote de estado | v1.4 authority; v1.5 draft; v1.6 não vigente | v1.6 authority vigente; v1.5 histórico draft; promoção concluída |
| effective-state reference | `v1.4` como vigente | `v1.6` como vigente; v1.4/v1.5 somente históricas |

`CANONICAL_AUTHORITY_BASELINE = v1.4` e `CONTENT_BASELINE = v1.5` devem
permanecer como provenance da genealogia; não podem ser apagados nem
reinterpretados como authority atual.

### 2.2 Skills/Plugins Policy v1.1

`APPROVED_CONTENT_HASH = 6C67CDA78256BE6EE336E1117266316F65DEB86527DE5855016018865553DDA2`

Somente os seguintes metadados/effective-state references podem mudar:

| Local lógico | Valor aprovado | Valor canônico futuro |
|---|---|---|
| título de estado `Versão 1.1` | `PROPOSTA CONTROLADA` | `CANÔNICA VIGENTE` |
| `STATUS` | `PROPOSED` | `CANONICAL` |
| `LIFECYCLE` | `DRAFT` | `VIGENTE` |
| `CANONICALIZATION` | `NO` | `COMPLETED` |
| `PROJECT_PROPAGATION` | `NO` | `COMPLETED` |
| `USER_REVIEW_REQUIRED` | `YES` | `NO` |
| seção 20, effective-state reference | v1.4 authority vigente | v1.6 authority vigente |
| footer `Status` | `PROPOSED / DRAFT` | `CANONICAL / VIGENTE` |
| footer `Canonicalização` | `NÃO executada` | `CONCLUÍDA SEM ALTERAÇÃO NORMATIVA` |
| footer `Revisão do usuário` | obrigatória antes de promoção | adjudicação concluída; promoção registrada |

As referências às v1.0 e v1.4 na seção de fontes e baseline permanecem como
provenance histórica. A regra normativa que exige sincronização com a Prompt
Policy permanece intacta.

### 2.3 Gate de conteúdo normativo

`NORMATIVE_CONTENT_CHANGE_REQUIRED = NO`

Para ser válido, o artifact final deve satisfazer:

```text
APPROVED_CONTENT_HASH = hash da fonte draft aprovada
FINAL_CANONICAL_ARTIFACT_HASH = hash novo após metadata-only change
NORMATIVE_CONTENT_UNCHANGED = YES
CANONICALIZATION_SCOPE_VIOLATION = NO
```

A verificação futura deve comparar o artifact aprovado e o final após remover
somente as spans explicitamente allowlisted nas tabelas acima. Qualquer diff
fora dessa allowlist, inclusive mudança de regra, exemplo, limiar, proibição,
authority ou semântica, deve interromper a promoção.

Os hashes finais não são conhecidos neste preflight porque a canonicalização
não foi executada.

## 3. Plano numerado

| STEP_ID | FASE | ACTION | FILES/REPRESENTATIONS | PRECONDITION | EXPECTED_RESULT | ROLLBACK_POINT | USER_AUTHORIZATION_REQUIRED |
|---|---|---|---|---|---|---|---|
| GOV09-P01 | PREPARE | congelar bytes, paths, sizes, hashes, manifests, ZIPs, árvore extraída e estado Git | todas as representations atuais | F01/F02/F03 adjudicados ou snapshot explicitamente aceito | baseline reprodutível e journal de promoção | snapshot S0 | YES |
| GOV09-P02 | PREPARE | construir staging isolado para as duas trees e os dois packages | árvores, policies, manifests | S0 íntegro; sem escrita em `Vigente` | staging completo, sem mistura de package | S1 | YES |
| GOV09-P03 | CANONICALIZE | gerar cópias finais das duas candidatas alterando somente a allowlist de metadata | v1.6 e v1.1 | hashes aprovados exatos; aprovação de promoção | `NORMATIVE_CONTENT_UNCHANGED = YES`; hashes finais registrados | S2 | YES |
| GOV09-P04 | CANONICALIZE | preservar v1.4, v1.5 e v1.0 como histórico/provenance | antigos artifacts e snapshot | destino histórico aprovado; nenhum overwrite | predecessor histórico recuperável | S3 | YES |
| GOV09-P05 | PACKAGE | reconciliar composição das árvores segundo seus manifests correspondentes | START_HERE, README, payload, manifests | F01/F02 resolvidos; package authority definida | cada tree corresponde ao ZIP correspondente | S4 | YES |
| GOV09-P06 | PACKAGE | atualizar entries, sizes e hashes em manifests e state | STARTER_MANIFEST, CONTINUITY_MANIFEST, PACKAGE_MANIFEST, PROJECT_STATE | policies finais e composition fechadas | zero missing/extra/hash mismatch em staging | S5 | YES |
| GOV09-P07 | PACKAGE | reconstruir ambos os ZIPs e validar conteúdo, manifest interno e ZIP hash | dois ZIPs `FINAL-AUDIT` | S5 pass | ZIPs byte-validos e package hashes registrados | S6 | YES |
| GOV09-P08 | VALIDATE | comparar ZIPs com árvores extraídas e verificar ausência de references ativas antigas | dois ZIPs, duas trees, manifests | S6 pass | composition, identity e active authority consistentes | S7 | YES |
| GOV09-P09 | PROMOTE | substituir coordenadamente todas as representations ativas no ponto de commit da transação | policies, trees, manifests, ZIPs, state | P01-P08 pass; user authorization específica | conjunto promovido sem estado intermediário declarado | S8, com rollback imediato se falhar | YES |
| GOV09-P10 | VALIDATE | executar post-promotion validation e declarar v1.6/v1.1 canônicas | conjunto completo | promoção concluída; todas validações pass | canonical state fechado e evidenciado | S9 | YES |
| GOV09-P11 | GIT | somente se autorizado, revisar diff, stage/commit conforme decisão do baseline | Git repository | Project Opening Gate PASS e autorização separada | primeiro baseline aprovado | S10 | YES |

Os passos P01-P11 são plano futuro; nenhum foi executado nesta atividade.

## 4. Project Opening e primeiro baseline

`CAN_POLICY_PROMOTION_PRECEDE_PROJECT_OPENING_GATE = YES`.

Justificativa: o Wizard define que o Project Opening Gate deve avaliar
documentação, source-of-truth, referências, continuidade, state e ausência de
conflito material. O gate deve consumir o package final e coerente; promover a
policy depois do gate produziria mudança de dependency imediatamente após a
avaliação. Isso não autoriza a promoção: F01-F03 precisam ser resolvidos e a
autorização física continua pendente.

`PROJECT_OPENING_GATE = NOT_EVALUATED`.

A decisão anterior de realizar o primeiro commit depois do Project Opening
Gate PASS permanece. O melhor encaixe é a opção `C`: depois de a promoção ser
explicitamente autorizada, validada e colocada antes da avaliação do gate, o
primeiro commit pode conter o mesmo primeiro baseline aprovado após o gate.

`INITIAL_COMMIT_DECISION_CHANGE_REQUIRED = NO`.

## 5. Pós-promoção obrigatória

Somente declarar sucesso se todas estas condições forem PASS:

1. v1.6 é a única Prompt Policy ativa;
2. v1.1 é a única Skills/Plugins Policy ativa;
3. v1.4 e v1.0 não aparecem como atuais;
4. v1.5 permanece `HISTORICAL INTERMEDIATE DRAFT` e `NEVER_CANONICAL`;
5. os dois ZIPs contêm as versões e names corretos;
6. manifests e `PROJECT_STATE` têm hashes recalculados;
7. árvores e ZIPs têm composição idêntica;
8. não há referência ativa a predecessor antigo;
9. o diff allowlisted prova conteúdo normativo inalterado;
10. o snapshot e o rollback continuam utilizáveis.

`POST_PROMOTION_VALIDATION_READY = YES`
