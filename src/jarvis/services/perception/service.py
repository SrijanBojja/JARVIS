"""
Perception service abstraction.
"""

from __future__ import annotations

from abc import abstractmethod

from jarvis.services.base import Service
from .state import PerceptionState


class PerceptionService(Service):
    """
    Base perception service.
    """

    @abstractmethod
    def capture_state(self) -> PerceptionState:
        """
        Capture the current desktop state.
        """
        raise NotImplementedError

    @abstractmethod
    def capture_screen(self):
        ...

    @abstractmethod
    def active_window(self):
        ...

    @abstractmethod
    def clipboard(self):
        ...

    @abstractmethod
    def running_processes(self):
        ...

    @abstractmethod
    def windows(self):
        ...