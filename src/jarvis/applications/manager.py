"""
Application manager.
"""

from jarvis.applications import (
    ApplicationCache,
    ApplicationRegistry,
    ApplicationScanner,
)


class ApplicationManager:
    """
    Coordinates the application subsystem.
    """

    def __init__(
        self,
        registry: ApplicationRegistry,
        cache: ApplicationCache,
        scanner: ApplicationScanner,
    ) -> None:
        self._registry = registry
        self._cache = cache
        self._scanner = scanner

    def initialize(
        self,
    ) -> None:
        """
        Initialize the application subsystem.
        """

        self._registry.register_many(
            self._cache.load(),
        )

        discovered = self._scanner.scan()

        self._registry.register_many(
            discovered,
        )

        self._cache.save(
            self._registry.all(),
        )