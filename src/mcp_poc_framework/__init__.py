"""
MCP PoC Operations Framework
============================

Skeleton package enabling multi-agent, multi-task orchestration with SSoT
controls. Components intentionally simplified for PoC showcase.
"""

from .config import FrameworkConfig  # noqa: F401
from .pipeline.executor import TaskOrchestrator  # noqa: F401
from .ssot.state_store import SSoTStateStore  # noqa: F401
