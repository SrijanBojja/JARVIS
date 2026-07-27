"""
Clipboard service contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from jarvis.services.base import Service


class ClipboardService(Service, ABC):
    """
    Clipboard abstraction.
    """

    @abstractmethod
    def read_text(self) -> str:
        """
        Read text from clipboard.
        """

    @abstractmethod
    def write_text(self, text: str) -> None:
        """
        Write text to clipboard.
        """

    @abstractmethod
    def clear(self) -> None:
        """
        Clear clipboard.
        """