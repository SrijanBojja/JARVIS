"""
AI runtime interface for JARVIS.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


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
    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate text from the model.
        """