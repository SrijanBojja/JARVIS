"""
Application discovery service.
"""

from __future__ import annotations

from jarvis.applications.application import Application
from jarvis.applications.discovery.base import (
    ApplicationDiscoverySource,
)


class ApplicationDiscoveryService:
    """
    Coordinates application discovery sources.
    """

    def __init__(self) -> None:
        self._sources: list[ApplicationDiscoverySource] = []

    def register(
        self,
        source: ApplicationDiscoverySource,
    ) -> None:
        """
        Register a discovery source.
        """

        self._sources.append(
            source,
        )

    def discover(
        self,
    ) -> list[Application]:
        """
        Discover applications from all registered sources.
        """

        applications: list[Application] = []

        for source in self._sources:

            applications.extend(
                source.discover(),
            )

        return applications