# Protocolo — Início de Abertura de Projeto

DOCUMENT_TYPE = OPERATIONAL_ENTRYPOINT
NORMATIVE_AUTHORITY = Project Opening Standard v1.0/PROJECT_OPENING_STANDARD.md
OPERATIONAL_PROTOCOL = Project Opening Standard v1.0/PROJECT_OPENING_WIZARD.md
CONTINUITY_DEPENDENCY = Agent-Continuity-Standard-v1.0/AGENT_CONTINUITY_STANDARD.md
STARTER_CREATES_AUTHORITY = NO
PROJECT_SPECIFIC_STATE_INCLUDED = NO

1. Leia este arquivo, o Standard e o Wizard.
2. Leia a dependência universal de continuidade; ela está `READY_FOR_REVIEW`
   para rereauditoria e não contém identidade ou state de projeto.
3. Conduza as phases e gates do Wizard; use templates somente após avaliar
   applicability.
4. Materialize os artifacts do novo projeto a partir dos templates e forneça
   payload específico quando ocorrer continuidade real.
5. Após o Opening Gate, aplique o Agent Continuity Standard e seus gates.

Paths do projeto real são declarados em `AGENTS.md`; não inventar paths.
`Project Opening Standard v1.0/PROJECT_STATE.md` é state do pacote, não de um
projeto novo. `OPENING_LEDGER != PROJECT_STATE`.
