# Multi-Model Query Tool

Fan out a single prompt to multiple AI models in parallel and compare their responses.

## Status: 🐛 CRAWL Phase

| Phase | Status | Description |
|-------|--------|-------------|
| **Crawl** | 🟡 In Progress | Foundation — types, registry, CI/CD, docs |
| Walk | ⬜ Not Started | Engine — single-model execution, Bedrock, Ollama, fallback |
| Run | ⬜ Not Started | Production — full fan-out, slash command, hardening |

## Supported Models

| Model | Type | Subscription | Status |
|-------|------|-------------|--------|
| Claude Code | CLI | Anthropic Pro | ✅ Ready |
| Codex | CLI | ChatGPT Pro | ✅ Ready |
| Goose | CLI | Anthropic (shared) | ✅ Ready |
| Rovo Dev | CLI | Atlassian Rovo | ✅ Ready |
| Gemini | CLI | Google AI Pro | ⬜ Pending install |
| AWS Bedrock | API (boto3) | IAM | ✅ Ready |
| Ollama | Local (HTTP) | Free | ✅ Ready (qwen3:4b) |
| Perplexity | API fallback | Perplexity Pro | ⬜ API key only |

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

# Override Ollama model (default: qwen3:4b from llmfit)
python3 scripts/multi-model-query.py --ollama-model llama3.1:8b "Hello"

# Disable API key fallback
python3 scripts/multi-model-query.py --no-api-fallback "Hello"
```

## Development

```bash
make dev       # Install with dev dependencies
make lint      # Run ruff linter
make typecheck # Run mypy
make test      # Run pytest
make dry-run   # Quick availability check
```

## Architecture

- **Registry** (`src/multi_model_lib/registry.py`) — Model definitions + availability detection
- **Engine** (`src/multi_model_lib/engine.py`) — Async fan-out via `asyncio.gather()`
- **Fallback** (`src/multi_model_lib/fallback.py`) — API key fallback when CLI unavailable
- **Telemetry** (`src/multi_model_lib/telemetry.py`) — JSONL logging to `logs/agent_runs.jsonl`
- **CLI** (`scripts/multi-model-query.py`) — argparse entry point

## Specification

Full spec: [`cli-multi-model-query-plan.md`](../anuba/applications/YC-2026-summer/cli-multi-model-query-plan.md)

## License

MIT — Anuba Technologies
