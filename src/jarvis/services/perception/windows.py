"""
Windows perception service.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
import tempfile

import psutil
import pyautogui
import win32gui

from jarvis.services.clipboard import ClipboardService

from .service import PerceptionService
from .state import PerceptionState


class WindowsPerceptionService(PerceptionService):
    """
    Windows implementation of desktop perception.
    """

    def __init__(
        self,
        clipboard: ClipboardService,
    ) -> None:
        self._clipboard = clipboard

    def capture_state(self) -> PerceptionState:
        """
        Capture the current desktop state.
        """

        screenshot = self.capture_screen()

        return PerceptionState(
            timestamp=datetime.now(),
            active_window=self.active_window(),
            clipboard=self.clipboard(),
            running_processes=self.running_processes(),
            screenshot=screenshot,
            windows=self.windows(),
        )

    def capture_screen(self) -> Path:
        """
        Capture the desktop.
        """

        image = pyautogui.screenshot()

        directory = (
            Path(tempfile.gettempdir())
            / "jarvis"
            / "screenshots"
        )

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = (
            datetime.now().strftime("%Y%m%d_%H%M%S")
            + ".png"
        )

        path = directory / filename

        image.save(path)

        return path

    def active_window(self) -> str:
        """
        Return the title of the foreground window.
        """

        hwnd = win32gui.GetForegroundWindow()

        return win32gui.GetWindowText(hwnd).strip()

    def clipboard(self) -> str:
        """
        Read clipboard text.
        """

        return self._clipboard.read_text()

    def running_processes(self) -> int:
        """
        Number of running processes.
        """

        return len(psutil.pids())

    def windows(self) -> list[str]:
        """
        Return titles of visible windows.
        """

        result: list[str] = []

        def callback(hwnd, _) -> None:

            if not win32gui.IsWindowVisible(hwnd):
                return

            title = win32gui.GetWindowText(hwnd).strip()

            if title:
                result.append(title)

        win32gui.EnumWindows(
            callback,
            None,
        )

        result.sort()

        return result