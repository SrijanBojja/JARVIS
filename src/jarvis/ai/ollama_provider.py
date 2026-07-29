"""
Ollama AI provider for JARVIS.
"""

from __future__ import annotations

from jarvis.ai.message import Message
from jarvis.ai.ollama_runtime import OllamaRuntime
from jarvis.ai.provider import AIProvider
from jarvis.responses import Response


class OllamaProvider(AIProvider):
    """
    AI provider backed by an Ollama runtime.
    """

    def __init__(
        self,
        runtime: OllamaRuntime | None = None,
    ) -> None:

        self._runtime = runtime or OllamaRuntime()

    def chat(
        self,
        messages: list[Message],
    ) -> Response:

        prompt = self._build_prompt(
            messages,
        )

        response = self._runtime.generate(
            prompt,
        )

        return Response(
            response,
        )

    @staticmethod
    def _build_prompt(
        messages: list[Message],
    ) -> str:
        """
        Convert chat messages into a prompt.
        """

        return "\n".join(
            f"{message.role}: {message.content}"
            for message in messages
        )