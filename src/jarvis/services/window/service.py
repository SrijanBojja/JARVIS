"""
Window service contract.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from jarvis.services.base import Service


class WindowService(Service, ABC):
    """
    Defines window operations.
    """

    @abstractmethod
    def focus(
        self,
        target: str,
    ) -> None:
        """
        Bring a window to the foreground.
        """

    @abstractmethod
    def minimize(
        self,
        target: str,
    ) -> None:
        """
        Minimize a window.
        """

    @abstractmethod
    def maximize(
        self,
        target: str,
    ) -> None:
        """
        Maximize a window.
        """

    @abstractmethod
    def restore(
        self,
        target: str,
    ) -> None:
        """
        Restore a minimized or maximized window.
        """