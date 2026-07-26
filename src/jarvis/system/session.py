"""
Session controller.
"""

from __future__ import annotations

import ctypes
import subprocess


class SessionController:
    """
    Controls the current Windows session.
    """

    def lock(self) -> None:
        ctypes.windll.user32.LockWorkStation()

    def close_application(
        self,
        process_name: str,
    ) -> None:
        subprocess.run(
            [
                "taskkill",
                "/IM",
                process_name,
                "/F",
            ],
            check=False,
        )

    def close_all_applications(self) -> None:
        raise NotImplementedError(
            "Close all applications is not implemented yet."
        )