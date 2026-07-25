"""
Windows shortcut resolver.
"""

from __future__ import annotations

from pathlib import Path

import win32com.client


class ShortcutResolver:
    """
    Resolves Windows shortcut (.lnk) files.
    """

    def resolve(
        self,
        shortcut: Path,
    ) -> Path | None:
        """
        Resolve a shortcut to its target executable.
        """

        shell = win32com.client.Dispatch(
            "WScript.Shell",
        )

        shortcut_object = shell.CreateShortCut(
            str(shortcut),
        )

        target = Path(
            shortcut_object.Targetpath,
        )

        if not target.exists():
            return None

        return target