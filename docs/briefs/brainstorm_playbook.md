# Brainstorm Collaboration Playbook

This playbook ensures structured, auditable brainstorming across AI agents (AAs) while protecting sensitive information.

## 1. Purpose
- Maintain a transparent, version-controlled space for ideation that complements the MCP Orchestration Framework.
- Guarantee that every brainstorm item references the Single Source of Truth (SoT) and can mature into formal plans or lessons.

## 2. Roles
| Role | Responsibilities |
| --- | --- |
| Moderator (human overseer, default: `tamld`) | Defines the topic, sets guardrails, observes progress, resolves conflicts, and approves the final merge. Does **not** author ideas unless clarification is needed. |
| Contributors (AAs: `codex`, `gemini`, `perplexity`, etc.) | Lead the brainstorm: create content, log reflections, update tracking tables, respond to peer feedback, keep evidence fresh. |
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
   - Create `brainstorm/<topic>/README.md` using `brainstorm/templates/session_readme_template.md`.
   - Commit & push the scaffold (objective, guardrails, participant table, open questions).
3. **Contributors join and own the flow**:
   ```bash
   git fetch origin
   git checkout brainstorm/<topic>-<YYYYMMDD>
   git pull --ff-only
   ```
4. **Contribution layout (AA-owned)**:
   - Ideas: `brainstorm/<topic>/ideas/<aa_id>/<slug>.md`
   - Evidence/supporting docs: `brainstorm/<topic>/evidence/<filename>.*`
   - Tracking table in the session README updated per idea/question.
5. **Commit etiquette**:
   - 1 idea per commit (`feat(brainstorm): add idea on stm-delta-evaluation`).
   - Cite artefacts and related SoT references inside the Markdown front matter.
   - Update `brainstorm/<topic>/README.md` contribution table after each commit (AA responsibility).
6. **Draft PR** (AA-led):
   - Open a draft PR to `main`, mention `@codex` for Copilot review, describe objectives + summary.
7. **Merge & archive** (Moderator oversight):
   - Confirm CI is green and open questions are resolved.
   - Approve/merge once conflicts are addressed; link outcomes back to SoT artefacts (`docs/briefs/project_charter.md`, `plans/poc/ROADMAP.md`, lessons).

## 4. Contribution Rules & Templates
- **AA ownership**: contributors must document every idea/action; moderators intervene only when blockers, conflicts, or policy escalations occur.
- **Law compliance**: start each idea with reflection bullet points referencing LAW-REFLECT-001.
- **Front matter template** (required):
  ```markdown
  ---
  author: codex
  timestamp: 2025-10-24T17:00:00Z
  question: "How do we quantify STM→LTM delta?"
  related_artifacts:
    - docs/briefs/project_charter.md
    - samples/logs/2025-10-24T150000Z.jsonl
  confidentiality: public-poC
  ---
  ## Idea
  ...
  ```
- **Question tracking**: log in session README “Open Questions” checklist and mirror in commit messages when addressed.
- **Sensitive data**: redact immediately; if required for context, store in private systems and link via ticket ID.
- **Cross-feedback**: comment inside idea files using blockquotes (e.g., `> Feedback (gemini): ...`) to keep context centralized.
- **Logging requirement**: every idea commit must be referenced in the session README contribution table so moderators can audit progress without editing content themselves.

## 5. Review & Promotion
- Annotate the PR description with a decision table: Accepted ✔ / Needs Data ❓ / Dropped ✖. AAs keep this table current.
- Moderators review for alignment and resolve disagreements; if agents disagree, document both viewpoints and flag the moderator for arbitration.
- Accepted ideas become tasks (update `plans/poc/ROADMAP.md` or create backlog entries), while rejected ideas remain for traceability.
- Promote lessons into STM/LTM only after evidence satisfies thresholds **and** moderator approval is recorded in the session README.

## 6. Automation & Guardrails
- Optional GitHub Actions: lint directory structure, enforce front matter, run sanitize script.
- Auto-merge policy follows `docs/briefs/contribution_policy.md` (CI green, no conflicts, Copilot review).
- Use branch protection rules to ensure only authorized moderators merge brainstorm branches.

## 7. Retrospective & Reporting
- After merge, add `brainstorm/<topic>/RETRO.md` summarising outcomes, risks, and follow-up actions.
- Mention retrospectives in the monthly executive summary to stakeholders.
- Archive the branch (optionally tag with `brainstorm/<topic>-<YYYYMMDD>`).

## 8. Security Considerations
- No credentials, API tokens, or customer specifics in brainstorm artefacts.
- Use `samples/` directory for sanitized examples; keep runtime `.agents/` logs local.
- Run `python tools/sanitize_manifest.py --root .` before each push.
- If sensitive info is accidentally committed, remove via PR and document the incident in the retro + project charter risk log.

This playbook keeps brainstorming collaborative, auditable, and aligned with the SoT philosophy.
