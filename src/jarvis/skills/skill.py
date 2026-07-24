"""
Base class for every JARVIS skill.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


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

    @abstractmethod
    def execute(
        self,
        args: list[str],
    ) -> None:
        ...