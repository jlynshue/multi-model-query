# AGENTS.md — Multi-Model Query Tool

## Project
Multi-model query CLI tool that fans out prompts to 7+ AI models in parallel.

## Rules
- Do NOT modify files outside `projects/active/multi-model-query/`
- All Python code must be type-annotated and pass `ruff check` and `mypy --strict`
- Follow the crawl-walk-run phases defined in `docs/crawl-walk-run.md`
- Spec is at `../anuba/applications/YC-2026-summer/cli-multi-model-query-plan.md`
- Outputs go to `outputs/multi-model/`, telemetry to `logs/agent_runs.jsonl`
- Secrets live in `.env` (never committed); template is `.env.example`
