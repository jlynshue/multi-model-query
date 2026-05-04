"""Multi-Model Query Library — Fan out prompts to multiple AI models."""

__version__ = "0.1.0"

from multi_model_lib.config import MultiModelConfig
from multi_model_lib.models import ModelResult, QueryResult

__all__ = ["MultiModelConfig", "ModelResult", "QueryResult", "__version__"]
