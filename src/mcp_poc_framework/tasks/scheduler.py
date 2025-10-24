"""
Simple task scheduling logic for the PoC framework.
"""

from __future__ import annotations

from dataclasses import dataclass

from ..agents.registry import AgentRegistry
from ..config import TaskConfig


@dataclass
class TaskAssignment:
    task_id: str
    agent_id: str
    provider: str

    @classmethod
    def from_task(cls, task: TaskConfig, registry: AgentRegistry) -> "TaskAssignment":
        agent = registry.pick_agent(task.required_skills)
        if not agent:
            raise RuntimeError(
                f"No agent available with required skills {task.required_skills} for task {task.id}",
            )
        return cls(task_id=task.id, agent_id=agent.id, provider=agent.provider)
