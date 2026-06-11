"""Multi-model query library — fan out prompts to multiple AI models in parallel."""

__version__ = "0.1.0"

from multi_model_lib.config import MultiModelConfig
from multi_model_lib.engine import fan_out
from multi_model_lib.models import ModelResult, QueryResult
from multi_model_lib.registry import MODEL_REGISTRY, list_all_models

__all__ = [
    "MultiModelConfig",
    "ModelResult",
    "QueryResult",
    "fan_out",
    "list_all_models",
    "MODEL_REGISTRY",
    "__version__",
]
