"""Data models for multi-model query results."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class ModelResult:
    """Result from a single model invocation."""

    name: str
    """Model identifier (e.g., 'claude', 'codex', 'rovo-dev', 'bedrock', 'ollama')."""

    provider: str
    """Provider identifier (e.g., 'anthropic-pro', 'chatgpt-pro', 'aws-bedrock')."""

    subscription: str
    """Human-readable subscription name."""

    status: str
    """One of: 'success', 'timeout', 'error', 'unavailable', 'fallback'."""

    invocation_method: str = "cli"
    """One of: 'cli', 'api-fallback', 'api', 'http'."""

    raw_output: str = ""
    """Raw stdout from the model."""

    parsed_response: str = ""
    """Extracted response text."""

    elapsed_seconds: float = 0.0
    """Wall-clock time for this model."""

    stderr: str = ""
    """Stderr output."""

    exit_code: int = -1
    """Process exit code."""

    def to_dict(self) -> dict[str, Any]:
        """Serialize to dictionary."""
        return asdict(self)

    def to_json(self) -> str:
        """Serialize to JSON string."""
        return json.dumps(self.to_dict(), indent=2)


@dataclass
class QueryResult:
    """Aggregate result from a multi-model fan-out query."""

    prompt: str
    """The input prompt."""

    timestamp: str
    """ISO 8601 timestamp."""

    session_id: str
    """Format: 'mmq-{date}-{time}'."""

    results: list[ModelResult] = field(default_factory=list)
    """Results from all invoked models."""

    total_elapsed_seconds: float = 0.0
    """Wall-clock time for the entire fan-out."""

    models_available: list[str] = field(default_factory=list)
    """Models detected as available."""

    models_invoked: list[str] = field(default_factory=list)
    """Models actually invoked."""

    models_unavailable: list[str] = field(default_factory=list)
    """Models not available."""

    models_fell_back: list[str] = field(default_factory=list)
    """Models that used API key fallback."""

    def to_dict(self) -> dict[str, Any]:
        """Serialize to dictionary."""
        return asdict(self)

    def to_json(self) -> str:
        """Serialize to JSON string."""
        return json.dumps(self.to_dict(), indent=2)
