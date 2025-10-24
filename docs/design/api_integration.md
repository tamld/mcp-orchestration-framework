# API Integration Strategy

## Objectives
- Allow the PoC framework to connect to multiple external AA platforms through a consistent API surface.
- Keep operational data under SSoT control so every action remains traceable.

## Components
| Module | Role | Artefact |
| --- | --- | --- |
| `config.py` | Load providers/agents/tasks from YAML | `configs/providers.example.yaml` |
| `integrations/providers.py` | Token-based HTTP adapter | Placeholder `HttpAgentClient` |
| `pipeline/executor.py` | Coordinate multi-task workflows | `TaskOrchestrator` |
| `ssot/state_store.py` | Persist assignments/results for SSoT | `SSoTStateStore.serialize()` |

## Integration Flow
1. Load configuration → initialise `FrameworkConfig`.
2. Construct an `AgentRegistry` to map skills → providers.
3. For each task, `TaskOrchestrator` calls `TaskAssignment.from_task` to pick a matching agent.
4. `build_provider_client` instantiates an HTTP client using an environment token.
5. Responses are recorded in the SSoT for audit and downstream analytics.

## Edge Cases & Limitations
- PoC uses `httpx.AsyncClient`; production should add connection pooling and retries.
- Current SSoT is in-memory; upgrade to Redis/Postgres for durability.
- YAML config stores only environment variable references, not credentials.

## Multi-provider Support
- Add new adapters (WebSocket, gRPC, message bus) in `integrations/providers.py`.
- Each adapter must implement the `AgentAPIClient.invoke` protocol.
- Update `capabilities` in YAML to gate features per provider.

## Governance & Compliance
- SSoT records every assignment/result with UTC timestamps.
- Logs/artefacts should reference `serialize()` output; never publish raw customer data pre-G3.
- Always run the sanitize script before sharing sample configs publicly.
