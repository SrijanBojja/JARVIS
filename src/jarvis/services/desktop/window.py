"""
Window controller.
"""

from __future__ import annotations

import win32con
import win32gui


class WindowController:
    """
    Controls Windows application windows.
    """

    def active_window(
        self,
    ) -> str:

        hwnd = win32gui.GetForegroundWindow()

        return win32gui.GetWindowText(hwnd).strip()

    def minimize(
        self,
        hwnd: int,
    ) -> None:

        win32gui.ShowWindow(
            hwnd,
            win32con.SW_MINIMIZE,
        )

    def maximize(
        self,
        hwnd: int,
    ) -> None:

        win32gui.ShowWindow(
            hwnd,
            win32con.SW_MAXIMIZE,
        )

    def restore(
        self,
        hwnd: int,
    ) -> None:

        win32gui.ShowWindow(
            hwnd,
            win32con.SW_RESTORE,
        )

    def activate(
        self,
        hwnd: int,
    ) -> None:

        self.restore(hwnd)

        win32gui.SetForegroundWindow(
            hwnd,
        )

    def find(
        self,
        title: str,
    ) -> int | None:

        title = title.lower()

        result = None

        def callback(hwnd, _):

            nonlocal result

            if not win32gui.IsWindowVisible(hwnd):
                return

            window_title = (
                win32gui.GetWindowText(hwnd)
                .strip()
                .lower()
            )

            if title in window_title:
                result = hwnd

        win32gui.EnumWindows(
            callback,
            None,
        )

        return result