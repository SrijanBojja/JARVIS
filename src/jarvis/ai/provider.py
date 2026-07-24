"""
AI provider interface for JARVIS.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from jarvis.ai.message import Message
from jarvis.responses import Response


class AIProvider(ABC):
    """
    Base interface for AI providers.
    """

    @abstractmethod
    def chat(
        self,
        messages: list[Message],
    ) -> Response:
        """
        Generate a response from a conversation.
        """