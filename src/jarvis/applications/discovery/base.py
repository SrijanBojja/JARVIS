"""
Base application discovery interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from jarvis.applications.application import Application


class ApplicationDiscoverySource(ABC):
    """
    Base class for all application discovery sources.
    """

    @abstractmethod
    def discover(
        self,
    ) -> list[Application]:
        """
        Discover available applications.
        """