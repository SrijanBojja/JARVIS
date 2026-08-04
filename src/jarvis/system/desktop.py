"""
Desktop-related operations for JARVIS.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


class DesktopController:
    """
    Controls desktop-related operations.
    """

    def open_application(
        self,
        application: str,
    ) -> bool:
        """
        Open a Windows application.
        """

        application = application.lower().strip()

        applications = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "paint": "mspaint.exe",
            "cmd": "cmd.exe",
            "powershell": "powershell.exe",
            "explorer": "explorer.exe",
        }

        executable = applications.get(application)

        if executable is None:
            return False

        subprocess.Popen(executable)

        return True

    def open_file(
        self,
        path: str,
    ) -> bool:
        """
        Open a file with its default application.
        """

        try:
            Path(path)

            subprocess.Popen(
                [
                    "cmd",
                    "/c",
                    "start",
                    "",
                    path,
                ],
                shell=True,
            )

            return True

        except Exception:
            return False