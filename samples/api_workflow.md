# Multi-Agent API Workflow (PoC)

## Preparation
```bash
export EXAMPLE_AA_TOKEN="REDACTED"
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Run the sample orchestrator
```python
import asyncio

from mcp_poc_framework.config import load_config
from mcp_poc_framework.agents.registry import AgentRegistry
from mcp_poc_framework.pipeline.executor import OrchestratorContext, TaskOrchestrator
from mcp_poc_framework.ssot.state_store import SSoTStateStore

cfg = load_config("configs/providers.example.yaml")
registry = AgentRegistry(cfg)
state_store = SSoTStateStore()
ctx = OrchestratorContext(config=cfg, registry=registry, state_store=state_store)

async def main():
    orchestrator = TaskOrchestrator(ctx)
    # Simulated payloads – do not include sensitive data
    results = await orchestrator.run_tasks([
        "discovery_brief",
        "sanitize_audit"
    ], [
        {"customer_prompt": "Summarise PoC requirement"},
        {"repo_path": "mcp-poc-operations"}
    ])
    print(results)
    print(state_store.serialize())

asyncio.run(main())
```

> Note: a real deployment would target the provider `/invoke` endpoint. The PoC never sends internal production data.
