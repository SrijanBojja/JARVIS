"""
Windows Desktop Controller.
"""

from __future__ import annotations

from jarvis.controllers.desktop.service import DesktopController

from jarvis.services.keyboard import KeyboardService
from jarvis.services.mouse import MouseService
from jarvis.services.perception import PerceptionService


class WindowsDesktopController(
    DesktopController,
):

    def __init__(
        self,
        mouse: MouseService,
        keyboard: KeyboardService,
        perception: PerceptionService,
    ) -> None:

        self._mouse = mouse
        self._keyboard = keyboard
        self._perception = perception

    def click(
        self,
        x: int,
        y: int,
    ) -> None:

        self._mouse.move(
            x,
            y,
        )

        self._mouse.click()

    def double_click(
        self,
        x: int,
        y: int,
    ) -> None:

        self._mouse.move(
            x,
            y,
        )

        self._mouse.double_click()

    def right_click(
        self,
        x: int,
        y: int,
    ) -> None:

        self._mouse.move(
            x,
            y,
        )

        self._mouse.right_click()

    def type_text(
        self,
        text: str,
    ) -> None:

        self._keyboard.type_text(
            text,
        )

    def press(
        self,
        key: str,
    ) -> None:

        self._keyboard.press(
            key,
        )

    def hotkey(
        self,
        *keys: str,
    ) -> None:

        self._keyboard.hotkey(
            *keys,
        )

    def scroll(
        self,
        amount: int,
    ) -> None:

        self._mouse.scroll(
            amount,
        )

    def screenshot(
        self,
    ) -> str:

        return str(
            self._perception.capture_screen(),
        )

    def cursor_position(
        self,
    ) -> tuple[int, int]:

        return self._mouse.position()