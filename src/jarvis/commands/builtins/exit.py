"""
Exit command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.responses import Response


class ExitCommand(Command):
    """
    Exit the JARVIS shell.
    """

    @property
    def name(self) -> str:
        return "exit"

    @property
    def description(self) -> str:
        return "Exit the JARVIS shell."

    def execute(
        self,
        args: list[str],
    ) -> Response:
        """
        Execute the exit command.
        """

        raise SystemExit