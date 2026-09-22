# Protocolo — Início de Abertura de Projeto

DOCUMENT_TYPE = OPERATIONAL_ENTRYPOINT
STATUS = CANONICAL
NORMATIVE_AUTHORITY = Project Opening Standard v1.0/PROJECT_OPENING_STANDARD.md
OPERATIONAL_PROTOCOL = Project Opening Standard v1.0/PROJECT_OPENING_WIZARD.md
CONTINUITY_DEPENDENCY = Agent-Continuity-Standard-v1.0/AGENT_CONTINUITY_STANDARD.md
VALIDATION_GATE_REFERENCE = Agent-Continuity-Standard-v1.0/policies/gate-de-internalizacao-operacional-teste-de-validacao-do-novo-agente.md
STARTER_CREATES_AUTHORITY = NO
PROJECT_SPECIFIC_STATE_INCLUDED = NO
CANONICAL_POLICY_MAP = CANONICAL_POLICY_MAP.md

1. Leia este arquivo, o Standard e o Wizard.
2. Leia a dependência universal de continuidade; ela está `CANONICAL` e não
   contém identidade ou state de projeto.
3. Leia e reconcilie todos os documentos aplicáveis antes de executar qualquer
   gate de internalização.
4. Ao final da leitura dos documentos, quando houver internalização de policy
   por novo agente, execute o gate referenciado acima em modo `READ-ONLY`.
5. Conduza as phases e gates do Wizard.
6. Materialize os artifacts do novo projeto a partir dos templates e forneça
   payload específico quando ocorrer continuidade real.
7. Após o Opening Gate, aplique o Agent Continuity Standard e seus gates.

Use `CANONICAL_POLICY_MAP.md` para resolver as policies transversais ativas;
não promova a candidata R2.4 sem a decisão de usuário exigida no documento.

Paths do projeto real são declarados em `AGENTS.md`; não inventar paths.
`Project Opening Standard v1.0/PROJECT_STATE.md` é state do pacote, não de um
projeto novo. `OPENING_LEDGER != PROJECT_STATE`.
