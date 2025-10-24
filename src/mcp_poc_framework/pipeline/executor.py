"""
Task orchestration primitives for the PoC framework.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence

from ..config import FrameworkConfig, TaskConfig
from ..ssot.state_store import SSoTStateStore
from ..tasks.scheduler import TaskAssignment
from ..agents.registry import AgentRegistry
from ..integrations.providers import build_provider_client


@dataclass
class OrchestratorContext:
    config: FrameworkConfig
    registry: AgentRegistry
    state_store: SSoTStateStore


class TaskOrchestrator:
    """Coordinates task execution across multiple AA providers."""

    def __init__(self, context: OrchestratorContext) -> None:
        self._ctx = context

    async def run_tasks(self, task_ids: Sequence[str], payloads: Iterable[Dict]) -> List[Dict]:
        results: List[Dict] = []
        for task_id, payload in zip(task_ids, payloads):
            result = await self._run_single(task_id, payload)
            results.append(result)
        return results

    async def _run_single(self, task_id: str, payload: Dict) -> Dict:
        task_config = self._resolve_task(task_id)
        assignment = TaskAssignment.from_task(task_config, self._ctx.registry)
        self._ctx.state_store.record_assignment(task_id, assignment.agent_id, payload)
        provider = self._ctx.config.provider_map()[assignment.provider]
        client = build_provider_client(provider)
        try:
            response = await client.invoke({"task": task_id, "payload": payload})
            self._ctx.state_store.record_result(task_id, response)
            return response
        finally:
            close = getattr(client, "aclose", None)
            if callable(close):
                await close()

    def _resolve_task(self, task_id: str) -> TaskConfig:
        for task in self._ctx.config.tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"Unknown task: {task_id}")
