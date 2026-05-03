#!/usr/bin/env python3
"""Multi-Model Query CLI — Fan out a prompt to multiple AI models."""

from __future__ import annotations

import argparse
import sys


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fan out a prompt to multiple AI models and compare responses.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("prompt", nargs="?", help="The prompt to send to all models")
    parser.add_argument("--prompt-file", help="Read prompt from a file")
    parser.add_argument("--models", help="Comma-separated list of models to query")
    parser.add_argument("--dry-run", action="store_true", help="Show what would run without executing")
    parser.add_argument("--json", action="store_true", help="Output raw JSON to stdout")
    parser.add_argument("--dedupe-providers", action="store_true", help="Skip duplicate providers")
    parser.add_argument("--ollama-model", default="qwen3:4b", help="Ollama model (default: qwen3:4b)")
    parser.add_argument("--bedrock-model", default="us.anthropic.claude-sonnet-4-20250514-v1:0", help="Bedrock model ID")
    parser.add_argument("--no-api-fallback", action="store_true", help="Disable API key fallback")
    parser.add_argument("--timeout", type=int, default=120, help="Per-model timeout in seconds")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("--output-dir", help="Override output directory")

    args = parser.parse_args()

    if not args.prompt and not args.prompt_file:
        parser.error("Provide a prompt as an argument or via --prompt-file")

    # TODO: Wire up engine in Walk phase
    print(f"[multi-model-query v0.1.0] Prompt: {args.prompt or '(from file)'}")
    print("[CRAWL PHASE] Engine not yet implemented. Use --dry-run to check model availability.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
