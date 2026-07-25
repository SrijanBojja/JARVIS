"""
Application manager.
"""

from jarvis.applications import (
    ApplicationCache,
    ApplicationRegistry,
)
from jarvis.applications.discovery import (
    ApplicationDiscoveryService,
)


class ApplicationManager:
    """
    Coordinates the application subsystem.
    """

    def __init__(
        self,
        registry: ApplicationRegistry,
        cache: ApplicationCache,
        discovery: ApplicationDiscoveryService,
    ) -> None:
        self._registry = registry
        self._cache = cache
        self._discovery = discovery

    def initialize(
        self,
    ) -> None:
        """
        Initialize the application subsystem.
        """

        self._registry.register_many(
            self._cache.load(),
        )

        discovered = self._discovery.discover()

        self._registry.register_many(
            discovered,
        )

        self._cache.save(
            self._registry.all(),
        )