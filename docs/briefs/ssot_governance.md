# SSoT Governance Snapshot

## Core Principles
- **One true state** – every assignment/result flows through `SSoTStateStore`.
- **Evidence required** – public artefacts must cite their data source (e.g., `serialize()` dump).
- **No auto-sync** to production until Gate G3 approvals are complete.

## PoC Controls
- In-memory store exposes JSON exports for reporting.
- `.agents/logs/` provide backtrace from action → task → agent.
- Sanitize checklist ensures tokens/base URLs are not leaked.

## Upgrade Path
| Stage | Action | Evidence |
| --- | --- | --- |
| G1 | Export JSON snapshots to `memory/anchors/staged/` | Audit dump |
| G2 | Attach CI upload to secure storage | CI logs |
| G3 | Deploy durable SSoT (Postgres/Redis) with encryption at rest | Private architecture pack |

## Deviation Policy
- Log any deviation from the SSoT process in `.agents/backlog/conflicts.yaml` with `deviation.reason`.
