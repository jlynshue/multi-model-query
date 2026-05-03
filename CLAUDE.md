# Multi-Model Query Tool — Claude Code Instructions

## Project Purpose
CLI tool that fans out a single prompt to 7+ AI models in parallel, collects responses, and presents a unified comparison.

## Key Files
- `src/multi_model_lib/` — Core Python package
- `scripts/multi-model-query.py` — CLI entry point
- `tests/` — Pytest test suite
- `docs/` — Architecture, CI/CD standards, crawl-walk-run phases

## Specification
Full spec at: `../anuba/applications/YC-2026-summer/cli-multi-model-query-plan.md`
Implementation plan at: `../../implementation_plan.md`

## Commands
```bash
make dev        # Install with dev deps
make test       # Run tests
make lint       # Run ruff
make dry-run    # Check model availability
```

## Conventions
- Python 3.11+, type-annotated, ruff-formatted
- Async engine using `asyncio.create_subprocess_exec` for CLI models
- `boto3` for Bedrock, `httpx` for Ollama and API fallback
- All outputs to `outputs/multi-model/`, telemetry to `logs/agent_runs.jsonl`
- Cost tracking: `cost_usd: 0` for subscription/local, estimated for Bedrock/API fallback
