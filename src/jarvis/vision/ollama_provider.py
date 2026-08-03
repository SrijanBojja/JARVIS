"""
Ollama Vision provider.
"""

from __future__ import annotations

from .provider import VisionProvider
from .runtime import VisionRuntime


class OllamaVisionProvider(VisionProvider):
    """
    Vision provider backed by Ollama.
    """

    def __init__(
        self,
        runtime: VisionRuntime | None = None,
    ) -> None:

        self._runtime = runtime or VisionRuntime()

    def describe(
        self,
        image_path: str,
        prompt: str,
    ) -> str:

        return self._runtime.describe(
            image_path=image_path,
            prompt=prompt,
        )