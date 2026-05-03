.PHONY: install dev lint typecheck test dry-run query clean

install:
	pip install -e .

dev:
	pip install -e ".[dev]"

lint:
	ruff check src/ tests/ scripts/

typecheck:
	mypy src/

test:
	pytest tests/ -v --tb=short

dry-run:
	python3 scripts/multi-model-query.py --dry-run "test prompt"

query:
	python3 scripts/multi-model-query.py $(PROMPT)

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
