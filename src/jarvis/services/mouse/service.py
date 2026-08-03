"""
Mouse service abstraction.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from jarvis.services import Service


class MouseService(Service, ABC):

    @abstractmethod
    def move(
        self,
        x: int,
        y: int,
    ) -> None:
        ...

    @abstractmethod
    def click(
        self,
    ) -> None:
        ...

    @abstractmethod
    def double_click(
        self,
    ) -> None:
        ...

    @abstractmethod
    def right_click(
        self,
    ) -> None:
        ...

    @abstractmethod
    def scroll(
        self,
        amount: int,
    ) -> None:
        ...

    @abstractmethod
    def position(
        self,
    ) -> tuple[int, int]:
        ...