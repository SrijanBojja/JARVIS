"""
Ollama AI provider for JARVIS.
"""

from __future__ import annotations

import httpx

from jarvis.ai import AIProvider
from jarvis.responses import Response


class OllamaProvider(AIProvider):
    """
    AI provider backed by Ollama.
    """

    def __init__(
        self,
        model: str = "qwen2.5:3b",
        host: str = "http://127.0.0.1:11434",
    ) -> None:
        self._model = model
        self._host = host

    def chat(
        self,
        message: str,
    ) -> Response:

        try:
            response = httpx.post(
                f"{self._host}/api/generate",
                json={
                    "model": self._model,
                    "prompt": message,
                    "stream": False,
                },
                timeout=120,
            )

            response.raise_for_status()

            data = response.json()

            return Response(
                data["response"].strip(),
            )

        except Exception as error:
            return Response(
                f"Ollama error: {error}"
            )