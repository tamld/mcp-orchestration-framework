# Contribution Policy & Auto-merge Rules

## Branch Strategy
- Use topic branches (`feature/...`, `fix/...`, `docs/...`) off `main`.
- Keep commits scoped and reference related artefacts (README sections, docs, samples).

## Mandatory Checks Before PR
1. `python tools/sanitize_manifest.py --root .`
2. `python3 -m venv .venv && source .venv/bin/activate && pip install -q -r requirements.txt && pytest`
3. Update artefact evidence (logs, plans) when changing workflows.
4. Add/refresh documentation where customer impact exists.

## Pull Request Workflow
- Push the branch and open a PR targeting `main`.
- Ensure GitHub Actions/CI status is **green**; auto-merge is enabled only when checks pass and no conflicts remain.
- Mention `@codex` in the PR description to trigger GitHub Copilot review for additional feedback.
- Keep PR description concise: motivation, changes, testing evidence, risk assessment.

## Auto-merge Policy
- Auto-merge requires:
  - All required CI checks succeed.
  - Branch has no merge conflicts with `main`.
  - Review from `@codex` (Copilot) is requested and completed.
- If any condition fails, auto-merge pauses; resolve issues and re-run checks.

## Release Notes
- Document customer-facing changes in `docs/briefs/value_story.md` or `docs/briefs/project_charter.md` (Roadmap section) as appropriate.
- For internal-only refactors, update the relevant plan/backlog notes.

## Incident Handling
- If a change causes a regression, revert via PR and document the lesson using the STM/LTM workflow.
- Notify stakeholders via the monthly executive summary or ad-hoc update.
