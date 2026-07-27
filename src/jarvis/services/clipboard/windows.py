"""
Windows clipboard implementation.
"""

from __future__ import annotations

import tkinter as tk

from .exceptions import (
    ClipboardClearError,
    ClipboardReadError,
    ClipboardWriteError,
)
from .service import ClipboardService


class WindowsClipboardService(ClipboardService):
    """
    Windows clipboard implementation using Tk.
    """

    def _root(self) -> tk.Tk:
        root = tk.Tk()
        root.withdraw()
        root.update()
        return root

    def read_text(self) -> str:
        try:
            root = self._root()

            try:
                return root.clipboard_get()

            except tk.TclError:
                # Clipboard is empty or doesn't contain text.
                return ""

            finally:
                root.destroy()

        except Exception as exc:
            raise ClipboardReadError(
                "Unable to read clipboard."
            ) from exc

    def write_text(self, text: str) -> None:
        try:
            root = self._root()

            try:
                root.clipboard_clear()
                root.clipboard_append(text)
                root.update()
            finally:
                root.destroy()

        except Exception as exc:
            raise ClipboardWriteError(
                "Unable to write clipboard."
            ) from exc

    def clear(self) -> None:
        try:
            root = self._root()

            try:
                root.clipboard_clear()
                root.update()
            finally:
                root.destroy()

        except Exception as exc:
            raise ClipboardClearError(
                "Unable to clear clipboard."
            ) from exc