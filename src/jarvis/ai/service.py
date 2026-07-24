"""
AI service for JARVIS.
"""

from __future__ import annotations

from jarvis.ai import AIProvider
from jarvis.responses import Response


class AIService:
    """
    High-level AI service.
    """

    def __init__(
        self,
        provider: AIProvider,
    ) -> None:
        self._provider = provider

    @property
    def provider(self) -> AIProvider:
        """
        Return the active AI provider.
        """

        return self._provider

    def chat(
        self,
        message: str,
    ) -> Response:
        """
        Generate an AI response.
        """

        return self._provider.chat(message)