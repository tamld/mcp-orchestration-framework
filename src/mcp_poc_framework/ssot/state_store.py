"""
Single Source of Truth (SSoT) store for PoC.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List, Optional


@dataclass
class AssignmentRecord:
    task_id: str
    agent_id: str
    payload_ref: Dict
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class ResultRecord:
    task_id: str
    data: Dict
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class SSoTStateStore:
    """
    Minimal in-memory store.

    In production this should persist to durable storage (e.g., PostgreSQL or
    object storage) with audit logs. For PoC, we keep records in memory and
    expose read APIs for presentation.
    """

    def __init__(self) -> None:
        self._assignments: List[AssignmentRecord] = []
        self._results: List[ResultRecord] = []

    def record_assignment(self, task_id: str, agent_id: str, payload: Dict) -> None:
        self._assignments.append(AssignmentRecord(task_id=task_id, agent_id=agent_id, payload_ref=payload))

    def record_result(self, task_id: str, data: Dict) -> None:
        self._results.append(ResultRecord(task_id=task_id, data=data))

    def latest_assignment(self, task_id: str) -> Optional[AssignmentRecord]:
        for record in reversed(self._assignments):
            if record.task_id == task_id:
                return record
        return None

    def latest_result(self, task_id: str) -> Optional[ResultRecord]:
        for record in reversed(self._results):
            if record.task_id == task_id:
                return record
        return None

    def serialize(self) -> Dict[str, List[Dict]]:
        return {
            "assignments": [record.__dict__ for record in self._assignments],
            "results": [record.__dict__ for record in self._results],
        }
