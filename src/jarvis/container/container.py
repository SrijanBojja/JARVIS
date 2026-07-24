"""
Service Container implementation.
"""

from __future__ import annotations

from typing import Any

from .exceptions import (
    ServiceAlreadyRegisteredError,
    ServiceNotFoundError,
)


class ServiceContainer:
    """
    Dependency Injection container for application services.
    """

    def __init__(self) -> None:
        self._services: dict[type[Any], Any] = {}

    def register(
        self,
        service_type: type[Any],
        instance: Any,
    ) -> None:
        """
        Register a singleton service.
        """

        if service_type in self._services:
            raise ServiceAlreadyRegisteredError(
                f"Service '{service_type.__name__}' is already registered."
            )

        self._services[service_type] = instance

    def resolve(
        self,
        service_type: type[Any],
    ) -> Any:
        """
        Resolve a registered singleton service.
        """

        if service_type not in self._services:
            raise ServiceNotFoundError(
                f"Service '{service_type.__name__}' is not registered."
            )

        return self._services[service_type]

    def has(
        self,
        service_type: type[Any],
    ) -> bool:
        """
        Check whether a service is registered.
        """

        return service_type in self._services