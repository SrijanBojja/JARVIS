"""
Keyboard controller.
"""

from __future__ import annotations

import pyautogui


class KeyboardController:
    """
    Controls keyboard input.
    """

    def type(
        self,
        text: str,
        interval: float = 0.02,
    ) -> None:
        """
        Type text.
        """

        pyautogui.write(
            text,
            interval=interval,
        )

    def press(
        self,
        key: str,
    ) -> None:
        """
        Press a key.
        """

        pyautogui.press(
            key,
        )

    def hotkey(
        self,
        *keys: str,
    ) -> None:
        """
        Press a keyboard shortcut.
        """

        pyautogui.hotkey(
            *keys,
        )