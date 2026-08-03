"""
AI provider interface for JARVIS.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from jarvis.ai.message import Message
from jarvis.ai.models import ChatResponse


class AIProvider(ABC):
    """
    Base interface for AI providers.
    """

    @abstractmethod
    def chat(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]] | None = None,
    ) -> ChatResponse:
        """
        Generate a structured chat response.
        """