import sys
from pathlib import Path

for candidate in Path(__file__).resolve().parents:
    src_dir = candidate / "src"
    if (src_dir / 'mcp_poc_framework/__init__.py').exists():
        sys.path.insert(0, str(src_dir))
        break
else:
    raise RuntimeError('Cannot locate framework src directory for tests')

from mcp_poc_framework.config import FrameworkConfig  # noqa: E402
from mcp_poc_framework.agents.registry import AgentRegistry  # noqa: E402


def test_pick_agent_by_skill():
    cfg = FrameworkConfig.parse_obj({
        "providers": [
            {"name": "p1", "base_url": "https://example", "auth_token_env": "TOKEN"}
        ],
        "agents": [
            {"id": "agent_a", "provider": "p1", "skills": ["plan", "write"]},
            {"id": "agent_b", "provider": "p1", "skills": ["review"]},
        ],
        "tasks": [],
    })
    registry = AgentRegistry(cfg)
    agent = registry.pick_agent(["plan"])
    assert agent is not None
    assert agent.id == "agent_a"
