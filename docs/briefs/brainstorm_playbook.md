# Brainstorm Collaboration Playbook

This playbook keeps brainstorming collaborative, auditable, and aligned with the SoT philosophy while ensuring humans stay in an oversight role.

## 1. Purpose
- Maintain a transparent, version-controlled space for ideation that complements the MCP Orchestration Framework.
- Guarantee that every brainstorm entry references the Single Source of Truth (SoT) and can mature into formal plans or lessons.

## 2. Roles
| Role | Responsibilities |
| --- | --- |
| Moderator (human overseer, default: `tamld`) | Defines the topic, sets guardrails, reviews conflicts, approves final outcomes. Does **not** author ideas unless clarification is needed. |
| Contributors (AAs: `codex`, `gemini`, `perplexity`, etc.) | Own the brainstorming process end-to-end: create content, log reflections, cross-review, keep evidence updated. |
| Observer (optional stakeholder) | Read-only; raises feedback via issues/comments. |

## 3. Branch Workflow
1. **Create topic branch** (Moderator):
   ```bash
   git checkout main
   git pull origin main
   git checkout -b brainstorm/<topic>-<YYYYMMDD>
   git push -u origin HEAD
   ```
2. **Scaffold session** (Moderator):
   - Create `brainstorm/<topic>/README.md` from `brainstorm/templates/session_readme_template.md`.
   - Commit & push the scaffold (objective, guardrails, participant list).
3. **Contributors (AAs) join and lead**:
   ```bash
   git fetch origin
   git checkout brainstorm/<topic>-<YYYYMMDD>
   git pull --ff-only
   ```
4. **Contribution layout** (AAs):
   - Ideas: `brainstorm/<topic>/ideas/<aa_id>/<slug>.md`
   - Evidence: `brainstorm/<topic>/evidence/<filename>.*`
   - Update session README tables (contributions, open questions) as work progresses.
5. **Commit etiquette**:
   - One idea/change per commit (`feat(brainstorm): add idea on stm-delta-evaluation`).
   - Include front matter with author, timestamp, question, related artefacts, confidentiality level.
6. **Draft PR** (AAs):
   - Open a draft PR to `main`, mention `@codex` for Copilot review, summarise objectives and key findings.
   - Continue iterating in the branch until the session completes.
7. **Merge & archive** (Moderator):
   - Verify CI (sanitize, pytest) is green and no conflicts exist.
   - Approve/merge once conflicts are resolved; update SoT artefacts with accepted outcomes.

## 4. Contribution Rules & Templates
- **Reflection-first**: each idea starts with LAW-REFLECT-001 notes before proposing actions.
- **Front matter** (required):
  ```markdown
  ---
  author: codex
  timestamp: 2025-10-24T17:00:00Z
  question: "How do we quantify STM→LTM delta?"
  related_artifacts:
    - docs/briefs/project_charter.md
    - samples/logs/2025-10-24T150000Z.jsonl
  confidentiality: public-poc
  ---
  ## Idea
  ...
  ```
- **Question tracking**: list questions in session README and mark them resolved via commits.
- **Sensitive data**: redact immediately; use ticket references if further detail resides outside the repo.
- **Cross-feedback**: AAs comment inside idea files using blockquotes with their IDs.

## 5. Review & Promotion
- PR description should include a table: ✔ accepted / ❓ needs data / ✖ dropped.
- Accepted ideas map to tasks (update `plans/poc/ROADMAP.md` or create backlog entries). Rejected ideas remain for traceability.
- Lessons feed the STM → LTM lifecycle once evidence satisfies thresholds.

## 6. Automation & Guardrails
- Optional GitHub Actions: enforce structure, check front matter, run sanitize script.
- Auto-merge policy obeys `docs/briefs/contribution_policy.md` (CI green, no conflicts, Copilot review).
- Branch protection ensures only moderators can merge; contributors request human approval when conflicts arise.

## 7. Retrospective & Reporting
- After merge, add `brainstorm/<topic>/RETRO.md` summarising outcomes, risks, follow-ups.
- Mention retrospectives in the monthly executive summary for stakeholders.
- Optionally tag the merge commit (e.g., `brainstorm/<topic>-<YYYYMMDD>`).

## 8. Security Considerations
- No credentials, API tokens, or customer specifics in brainstorm artefacts.
- Keep runtime `.agents/` logs local; share sanitized examples via `samples/`.
- Run `python tools/sanitize_manifest.py --root .` before each push.
- Document any accidental exposure in the retrospective and project charter risk log.

This playbook keeps brainstorming AA-led, with humans providing review and approval only when conflicts or escalation paths demand oversight.
