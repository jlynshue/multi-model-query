"""Configuration for multi-model query tool."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# Resolve repo root relative to this file: src/multi_model_lib/config.py -> repo root
REPO_ROOT = Path(__file__).resolve().parent.parent.parent


@dataclass
class MultiModelConfig:
    """Runtime configuration for the multi-model query engine."""

    timeout: int = 120
    """Per-model timeout in seconds."""

    models: list[str] | None = None
    """Specific models to invoke. None = all available."""

    output_dir: Path = field(default_factory=lambda: REPO_ROOT / "outputs" / "multi-model")
    """Directory for query output files."""

    log_dir: Path = field(default_factory=lambda: REPO_ROOT / "logs")
    """Directory for telemetry logs."""

    dedupe_providers: bool = False
    """Skip duplicate providers (e.g., skip Goose when Claude is available)."""

    verbose: bool = False
    """Enable verbose output."""

    dry_run: bool = False
    """Print commands without executing."""

    api_key_fallback: bool = True
    """Fall back to API keys if subscription CLI is unavailable."""

    ollama_model: str = "qwen3:4b"
    """Default Ollama model (llmfit recommended for M4/16GB)."""

    bedrock_model: str = "us.anthropic.claude-sonnet-4-20250514-v1:0"
    """Default AWS Bedrock model ID."""

    bedrock_region: str = "us-east-1"
    """AWS region for Bedrock."""
