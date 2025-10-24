# Brainstorm Workflow – Assumptions, File Types & Lessons

## Preferred File Types for Brainstorm
| File Type | Usage | Why it works |
| --- | --- | --- |
| Markdown (`.md`) | Session README, individual ideas, retrospective | Human-readable, version-friendly, supports tables/front matter, Git diff friendly. |
| YAML (`.yaml`) | Optional metadata snapshots or config overrides | Machine-readable structure; easy for AAs to parse while remaining simple to edit. |
| JSONL (`.jsonl`) | Evidence logs, automated outputs (if needed) | Streams data-friendly for downstream tooling, consistent with existing log format. |
| SVG/PNG (sanitised) | Visual summaries if required | Only after review; kept minimal to avoid leaking details. |
| Plain text (`.txt`) | Rapid scratchpad (optional) | Temporary, later converted to Markdown for permanence. |

**Why Markdown as primary**: allows narrative, tables, and code snippets, integrates well with Git history, simplifies review and merge. YAML/JSONL serve as structured companions when automation or SoT integration is needed.

## Updated Assumptions
| ID | Assumption | Rationale | Validation Plan |
| --- | --- | --- | --- |
| A1 | Branch `brainstorm/gemini-collab-20251024` holds session artefacts. | Keeps brainstorm isolated and auditable. | Moderator creates branch, Gemini confirms checkout. |
| A2 | Ideas recorded as Markdown files with front matter. | Ensures consistent metadata + human readability. | First AA commit uses template, moderator spot-checks. |
| A3 | Optional YAML snapshot captures agreed decisions. | Allows automated ingestion later. | Create `brainstorm/.../decisions.yaml` after session wrap-up. |
| A4 | Evidence logs (if generated) stored as JSONL under `samples/` or session `evidence/`. | Aligns with existing log practices, easy automation. | Only add sanitized entries; moderator verifies before merge. |

## Potential Challenges & Mitigations
| Challenge | Impact | Mitigation |
| --- | --- | --- |
| Markdown conflicts when multiple AAs edit same README table | Slows iteration | Use short update windows, append rows carefully, consider splitting tables into per-AA files if conflicts persist. |
| YAML/JSON syntax errors | Breaks tooling | Run lint or quick validation (`python -c 'import yaml,...'`) before commit. |
| Sensitive content slipping into artefacts | Compliance risk | Sanitize script + moderator review + retrospective log when incident occurs. |

## Workflow Conventions Added
- Each session README now includes **Moderator Notes** section (for oversight comments without changing AA content).
- PR description template includes:
  ```markdown
  ## Checklist
  - [ ] sanitize run
  - [ ] pytest (if applicable)
  - [ ] decision table updated
  - [ ] retrospective drafted
  ## Decisions
  | Idea | Status | Notes |
  | --- | --- | --- |
  ```
- After merge, create `brainstorm/<topic>/decisions.yaml` summarising key accepted items.
- Use issue label `brainstorm-question` to track prompts outside the branch.

## Lessons Learned
### Successes
| Lesson | Artefact |
| --- | --- |
| L1: Markdown front matter keeps metadata consistent across agents. | `brainstorm/templates/session_readme_template.md`, idea files referencing template |
| L2: Branch isolation + README tables make audit trail clear for moderators. | Sample branch instructions in `docs/briefs/brainstorm_playbook.md` |

### Failures / Opportunities
| Lesson | Artefact |
| --- | --- |
| F1: Early sessions had mingled human/AA content, causing unclear ownership. Resolved by revising playbook to emphasise AA-led writing. | Git history prior to commit `88205fd` (docs: emphasise AA ownership...) |
| F2: Lacked assumptions/goals upfront; added `docs/briefs/brainstorm_lessons.md` to document hypotheses and mitigations. | Current file + README evidence bundle entry |

## Next Actions
1. Create branch `brainstorm/gemini-collab-20251024` with README scaffold using Markdown template.
2. Define decisions.yaml structure (YAML) for post-session summary.
3. Encourage AAs to log evidence or automation outputs using JSONL when available.
4. Review retro output and integrate into monthly executive summary.
