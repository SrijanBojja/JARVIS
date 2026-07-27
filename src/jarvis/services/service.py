"""
Base service abstraction.
"""

from __future__ import annotations

from abc import ABC


class Service(ABC):
    """
    Base class for all platform services.
    """

    @property
    def name(self) -> str:
        """
        Return the service name.
        """

        return self.__class__.__name__