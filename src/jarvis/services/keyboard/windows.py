"""
Windows keyboard implementation.
"""

from __future__ import annotations

import pyautogui

from .exceptions import (
    KeyboardPressError,
    KeyboardTypeError,
)
from .service import KeyboardService


class WindowsKeyboardService(KeyboardService):

    def type_text(
        self,
        text: str,
    ) -> None:

        try:
            pyautogui.write(
                text,
                interval=0.02,
            )

        except Exception as exc:
            raise KeyboardTypeError() from exc

    def press(
        self,
        key: str,
    ) -> None:

        try:
            pyautogui.press(
                key,
            )

        except Exception as exc:
            raise KeyboardPressError() from exc

    def hotkey(
        self,
        *keys: str,
    ) -> None:

        pyautogui.hotkey(
            *keys,
        )

    def key_down(
        self,
        key: str,
    ) -> None:

        pyautogui.keyDown(
            key,
        )

    def key_up(
        self,
        key: str,
    ) -> None:

        pyautogui.keyUp(
            key,
        )