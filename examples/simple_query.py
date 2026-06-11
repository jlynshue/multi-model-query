"""Minimal example: query multiple models in parallel."""

import asyncio

from multi_model_lib import MultiModelConfig, fan_out


async def main():
    config = MultiModelConfig(models=["claude", "ollama", "bedrock"])
    result = await fan_out("What is the CAP theorem?", config)

    print(f"Session: {result.session_id}")
    print(f"Total time: {result.total_elapsed_seconds}s\n")

    for r in result.results:
        preview = r.parsed_response[:100] if r.parsed_response else r.stderr
        print(f"[{r.name}] ({r.status}) {preview}...")


if __name__ == "__main__":
    asyncio.run(main())
