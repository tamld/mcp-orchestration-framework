# MCP Orchestration Framework – Architecture & Value Stream

## 1. Objectives
- Demonstrate how an MCP-style control plane can operate in a customer-facing PoC.
- Preserve confidential techniques by publishing strategy-level artefacts only.
- Prepare a foundation that can be promoted to a production product after validation.

## 2. Framework Architecture (high level)
```
+------------------+      +------------------+      +---------------------+
| Global MCP SSoT  | ---> | PoC Bootstrapper | ---> | Framework Core      |
+------------------+      +------------------+      +---------------------+
         |                          |                         |
         v                          v                         v
 +----------------------+   +------------------+   +-----------------------+
 | Policies & Templates |   | Task Contracts   |   | API Integrations (AA) |
 +----------------------+   +------------------+   +-----------------------+
                                                          |
                                                          v
                                               +--------------------------+
                                               | SSoT State Store (PoC)   |
                                               +--------------------------+
```

- **Framework Core** (`src/mcp_poc_framework/`):
  - `config.py` loads providers/agents/tasks from YAML.
  - `agents/registry.py` maps skills → agents → providers.
  - `pipeline/executor.py` orchestrates tasks and records results.
  - `tasks/scheduler.py` selects agents based on the skill matrix.
  - `integrations/providers.py` holds the HTTP adapter (extendable to other protocols).
  - `ssot/state_store.py` stores PoC assignments/results in memory and is ready to swap for persistent storage.
- **Policies & Templates**: inherit MCP guardrails to ensure artefacts include evidence.
- **Task Contracts**: `memory/templates/contract_template.md` + `configs/providers.example.yaml` set reproducible workflows.
- **Secure Channel**: reserved for Gate G3 (private repo with sensitive assets).

## 3. Value Stream
1. Capture customer requirement → record a scope contract in runtime `.agents/logs/` (gitignored, not committed).
2. Run bootstrap (LAW-REFLECT-001) → produce a ≤5 step plan.
3. Execute minimal changes and collect artefacts (`docs/`, `samples/`).
4. Gate review (G0→G2) verifies that the PoC outcomes match expectations.
5. Upon approval → migrate to a private repo and enable the secure channel.

## 4. Security & Sanitation
- `tools/sanitize_manifest.py` scans for emails, tokens, home paths.
- `docs/briefs/sanitize_checklist.md` guides manual review before publication.
- Artefacts replace confidential details with `REDACTED`.

## 5. Gate Roadmap
| Gate | Criteria | Evidence |
| --- | --- | --- |
| G0 | Repo skeleton + linkage to MCP | README, `.agent/AGENTS.md` |
| G1 | Mandatory artefacts + sanitize pass | `tech_fit.yaml`, `tests/PLAN.md` |
| G2 | End-to-end demo + customer-facing log | `samples/session_walkthrough.md` |
| G3 | Private deployment plan | Confidential delivery pack |

## 6. Risks & Mitigations
- **Confidential leakage** – always run the sanitize script and manual checklist → log evidence.
- **Scope drift** – README focuses on strategic modules; detailed code stays private.
- **Missing validation** – provide at least one sample workflow and agent log per gate.
