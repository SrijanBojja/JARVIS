"""
Lifecycle service abstraction.
"""

from __future__ import annotations

from abc import abstractmethod

from .base import Service


class LifecycleService(Service):
    """
    Base class for services that require startup
    and shutdown management.
    """

    @abstractmethod
    def initialize(self) -> None:
        """
        Initialize the service.
        """

    @abstractmethod
    def shutdown(self) -> None:
        """
        Shut down the service.
        """