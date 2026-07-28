"""
Base interface for speech engines.
"""

from abc import ABC, abstractmethod


class SpeechEngine(ABC):
    """
    Base class for all speech engines.
    """

    @abstractmethod
    def speak(
        self,
        text: str,
    ) -> None:
        """
        Speak the given text.
        """