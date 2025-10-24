"""
Provider adapters for external AA platforms.

Each provider can map to HTTP APIs, message queues, or SDKs. The PoC keeps the
implementation minimal while showing extension points.
"""

from __future__ import annotations

from typing import Any, Dict, Protocol

import httpx

from ..config import ProviderConfig


class AgentAPIClient(Protocol):
    async def invoke(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        ...


class HttpAgentClient:
    """HTTP-based provider adapter using bearer token auth."""

    def __init__(self, config: ProviderConfig) -> None:
        self._config = config
        self._client = httpx.AsyncClient(base_url=config.base_url, timeout=30.0)

    async def invoke(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        token = _resolve_token(self._config.auth_token_env)
        response = await self._client.post(
            "/invoke",
            json=payload,
            headers={"Authorization": f"Bearer {token}"},
        )
        response.raise_for_status()
        return response.json()

    async def aclose(self) -> None:
        await self._client.aclose()


def build_provider_client(config: ProviderConfig) -> AgentAPIClient:
    # Placeholder: we only support HTTP in PoC but can extend here.
    return HttpAgentClient(config)


def _resolve_token(env_var: str) -> str:
    import os

    token = os.getenv(env_var)
    if not token:
        raise RuntimeError(
            f"Credential missing: set environment variable '{env_var}' before invoking provider.",
        )
    return token
