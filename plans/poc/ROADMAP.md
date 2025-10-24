# PoC Roadmap – Gate-based

| Gate | Objective | Deliverables | Status |
| --- | --- | --- | --- |
| G0 | Repo skeleton aligned with MCP | README, `.agent/AGENTS.md`, contract template | In progress |
| G1 | Add mandatory artefacts + sanitize | `tech_fit.yaml`, `tests/PLAN.md`, sanitize script | Planned |
| G2 | Customer-facing demo story | `samples/session_walkthrough.md`, sample JSONL log | Planned |
| G3 | Transition to production engagement | Private delivery pack, production repo | Pending |

## Suggested Timeline
- 2025-10-24: Complete G0 deliverables.
- 2025-10-27: G1 review + security checklist sign-off.
- 2025-10-31: Run G2 demo with pilot customers.
- After customer agreement: move to G3 (private repo).

## Notes
- Log any scope extension in `.agents/backlog/conflicts.yaml` (local, gitignored).
- Gates open only after evidence is reflected in runtime logs; sanitized samples live in `samples/logs/`.
