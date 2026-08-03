"""
Ollama AI provider for JARVIS.
"""

from __future__ import annotations

from typing import Any

from jarvis.ai.message import Message
from jarvis.ai.models import ChatResponse
from jarvis.ai.ollama_runtime import OllamaRuntime
from jarvis.ai.provider import AIProvider


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
        tools: list[dict[str, Any]] | None = None,
    ) -> ChatResponse:
        """
        Generate a chat response using Ollama.
        """

        return self._runtime.chat(
            messages=messages,
            tools=tools,
        )