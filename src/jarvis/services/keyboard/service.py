"""
Keyboard service abstraction.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from jarvis.services import Service


class KeyboardService(Service, ABC):

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
    def key_down(
        self,
        key: str,
    ) -> None:
        ...

    @abstractmethod
    def key_up(
        self,
        key: str,
    ) -> None:
        ...