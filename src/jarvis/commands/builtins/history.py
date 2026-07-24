"""
History command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
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
    ) -> None:
        print()
        print("=" * 40)
        print("COMMAND HISTORY")
        print("=" * 40)
        print()

        for index, command in enumerate(self._history.commands(), start=1):
            print(f"{index:>3}. {command}")