#!/usr/bin/env bash
# Compare all available models on a single prompt (deduplicates providers)
python3 scripts/multi-model-query.py "Explain async/await in Python" --dedupe-providers
