"""
Ollama AI provider for JARVIS.
"""

from __future__ import annotations

import httpx

from jarvis.ai.provider import AIProvider
from jarvis.ai.message import Message
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
        messages: list[Message],
    ) -> Response:

        try:
            response = httpx.post(
                f"{self._host}/api/chat",
                json={
                    "model": self._model,
                    "messages": [
                        {
                            "role": message.role,
                            "content": message.content,
                        }
                        for message in messages
                    ],
                    "stream": False,
                },
                timeout=120,
            )

            response.raise_for_status()

            data = response.json()

            return Response(
                data["message"]["content"].strip(),
            )

        except Exception as error:
            return Response(
                f"Ollama error: {error}"
            )