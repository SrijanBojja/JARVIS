"""
Help command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.responses import Response


class HelpCommand(Command):
    """
    Display available commands.
    """

    def __init__(
        self,
        registry,
    ) -> None:
        self._registry = registry

    @property
    def name(self) -> str:
        return "help"

    @property
    def description(self) -> str:
        return "Display available commands."

    def execute(
        self,
        args: list[str],
    ) -> Response:
        """
        Execute the help command.
        """

        lines = [
            "",
            "========================================",
            "Available Commands",
            "========================================",
            "",
        ]

        for command in self._registry.commands():
            lines.append(
                f"{command.name:<10} {command.description}"
            )

        return Response("\n".join(lines))