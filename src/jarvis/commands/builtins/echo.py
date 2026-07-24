"""
Echo command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.responses import Response


class EchoCommand(Command):
    """
    Echo the supplied text.
    """

    @property
    def name(self) -> str:
        return "echo"

    @property
    def description(self) -> str:
        return "Print the supplied text."

    def execute(
        self,
        args: list[str],
    ) -> Response:
        """
        Execute the echo command.
        """

        return Response(
            " ".join(args),
        )