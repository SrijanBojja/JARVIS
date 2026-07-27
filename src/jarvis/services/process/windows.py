"""
Windows process service.
"""

from __future__ import annotations
from pathlib import Path
import os
import subprocess

from .exceptions import (
    ProcessLaunchError,
    ProcessNotFoundError,
    ProcessTerminationError,
)
from .service import ProcessService


class WindowsProcessService(ProcessService):
    """
    Windows implementation of process operations.
    """

    def launch(self, target: str) -> None:
        """
        Launch an application, file, folder, or URL.
        """
        try:
            os.startfile(target)
        except OSError as exc:
            raise ProcessLaunchError(
                f"Unable to launch '{target}'."
            ) from exc

    def is_running(self, process_name: str) -> bool:
        """
        Return True if the process is running.
        """
        result = subprocess.run(
            ["tasklist"],
            capture_output=True,
            text=True,
            check=True,
        )

        return process_name.lower() in result.stdout.lower()

    def terminate(self, target: str) -> None:
        """
        Terminate a running application.
        """

        process_name = Path(target).name

        try:
            subprocess.run(
                [
                    "taskkill",
                    "/IM",
                    process_name,
                    "/F",
                ],
                check=True,
                capture_output=True,
                text=True,
            )

        except subprocess.CalledProcessError as exc:

            if "not found" in exc.stderr.lower():
                raise ProcessNotFoundError(
                    f"Process '{process_name}' is not running."
                ) from exc

            raise ProcessTerminationError(
                f"Unable to terminate '{process_name}'."
            ) from exc