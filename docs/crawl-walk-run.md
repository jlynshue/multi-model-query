# Crawl-Walk-Run Development Phases

## Phase 1: CRAWL — Foundation

**Goal:** Establish project structure, type system, model registry, CI/CD, and documentation.

**Deliverables:**
- [x] Repository scaffolding (pyproject.toml, Makefile, README, .gitignore)
- [x] Python package skeleton (src/multi_model_lib/)
- [x] ModelResult, QueryResult, MultiModelConfig dataclasses
- [x] MODEL_REGISTRY with 7 models + detect_available()
- [x] CI/CD pipelines (ci.yml)
- [x] Documentation (this file, ci-cd-standards, architecture)
- [x] 21 passing unit tests

**Acceptance Criteria:**
- `pytest tests/` — 21 tests pass
- `ruff check src/ tests/` — no lint errors
- `--dry-run` lists all registry entries with availability status
- CI passes on push to main

**Jira:** [PLACEHOLDER — AT-xxx: CRAWL phase foundation]
**Confluence:** [PLACEHOLDER — Multi-Model Query Tool PRD]

---

## Phase 2: WALK — Engine + Single-Model Execution

**Goal:** Implement the async fan-out engine, Bedrock/Ollama integrations, API fallback, CLI entry point, and telemetry.

**Deliverables:**
- [ ] engine.py — async fan-out with _invoke_cli, _invoke_bedrock, _invoke_ollama
- [ ] fallback.py — API key fallback logic
- [ ] telemetry.py — JSONL logging
- [ ] CLI entry point wired to engine
- [ ] Integration tests with mocked subprocesses

**Acceptance Criteria:**
- Single-model query works for each of: claude, codex, ollama, bedrock
- API key fallback activates when CLI binary is missing
- Outputs written to outputs/multi-model/
- Telemetry entries logged with cost_usd
- All CLI flags functional

**Jira:** [PLACEHOLDER — AT-xxx: WALK phase engine]
**Confluence:** [PLACEHOLDER — Update PRD with Walk phase]

---

## Phase 3: RUN — Full Fan-out + Production

**Goal:** Full parallel fan-out, rich output, slash command, production hardening.

**Deliverables:**
- [ ] Full parallel fan-out across all available models
- [ ] Rich console output with comparison table
- [ ] Markdown comparison report generation
- [ ] /multi-query slash command
- [ ] --dedupe-providers logic
- [ ] Self-evaluation ADR
- [ ] v1.0.0 release tag

**Acceptance Criteria:**
- Full fan-out completes in ~max(individual times), not sum
- --dedupe-providers correctly skips Goose when Claude is present
- Slash command works from Claude Code
- All 10 verification tests from the plan pass
- cost_usd: 0 for subscription/local, estimated for Bedrock/API fallback

**Jira:** [PLACEHOLDER — AT-xxx: RUN phase production]
**Confluence:** [PLACEHOLDER — Update PRD with Run phase completion]
