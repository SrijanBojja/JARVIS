"""
Version command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.config import settings


class VersionCommand(Command):
    """
    Display the current JARVIS version.
    """

    @property
    def name(self) -> str:
        return "version"

    @property
    def description(self) -> str:
        return "Display the current JARVIS version."

    def execute(
        self,
        args: list[str],
    ) -> None:
        """
        Execute the version command.
        """

        print()
        print("JARVIS OS")
        print(f"Version: {settings.version}")