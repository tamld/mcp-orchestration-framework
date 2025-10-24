# Test Plan – MCP Orchestration Framework

## Scope
- Verify the PoC bootstrap runs in dry-run mode.
- Ensure mandatory artefacts exist and comply with schemas.
- Confirm the sanitize checklist reports no risks.

## Test Cases
| ID | Description | Gate | Type | Artefact |
| --- | --- | --- | --- | --- |
| TC-BOOT-01 | Run `tools/bootstrap_orchestrator.sh --fast` | G0 | Manual | console log |
| TC-SAN-02 | Execute `python tools/sanitize_manifest.py --dry-run` | G1 | Automated | sanitize output |
| TC-DOC-03 | Review `README.md` & `docs/briefs` for sensitive data | G1 | Manual | checklist |
| TC-DEMO-04 | Follow `samples/session_walkthrough.md` customer demo | G2 | Manual | feedback notes |

## Automation Hooks
- When migrating to a private repo (G3), integrate CI with `pre-commit` (ruff, markdownlint).

## Rollback Strategy
- If leakage is detected → remove the public commit, update the sanitize checklist, log the deviation in runtime `.agents/logs/` (gitignored) and capture a sanitized copy in `samples/logs/` if required.
