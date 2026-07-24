"""
AI service for JARVIS.
"""

from __future__ import annotations

from jarvis.ai.memory import ConversationMemory
from jarvis.ai.message import Message
from jarvis.ai.prompts import SYSTEM_PROMPT
from jarvis.ai.provider import AIProvider
from jarvis.responses import Response


class AIService:
    """
    High-level AI service.
    """

    def __init__(
        self,
        provider: AIProvider,
        memory: ConversationMemory,
    ) -> None:

        self._provider = provider
        self._memory = memory

    @property
    def provider(
        self,
    ) -> AIProvider:
        return self._provider

    def chat(
        self,
        message: str,
    ) -> Response:

        self._memory.add_user_message(
            message,
        )

        messages = [
            Message(
                role="system",
                content=SYSTEM_PROMPT,
            ),
            *self._memory.messages(),
        ]

        response = self._provider.chat(
            messages,
        )

        self._memory.add_assistant_message(
            response.text,
        )

        return response