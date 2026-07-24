"""
Exit command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command


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

    def execute(self) -> None:
        """
        Execute the exit command.
        """

        print("Goodbye.")

        raise SystemExit