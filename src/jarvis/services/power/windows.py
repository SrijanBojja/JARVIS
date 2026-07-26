"""
Windows power service.
"""

from __future__ import annotations

import subprocess

from .exceptions import (
    HibernateNotSupportedError,
    LogoutFailedError,
    RestartFailedError,
    ShutdownFailedError,
    SleepNotSupportedError,
)
from .service import PowerService


class WindowsPowerService(PowerService):
    """
    Windows implementation of power operations.
    """

    def shutdown(self) -> None:
        try:
            subprocess.run(
                ["shutdown", "/s", "/t", "0"],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            raise ShutdownFailedError(
                "Unable to shut down Windows."
            ) from exc

    def restart(self) -> None:
        try:
            subprocess.run(
                ["shutdown", "/r", "/t", "0"],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            raise RestartFailedError(
                "Unable to restart Windows."
            ) from exc

    def sleep(self) -> None:
        raise SleepNotSupportedError(
            "Modern Standby (S0) support will be implemented separately."
        )

    def hibernate(self) -> None:
        try:
            subprocess.run(
                ["shutdown", "/h"],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            raise HibernateNotSupportedError(
                "Unable to hibernate Windows."
            ) from exc

    def logout(self) -> None:
        try:
            subprocess.run(
                ["shutdown", "/l"],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            raise LogoutFailedError(
                "Unable to log out."
            ) from exc