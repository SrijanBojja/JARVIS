"""
Windows window service.
"""

from __future__ import annotations

from pathlib import Path

import win32con
import win32gui
import win32process
import win32api
import time

from .exceptions import (
    WindowNotFoundError,
    WindowOperationError,
)
from .service import WindowService


class WindowsWindowService(WindowService):
    """
    Windows implementation of window operations.
    """

    def focus(
        self,
        target: str,
    ) -> None:
        hwnd = self._wait_for_window(target)

        try:
            if win32gui.IsIconic(hwnd):
                win32gui.ShowWindow(
                    hwnd,
                    win32con.SW_RESTORE,
                )
            else:
                win32gui.ShowWindow(
                    hwnd,
                    win32con.SW_SHOW,
                )

            foreground = win32gui.GetForegroundWindow()

            current_thread = win32api.GetCurrentThreadId()

            foreground_thread, _ = (
                win32process.GetWindowThreadProcessId(
                    foreground,
                )
            )

            target_thread, _ = (
                win32process.GetWindowThreadProcessId(
                    hwnd,
                )
            )

            if foreground_thread != target_thread:

                win32process.AttachThreadInput(
                    foreground_thread,
                    target_thread,
                    True,
                )

                try:
                    win32gui.SetForegroundWindow(hwnd)
                    win32gui.BringWindowToTop(hwnd)
                    win32gui.SetActiveWindow(hwnd)

                finally:
                    win32process.AttachThreadInput(
                        foreground_thread,
                        target_thread,
                        False,
                    )

            else:
                win32gui.SetForegroundWindow(hwnd)

        except Exception as exc:
            raise WindowOperationError(
                f"Unable to focus '{target}'."
            ) from exc

    def minimize(
        self,
        target: str,
    ) -> None:
        hwnd = self._wait_for_window(target)

        try:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

        except Exception as exc:
            raise WindowOperationError(
                f"Unable to minimize '{target}'."
            ) from exc

    def maximize(
        self,
        target: str,
    ) -> None:
        hwnd = self._wait_for_window(target)

        try:
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

        except Exception as exc:
            raise WindowOperationError(
                f"Unable to maximize '{target}'."
            ) from exc

    def restore(
        self,
        target: str,
    ) -> None:
        hwnd = self._wait_for_window(target)

        try:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        except Exception as exc:
            raise WindowOperationError(
                f"Unable to restore '{target}'."
            ) from exc

    def _wait_for_window(
        self,
        target: str,
        timeout: float = 5.0,
    ) -> int:
        """
        Wait until a window exists.
        """

        deadline = time.time() + timeout

        while time.time() < deadline:

            try:
                return self._find_window(
                    target,
                )

            except WindowNotFoundError:
                time.sleep(
                    0.1,
                )

        raise WindowNotFoundError(
            f"Window for '{target}' not found."
        )

    def _find_window(
        self,
        target: str,
    ) -> int:
        """
        Locate the application's main window.
        """

        process_name = Path(target).name.lower()

        window_handle = None

        def callback(hwnd, _) -> None:
            nonlocal window_handle

            if not win32gui.IsWindowVisible(hwnd):
                return

            _, pid = win32process.GetWindowThreadProcessId(hwnd)

            try:
                import subprocess

                result = subprocess.run(
                    [
                        "tasklist",
                        "/FI",
                        f"PID eq {pid}",
                        "/FO",
                        "CSV",
                        "/NH",
                    ],
                    capture_output=True,
                    text=True,
                    check=True,
                )

                if process_name in result.stdout.lower():
                    window_handle = hwnd

            except Exception:
                return

        win32gui.EnumWindows(callback, None)

        if window_handle is None:
            raise WindowNotFoundError(
                f"Window for '{target}' not found."
            )

        return window_handle