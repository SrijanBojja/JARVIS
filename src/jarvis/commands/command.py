"""
Base command definition for the JARVIS Operating System.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Command(ABC):
    """
    Abstract base class for all JARVIS commands.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Return the command name.
        """

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Return the command description.
        """

    @abstractmethod
    def execute(self) -> None:
        """
        Execute the command.
        """