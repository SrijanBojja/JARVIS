"""
Application manager.
"""

from jarvis.applications import (
    ApplicationCache,
)
from jarvis.applications.discovery import (
    ApplicationDiscoveryService,
)
from jarvis.applications.store import (
    ApplicationStore,
)


class ApplicationManager:
    """
    Coordinates the application subsystem.
    """

    def __init__(
        self,
        store: ApplicationStore,
        cache: ApplicationCache,
        discovery: ApplicationDiscoveryService,
    ) -> None:
        self._store = store
        self._cache = cache
        self._discovery = discovery

    def initialize(
        self,
    ) -> None:
        """
        Initialize the application subsystem.
        """

        self._store.add_many(
            self._cache.load(),
        )

        discovered = self._discovery.discover()

        self._store.add_many(
            discovered,
        )

        self._cache.save(
            self._store.all(),
        )