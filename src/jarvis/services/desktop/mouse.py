"""
Mouse controller.
"""

from __future__ import annotations

import pyautogui


class MouseController:
    """
    Controls the system mouse.
    """

    def move_to(
        self,
        x: int,
        y: int,
        duration: float = 0.2,
    ) -> None:
        """
        Move the mouse.
        """

        pyautogui.moveTo(
            x,
            y,
            duration=duration,
        )

    def click(
        self,
    ) -> None:
        """
        Left click.
        """

        pyautogui.click()

    def double_click(
        self,
    ) -> None:
        """
        Double click.
        """

        pyautogui.doubleClick()

    def right_click(
        self,
    ) -> None:
        """
        Right click.
        """

        pyautogui.rightClick()

    def scroll(
        self,
        amount: int,
    ) -> None:
        """
        Scroll vertically.
        """

        pyautogui.scroll(amount)

    def position(
        self,
    ) -> tuple[int, int]:
        """
        Current mouse position.
        """

        return pyautogui.position()