# CI/CD Pipeline Standards

## Workflows

| Workflow | File | Trigger | Purpose |
|----------|------|---------|---------|
| CI | `ci.yml` | PR + push to main | Lint (ruff), type-check (mypy), test (pytest) |
| PII Scan | `pii-scan.yml` | PR | Scan for secrets/PII (future) |
| Agentic Gate | `agentic-gate.yml` | PR | AI-generated code quality (future) |

## CI Pipeline Details

**Matrix:** Python 3.11, 3.12, 3.13 on ubuntu-latest

**Steps:**
1. Checkout code
2. Set up Python
3. Install package with dev dependencies (`pip install -e ".[dev]"`)
4. Lint: `ruff check src/ tests/ scripts/`
5. Type check: `mypy src/`
6. Test: `pytest tests/ -v --tb=short`

## Local Development

```bash
make dev        # Install with dev deps in venv
make lint       # ruff check
make typecheck  # mypy
make test       # pytest
```

## Branch Strategy

- `main` — protected, requires passing CI
- Feature branches — `feat/<name>`, `fix/<name>`
- PRs required for all changes to main

## Release Process

1. All tests pass on main
2. Tag with `v<major>.<minor>.<patch>`
3. Push tag to trigger release workflow (future)
