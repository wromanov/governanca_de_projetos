# GOV-09 — Plano de Rollback Determinístico

`ROLLBACK_EXECUTION = NOT_PERFORMED`

Este plano descreve uma reversão futura; não altera o estado atual.

## 1. Triggers

Iniciar rollback e interromper a promoção se ocorrer qualquer condição:

- hash de v1.6 ou v1.1 diferente do hash aprovado;
- diff fora da allowlist de canonicalização-only;
- `NORMATIVE_CONTENT_UNCHANGED != YES`;
- authority lógica duplicada ou caminho ativo ambíguo;
- divergência entre ZIP e árvore extraída;
- missing/extra/hash mismatch em qualquer manifest;
- `PROJECT_STATE` não reconciliado com os ZIPs observados;
- falha de substituição de qualquer representação no commit da transação;
- referência ativa ainda aponta para v1.4, v1.0 ou v1.5;
- post-promotion validation falha;
- Project Opening dependency permanece não resolvida;
- usuário retira a autorização ou a promoção é interrompida.

## 2. Inputs imutáveis do rollback

O snapshot S0 deve conter, antes de qualquer escrita autorizada:

1. as duas cópias extraídas de Prompt v1.4 e seus hashes;
2. as duas cópias extraídas de Skills v1.0 e seus hashes;
3. os dois ZIPs observados, bytes completos, sizes e hashes;
4. as árvores extraídas completas, inclusive `START_HERE`, README, payload e
   manifests;
5. `STARTER_MANIFEST.md`, `CONTINUITY_MANIFEST.md`, `PACKAGE_MANIFEST.md` e
   `PROJECT_STATE.md` completos;
6. o conteúdo draft v1.5 e os artifacts de revisão GOV-02 a GOV-08;
7. lista de files, status Git, branch, remote, staging e untracked files;
8. journal ordenado de cada operação e seu resultado.

O snapshot deve ser preservado sem overwrite e deve permitir recompor os
packages anteriores mesmo que a troca final tenha começado.

## 3. Sequência

| ROLLBACK_STEP | ACTION | RESULTADO ESPERADO |
|---|---|---|
| RB-01 | parar imediatamente novas substituições e marcar transação como abortada | nenhum passo adicional de promoção é iniciado |
| RB-02 | preservar o estado parcial e o journal para auditoria | evidência de falha não é apagada |
| RB-03 | restaurar as policies antigas nos dois caminhos ativos | Prompt v1.4 volta a ser vigente e Skills v1.0 volta a ser vigente |
| RB-04 | restaurar a composição anterior das árvores extraídas | entrypoints, README, payload e manifests retornam aos bytes S0 |
| RB-05 | restaurar `STARTER_MANIFEST.md`, `CONTINUITY_MANIFEST.md`, `PACKAGE_MANIFEST.md` e `PROJECT_STATE.md` | manifests/state retornam exatamente ao snapshot S0 |
| RB-06 | restaurar os dois ZIPs anteriores | packages anteriores retornam byte-identicamente ao snapshot S0 |
| RB-07 | remover apenas artifacts temporários de staging, sem apagar snapshot ou evidência | working area limpa; histórico do rollback preservado |
| RB-08 | validar hashes, sizes, entries e referências contra S0 | `RESTORED_TO_SNAPSHOT = YES` ou rollback fica FAIL |
| RB-09 | registrar que qualquer finding pré-existente, incluindo F01-F03, permanece finding | rollback não é usado para ocultar ou corrigir silenciosamente findings |

O rollback deve restaurar também a árvore extraída anterior; restaurar apenas
os ZIPs não é suficiente.

## 4. Validação do rollback

```text
PROMPT_v1.4_RESTORED = YES
SKILLS_v1.0_RESTORED = YES
PROMPT_v1.4_HASH = 8006DB0B5161B6CAC1604203BA5EAC09AAE964C5E65BCA6B00C3194B387AD069
SKILLS_v1.0_HASH = C0D657C673B93719F250DCB52F2DA5853E1C33ECA202D769570A8EF742D5D695
PREVIOUS_PACKAGES_RESTORED = YES
PREVIOUS_MANIFESTS_RESTORED = YES
PREVIOUS_HASH_REGISTRY_RESTORED = YES
PREVIOUS_EXTRACTED_TREES_RESTORED = YES
SNAPSHOT_BYTE_IDENTITY = REQUIRED
ROLLBACK_VALIDATION = PASS_ONLY_IF_ALL_ABOVE_PASS
```

Se S0 contiver a divergência conhecida entre `PROJECT_STATE` e os ZIPs
observados, a validação deve registrar a divergência como preexistente e
restaurada; não deve alegar que o rollback corrigiu F03.

## 5. Gate

`ROLLBACK_PLAN_READY = YES`

`ROLLBACK_SAFE_BOUNDARY = S0_BEFORE_ANY_PROMOTION_WRITE`

`ROLLBACK_EXECUTED = NO`
