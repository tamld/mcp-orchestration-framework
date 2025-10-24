# Walkthrough Demo – MCP Orchestration Framework

## Context
Customer request: "Show how MCP agents plan and log while keeping sensitive details hidden."

## Demo Steps
1. **Bootstrap** – run `./tools/bootstrap_orchestrator.sh --fast` and display the console output.
2. **Reflection** – open `memory/templates/contract_template.md`, fill the summary (mask details).
3. **Execution** – update the README (architecture only) and record evidence in runtime `.agents/logs/` (gitignored).
4. **Review** – complete `docs/briefs/sanitize_checklist.md` before pushing.

## Expected Outcomes
- Stakeholders see the guardrail-compliant workflow.
- No sensitive data is exposed.
- Evidence logs confirm each action.

> Note: the PoC never enables real anchors. Any upgrade requires Gate G3 sign-off and a private channel.
