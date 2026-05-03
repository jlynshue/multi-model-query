Fan out a prompt to multiple AI models and compare responses. $ARGUMENTS

Run: `python3 scripts/multi-model-query.py --json $ARGUMENTS`

Parse the JSON output and present:
1. A comparison table (model, invocation method, response time, response summary)
2. Points of consensus across models
3. Unique insights from individual models
4. Any models that used API key fallback (and associated cost)
5. The full output file path for reference
