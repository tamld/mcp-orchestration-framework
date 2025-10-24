# Agent Guide – MCP Orchestration Framework

## Sources of Authority
- **Global SSoT**: `${MCP_ROOT}` (references the central MCP repository). Never override core laws locally.
- **This repository**: only adds PoC procedures; do not relax guardrails.
- If conflicts appear → follow Global guidance and log the deviation in `.agents/backlog/conflicts.yaml`.

## Bootstrap Checklist
1. Run `tools/bootstrap_orchestrator.sh --fast`.
2. Read `README.md` and `docs/design/overview.md`.
3. Follow LAW-REFLECT-001: reflect → create a ≤5 step plan → execute minimally.

## Mandatory Artefacts
- `tech_fit.yaml`
- `tests/PLAN.md`
- `.agents/logs/*.jsonl` (schema defined in `${MCP_ROOT}/schemas/aa_log.schema.json`)
- `docs/briefs/*` (pros/cons, roadmap) plus the sanitize checklist.

## Security Policy
- Replace proprietary details with `REDACTED`.
- Every public PR must run `python tools/sanitize_manifest.py --dry-run`.
- Real anchors/bundles are disabled in this PoC; enable only after Gate G3 in a private repo.

## Pre-commit Checklist
- [ ] Scope contract and assumptions logged in `.agents/logs/`.
- [ ] Sanitize script executed and result recorded.
- [ ] Evidence links added to relevant artefacts.
- [ ] Deviation reason written when skipping any “should” artefact.

## Contacts
- `owner`: MCP AI Operations Team (placeholder)
- `aa_id`: record the agent identifier in activity logs.
