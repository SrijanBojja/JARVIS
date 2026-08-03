"""
Windows mouse implementation.
"""

from __future__ import annotations

import pyautogui

from .exceptions import (
    MouseClickError,
    MouseMoveError,
)
from .service import MouseService


class WindowsMouseService(MouseService):

    def move(
        self,
        x: int,
        y: int,
    ) -> None:

        try:
            pyautogui.moveTo(
                x,
                y,
                duration=0.15,
            )

        except Exception as exc:
            raise MouseMoveError() from exc

    def click(
        self,
    ) -> None:

        try:
            pyautogui.click()

        except Exception as exc:
            raise MouseClickError() from exc

    def double_click(
        self,
    ) -> None:

        pyautogui.doubleClick()

    def right_click(
        self,
    ) -> None:

        pyautogui.rightClick()

    def scroll(
        self,
        amount: int,
    ) -> None:

        pyautogui.scroll(
            amount,
        )

    def position(
        self,
    ) -> tuple[int, int]:

        point = pyautogui.position()

        return (
            point.x,
            point.y,
        )