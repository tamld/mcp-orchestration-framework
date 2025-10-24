# Brainstorm Collaboration Playbook

This playbook explains how AI agents (AAs) collaborate on structured brainstorming sessions while keeping every artefact traceable in the repository.

## 1. Purpose
- Maintain a transparent, version-controlled space for ideation that complements the MCP Orchestration Framework.
- Ensure every brainstorm item references the Single Source of Truth (SoT) and can graduate into formal plans or lessons.

## 2. Roles
| Role | Responsibilities |
| --- | --- |
| Moderator (default: `tamld`) | Defines the topic, creates the branch, reviews contributions, merges outcomes. |
| Contributors (AAs, e.g., `codex`, `gemini`, `perplexity`) | Pull the latest branch, add ideas/evidence, follow guardrails. |
| Observer (optional stakeholders) | Read-only; provide feedback through issues or comments. |

## 3. Branch Workflow
1. **Create topic branch** (Moderator):
   ```bash
   git checkout main
   git pull origin main
   git checkout -b brainstorm/<topic>-<YYYYMMDD>
   git push -u origin HEAD
   ```
2. **Prepare workspace for contributors**:
   - Add a session README under `brainstorm/<topic>/README.md` describing goals, timeline, and success criteria.
   - Commit & push the initial scaffold.
3. **Contributors join**:
   ```bash
   git fetch origin
   git checkout brainstorm/<topic>-<YYYYMMDD>
   git pull --ff-only
   ```
4. **Contribution cadence**:
   - Each idea lives under `brainstorm/<topic>/ideas/<aa_id>/<slug>.md`.
   - Evidence or supporting artefacts go in `brainstorm/<topic>/evidence/<filename>.*`.
   - Update the session README with summaries or decisions after each round.
5. **Commit guidelines**:
   - Use clear messages, e.g., `feat(brainstorm): add idea on stm-delta-evaluation`.
   - Run mandatory checks (sanitize + pytest if applicable) before pushing.
6. **Draft PR**:
   - Open a draft PR targeting `main`.
   - Mention `@codex` for Copilot review and note the brainstorming objective.
7. **Merge & archival**:
   - Moderator converts the PR to “Ready for review” once the session is complete and CI is green.
   - After merge, update `docs/briefs/project_charter.md` or relevant artefacts with decisions, if any.

## 4. Contribution Rules
- Respect LAW-REFLECT-001: note the reflection step before proposing a solution.
- Cite SoT references (e.g., template IDs, policy sections) within each idea file.
- Keep sensitive data out; use `REDACTED` placeholders when necessary.
- Limit a single idea per file to maintain atomic history.
- Prefer Markdown with front matter template:
  ```markdown
  ---
  author: codex
  timestamp: 2025-10-24T17:00:00Z
  confidence: medium
  related_artifacts:
    - docs/briefs/project_charter.md
    - samples/logs/2025-10-24T150000Z.jsonl
  ---
  ## Idea
  ...
  ```

## 5. Review & Promotion
- Use the PR discussion for quick triage (mark ideas as ✔ accepted, ❓ needs data, ✖ dropped).
- Accepted ideas should map to follow-up tasks in `plans/poc/ROADMAP.md` or backlog entries.
- Lessons stemming from the brainstorm should pass through the STM → LTM evaluation process.

## 6. Automation Hooks
- Optional GitHub Action can enforce directory structure (`brainstorm/<topic>/...`) and sanitize checks.
- Auto-merge remains subject to CI success, no conflicts, and Copilot review (see `docs/briefs/contribution_policy.md`).

## 7. Session Retrospective
- After merging, create `brainstorm/<topic>/RETRO.md` summarising outcomes, risks, and next actions.
- Mention retrospectives in the monthly executive summary for stakeholders.

Following this playbook ensures every brainstorming effort remains auditable, structured, and easy to roll into production planning.
