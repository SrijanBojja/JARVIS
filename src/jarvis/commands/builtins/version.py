"""
Version command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.config import settings
from jarvis.responses import Response


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
    ) -> Response:
        """
        Execute the version command.
        """

        return Response(
            "\n"
            "JARVIS OS\n"
            f"Version: {settings.version}"
        )