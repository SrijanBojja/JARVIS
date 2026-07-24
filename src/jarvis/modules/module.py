"""
Base module definition for the JARVIS Operating System.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Module(ABC):
    """
    Abstract base class for all JARVIS modules.
    """

    @abstractmethod
    def initialize(self) -> None:
        """
        Initialize the module.
        """

    @abstractmethod
    def start(self) -> None:
        """
        Start the module.
        """

    @abstractmethod
    def stop(self) -> None:
        """
        Stop the module.
        """