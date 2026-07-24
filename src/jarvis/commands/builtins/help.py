"""
Help command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command


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
    ) -> None:
        """
        Execute the help command.
        """

        print()
        print("=" * 40)
        print("Available Commands")
        print("=" * 40)
        print()

        for command in self._registry.commands():
            print(
                f"{command.name:<10} {command.description}"
            )