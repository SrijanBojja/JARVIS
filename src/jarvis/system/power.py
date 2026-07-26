"""
Power controller.
"""

from __future__ import annotations

import subprocess


class PowerController:
    """
    Controls Windows power operations.
    """

    def shutdown(self) -> None:
        subprocess.run(
            ["shutdown", "/s", "/t", "0"],
            check=False,
        )

    def restart(self) -> None:
        subprocess.run(
            ["shutdown", "/r", "/t", "0"],
            check=False,
        )

    def logout(self) -> None:
        subprocess.run(
            ["shutdown", "/l"],
            check=False,
        )

    def sleep(self) -> None:
        subprocess.run(
            [
                "rundll32.exe",
                "powrprof.dll,SetSuspendState",
                "0,1,0",
            ],
            check=False,
        )

    def hibernate(self) -> None:
        subprocess.run(
            [
                "shutdown",
                "/h",
            ],
            check=False,
        )