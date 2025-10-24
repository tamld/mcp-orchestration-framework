"""
Agent registry supporting multi-provider AA orchestration.
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from ..config import AgentConfig, FrameworkConfig


class AgentRegistry:
    """Holds agent definitions and resolves capabilities across providers."""

    def __init__(self, config: FrameworkConfig) -> None:
        self._config = config
        self._agents: Dict[str, AgentConfig] = config.agent_map()

    def list_agents(self) -> List[AgentConfig]:
        return list(self._agents.values())

    def agents_with_skill(self, skill: str) -> List[AgentConfig]:
        return [agent for agent in self._agents.values() if skill in agent.skills]

    def pick_agent(self, skills: Iterable[str]) -> Optional[AgentConfig]:
        """Simple resolver for PoC: first agent matching all required skills."""
        required = set(skills)
        for agent in self._agents.values():
            if required.issubset(agent.skills):
                return agent
        return None

    def provider_for(self, agent_id: str) -> str:
        agent = self._agents.get(agent_id)
        if not agent:
            raise KeyError(f"Unknown agent id: {agent_id}")
        return agent.provider
