# Multi-Model Query Tool

Fan out a single prompt to multiple AI models in parallel and compare their responses.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Async Engine](https://img.shields.io/badge/asyncio-native-green.svg)](https://docs.python.org/3/library/asyncio.html)

## Features

| Feature | Status | Details |
|---------|--------|---------|
| **CLI Model Support** | ✅ Ready | Claude Code, Codex, Goose, Rovo Dev |
| **API Backends** | ✅ Ready | AWS Bedrock, Ollama, Perplexity fallback |
| **Async Fan-Out** | ✅ Ready | Parallel execution with `asyncio.gather()` |
| **Telemetry** | ✅ Ready | JSONL logging to `logs/agent_runs.jsonl` |

## Supported Models

| Model | Type | Subscription |
|-------|------|-------------|
| Claude Code | CLI | Anthropic Pro |
| Codex | CLI | ChatGPT Pro |
| Goose | CLI | Anthropic (shared) |
| Rovo Dev | CLI | Atlassian Rovo |
| AWS Bedrock | API (boto3) | IAM |
| Ollama | Local (HTTP) | Free (qwen3:4b default) |
| Perplexity | API fallback | Perplexity Pro |

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Dry run — see what models are available
python3 scripts/multi-model-query.py --dry-run "test prompt"

# Query a single model
python3 scripts/multi-model-query.py --models claude "What is async/await?"

# Query all available models
python3 scripts/multi-model-query.py "Explain event sourcing in 2 sentences"

# Override Ollama model (default: qwen3:4b)
python3 scripts/multi-model-query.py --ollama-model llama3.1:8b "Hello"

# Disable API key fallback
python3 scripts/multi-model-query.py --no-api-fallback "Hello"
```

## Architecture

- **Registry** (`src/multi_model_lib/registry.py`) — Model definitions + availability detection
- **Engine** (`src/multi_model_lib/engine.py`) — Async fan-out via `asyncio.gather()`
- **Fallback** (`src/multi_model_lib/fallback.py`) — API key fallback when CLI unavailable
- **Telemetry** (`src/multi_model_lib/telemetry.py`) — JSONL logging to `logs/agent_runs.jsonl`
- **CLI** (`scripts/multi-model-query.py`) — argparse entry point

## Development

```bash
make dev       # Install with dev dependencies
make lint      # Run ruff linter
make typecheck # Run mypy
make test      # Run pytest
make dry-run   # Quick availability check
```

## Author

[Jonathan Lyn-Shue](https://jonathanlynshue.com) — Fractional CIO/CTO | Data & AI Executive

## License

MIT — Anuba Technologies
