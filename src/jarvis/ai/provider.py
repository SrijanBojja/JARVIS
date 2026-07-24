"""
AI provider interface for JARVIS.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from jarvis.responses import Response


class AIProvider(ABC):
    """
    Base interface for AI providers.
    """

    @abstractmethod
    def chat(
        self,
        message: str,
    ) -> Response:
        """
        Generate a response to the user's message.
        """