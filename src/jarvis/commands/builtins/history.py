"""
History command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.responses import Response
from jarvis.utils import CommandHistory


class HistoryCommand(Command):
    """
    Display command history.
    """

    def __init__(
        self,
        history: CommandHistory,
    ) -> None:
        self._history = history

    @property
    def name(self) -> str:
        return "history"

    @property
    def description(self) -> str:
        return "Display command history."

    def execute(
        self,
        args: list[str],
    ) -> Response:
        lines = [
            "",
            "========================================",
            "COMMAND HISTORY",
            "========================================",
            "",
        ]

        for index, command in enumerate(
            self._history.commands(),
            start=1,
        ):
            lines.append(f"{index:>3}. {command}")

        return Response("\n".join(lines))