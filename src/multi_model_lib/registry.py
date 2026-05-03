"""Model registry — single source of truth for all supported AI models."""

from __future__ import annotations

import shutil
import subprocess
from typing import Any

from multi_model_lib.config import MultiModelConfig

MODEL_REGISTRY: dict[str, dict[str, Any]] = {
    "claude": {
        "binary": "claude",
        "args_template": ["-p", "{prompt}", "--output-format", "json", "--bare"],
        "provider": "anthropic-pro",
        "subscription": "Anthropic Pro",
        "parse_mode": "json",
        "install_hint": "Already installed via Anthropic Pro subscription",
        "api_fallback": {
            "provider": "anthropic",
            "env_var": "ANTHROPIC_API_KEY",
            "endpoint": "https://api.anthropic.com/v1/messages",
            "method": "httpx",
            "default_model": "claude-sonnet-4-20250514",
        },
    },
    "codex": {
        "binary": "codex",
        "args_template": ["exec", "{prompt}"],
        "provider": "chatgpt-pro",
        "subscription": "ChatGPT Pro",
        "parse_mode": "text",
        "install_hint": "npm install -g @openai/codex",
        "api_fallback": {
            "provider": "openai",
            "env_var": "OPENAI_API_KEY",
            "endpoint": "https://api.openai.com/v1/chat/completions",
            "method": "httpx",
            "default_model": "gpt-4o",
        },
    },
    "goose": {
        "binary": "goose",
        "args_template": ["run", "-t", "{prompt}"],
        "provider": "anthropic-acp",
        "subscription": "Anthropic Pro (shared)",
        "parse_mode": "text",
        "install_hint": "pipx install goose-ai",
        "api_fallback": None,
    },
    "rovo-dev": {
        "binary": "rovo-dev",
        "args_template": ["chat", "--prompt", "{prompt}", "--non-interactive"],
        "provider": "atlassian-rovo",
        "subscription": "Atlassian Rovo",
        "parse_mode": "text",
        "install_hint": (
            "See https://support.atlassian.com/rovo/docs/"
            "install-and-run-rovo-dev-cli-on-your-device/"
        ),
        "api_fallback": None,
    },
    "gemini": {
        "binary": "gemini",
        "args_template": ["-p", "{prompt}"],
        "provider": "google-ai-pro",
        "subscription": "Google AI Pro",
        "parse_mode": "text",
        "install_hint": "npm install -g @anthropic-ai/gemini-cli  # verify actual package name",
        "api_fallback": {
            "provider": "google",
            "env_var": "GOOGLE_API_KEY",
            "endpoint": (
                "https://generativelanguage.googleapis.com/v1beta/"
                "models/{model}:generateContent"
            ),
            "method": "httpx",
            "default_model": "gemini-2.5-pro",
        },
    },
    "bedrock": {
        "binary": "aws",
        "args_template": None,
        "provider": "aws-bedrock",
        "subscription": "AWS IAM (pay-per-use or committed)",
        "parse_mode": "json",
        "install_hint": "aws configure  # IAM credentials must have bedrock:InvokeModel permission",
        "invocation_method": "boto3",
        "suggested_models": [
            "us.anthropic.claude-sonnet-4-20250514-v1:0",
            "us.anthropic.claude-opus-4-6-v1",
            "amazon.nova-pro-v1:0",
            "amazon.nova-lite-v1:0",
        ],
        "api_fallback": None,
    },
    "ollama": {
        "binary": "ollama",
        "args_template": ["run", "{model}", "{prompt}"],
        "provider": "ollama-local",
        "subscription": "Free / Local",
        "parse_mode": "text",
        "install_hint": "brew install ollama && ollama pull qwen3:4b",
        "invocation_method": "http",
        "http_endpoint": "http://localhost:11434/api/generate",
        "llmfit_recommended": {
            "model": "qwen3:4b",
            "score": 95.3,
            "speed_tok_s": 52.1,
            "ram_needed": "4 GB",
            "category": "Chat",
            "hardware": "Apple M4, 16 GB RAM",
        },
        "suggested_models": [
            "qwen3:4b",
            "qwen3:8b",
            "qwen2.5-coder:7b",
            "llama3.1:8b",
            "deepseek-coder-v2-lite",
        ],
        "api_fallback": None,
    },
}


def list_all_models() -> list[str]:
    """Return all registered model names."""
    return list(MODEL_REGISTRY.keys())


def get_registry_entry(name: str) -> dict[str, Any] | None:
    """Lookup a single model entry by name."""
    return MODEL_REGISTRY.get(name)


def _check_binary(binary: str) -> bool:
    """Check if a binary is available on PATH."""
    return shutil.which(binary) is not None


def _check_bedrock_access() -> bool:
    """Verify AWS credentials are configured for Bedrock access."""
    try:
        result = subprocess.run(
            ["aws", "sts", "get-caller-identity"],
            capture_output=True,
            timeout=10,
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def _check_ollama_running() -> bool:
    """Check if the Ollama server is running."""
    try:
        import httpx

        resp = httpx.get("http://localhost:11434/api/tags", timeout=5)
        return resp.status_code == 200
    except Exception:
        return False


def detect_available(config: MultiModelConfig) -> dict[str, dict[str, Any]]:
    """Detect which models are available on this system.

    Returns a subset of MODEL_REGISTRY with only available models.
    """
    available: dict[str, dict[str, Any]] = {}

    for name, entry in MODEL_REGISTRY.items():
        # Filter to requested models if specified
        if config.models and name not in config.models:
            continue

        binary = entry["binary"]

        if name == "bedrock":
            if _check_binary(binary) and _check_bedrock_access():
                available[name] = entry
        elif name == "ollama":
            if _check_binary(binary) and _check_ollama_running():
                available[name] = entry
        else:
            if _check_binary(binary):
                available[name] = entry

    return available
