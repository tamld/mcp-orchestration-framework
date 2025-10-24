"""
Config primitives for the PoC framework.

The configuration is designed to be API-agnostic so that external AA platforms
can be plugged in via provider adapters. Pydantic is optional but available for
schema validation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from pydantic import BaseModel, Field, validator


class ProviderConfig(BaseModel):
    """Defines external AA provider endpoints."""

    name: str
    base_url: str = Field(..., description="Public URL for the provider API")
    auth_token_env: str = Field(
        ...,
        description="Environment variable name containing credential/token",
    )
    capabilities: List[str] = Field(default_factory=list)


class AgentConfig(BaseModel):
    """Represents an Agent role registered in the framework."""

    id: str
    provider: str
    skills: List[str]
    metadata: Dict[str, Any] = Field(default_factory=dict)

    @validator("id")
    def validate_identifier(cls, value: str) -> str:  # noqa: D401
        if not value or " " in value:
            raise ValueError("Agent id must be non-empty and use snake-case.")
        return value


class TaskConfig(BaseModel):
    """Defines a reusable task template orchestrated by the PoC framework."""

    id: str
    description: str
    required_skills: List[str] = Field(default_factory=list)
    sla_minutes: int = Field(default=15, ge=1)


class FrameworkConfig(BaseModel):
    """Top-level configuration loaded from YAML."""

    providers: List[ProviderConfig]
    agents: List[AgentConfig]
    tasks: List[TaskConfig]
    ssot_bucket: str = Field(
        default="local",
        description="Identifier for SSoT storage target (local, redis, etc.)",
    )

    def provider_map(self) -> Dict[str, ProviderConfig]:
        return {p.name: p for p in self.providers}

    def agent_map(self) -> Dict[str, AgentConfig]:
        return {a.id: a for a in self.agents}

    @classmethod
    def load(cls, path: Path) -> "FrameworkConfig":
        data = yaml.safe_load(path.read_text()) or {}
        return cls.parse_obj(data)

    def to_dict(self) -> Dict[str, Any]:
        return self.dict()


def load_config(path: str | Path, overrides: Optional[Dict[str, Any]] = None) -> FrameworkConfig:
    """Helper to load and optionally override config at runtime."""
    cfg = FrameworkConfig.load(Path(path))
    if overrides:
        merged = cfg.to_dict()
        merged.update(overrides)
        return FrameworkConfig.parse_obj(merged)
    return cfg
