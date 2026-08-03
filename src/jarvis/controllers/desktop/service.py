"""
Desktop controller abstraction.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class DesktopController(ABC):

    @abstractmethod
    def click(
        self,
        x: int,
        y: int,
    ) -> None:
        ...

    @abstractmethod
    def double_click(
        self,
        x: int,
        y: int,
    ) -> None:
        ...

    @abstractmethod
    def right_click(
        self,
        x: int,
        y: int,
    ) -> None:
        ...

    @abstractmethod
    def type_text(
        self,
        text: str,
    ) -> None:
        ...

    @abstractmethod
    def press(
        self,
        key: str,
    ) -> None:
        ...

    @abstractmethod
    def hotkey(
        self,
        *keys: str,
    ) -> None:
        ...

    @abstractmethod
    def scroll(
        self,
        amount: int,
    ) -> None:
        ...

    @abstractmethod
    def screenshot(
        self,
    ) -> str:
        ...

    @abstractmethod
    def cursor_position(
        self,
    ) -> tuple[int, int]:
        ...