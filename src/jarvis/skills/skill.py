"""
Base class for every JARVIS skill.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from jarvis.responses import Response


class Skill(ABC):
    """
    Base interface for every skill.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @property
    @abstractmethod
    def aliases(
        self,
    ) -> list[str]:
        ...

    @abstractmethod
    def execute(
        self,
        args: list[str],
    ) -> Response:
        ...