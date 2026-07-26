"""
Base service abstraction.
"""

from __future__ import annotations

from abc import ABC


class Service(ABC):
    """
    Marker base class for all JARVIS services.
    """

    @property
    def name(self) -> str:
        return self.__class__.__name__