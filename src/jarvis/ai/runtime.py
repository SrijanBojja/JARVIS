from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from jarvis.ai.message import Message
from jarvis.ai.models import ChatResponse


class AIRuntime(ABC):
    """
    Base interface for AI runtimes.
    """

    @abstractmethod
    def start(self) -> None:
        """
        Start the runtime.
        """

    @abstractmethod
    def stop(self) -> None:
        """
        Stop the runtime.
        """

    @abstractmethod
    def chat(
        self,
        messages: list[Message],
        tools: list[dict[str, Any]] | None = None,
    ) -> ChatResponse:
        """
        Execute a chat completion request.
        """