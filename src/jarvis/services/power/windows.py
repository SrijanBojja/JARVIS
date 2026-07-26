"""
Windows power service.
"""

from __future__ import annotations

import os

from .service import PowerService


class WindowsPowerService(PowerService):
    """
    Windows implementation of power operations.
    """

    def shutdown(self) -> None:
        os.system("shutdown /s /t 0")

    def restart(self) -> None:
        os.system("shutdown /r /t 0")

    def sleep(self) -> None:
        raise NotImplementedError(
            "Sleep is not yet implemented for Modern Standby (S0)."
        )

    def hibernate(self) -> None:
        os.system("shutdown /h")

    def logout(self) -> None:
        os.system("shutdown /l")