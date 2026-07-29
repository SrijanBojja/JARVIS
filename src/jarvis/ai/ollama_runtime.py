"""
Ollama runtime for JARVIS.
"""

from __future__ import annotations

import httpx

from jarvis.ai.runtime import AIRuntime
from jarvis.config.settings import settings
from jarvis.ai.exceptions import AIRuntimeError


class OllamaRuntime(AIRuntime):
    """
    Runtime responsible for communicating with Ollama.
    """

    def __init__(
        self,
        host: str | None = None,
        model: str | None = None,
    ) -> None:

        self._host = host or settings.ai_host
        self._model = model or settings.ai_model

    def start(self) -> None:
        """
        Start the runtime.
        """

    def stop(self) -> None:
        """
        Stop the runtime.
        """

    def generate(
        self,
        prompt: str,
    ) -> str:

        try:
            response = httpx.post(
                f"{self._host}/api/generate",
                json={
                    "model": self._model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=120,
            )

            response.raise_for_status()

            data = response.json()

            return data["response"].strip()

        except Exception as error:
            raise AIRuntimeError(
                f"Failed to generate response from Ollama: {error}"
            ) from error