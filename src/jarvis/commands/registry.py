"""
Command registry for the JARVIS Operating System.
"""

from __future__ import annotations

from .command import Command
from .exceptions import CommandNotFoundError

class CommandRegistry:
    """
    Stores and resolves JARVIS commands.
    """

    def __init__(self) -> None:
        self._commands: dict[str, Command] = {}

    def register(
        self,
        command: Command,
    ) -> None:
        """
        Register a command.
        """

        self._commands[command.name] = command

    def resolve(
        self,
        name: str,
    ) -> Command:
        """
        Resolve a registered command.
        """

        if name not in self._commands:
            raise CommandNotFoundError(f"Command '{name}' is not registered.")

        return self._commands[name]
    
    def commands(self) -> list[Command]:
        """
        Return all registered commands.
        """

        return list(self._commands.values())