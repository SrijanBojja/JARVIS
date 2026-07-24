"""
Command module for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands.builtins import (
    EchoCommand,
    ExitCommand,
    HelpCommand,
    StatusCommand,
    HistoryCommand,
    VersionCommand,
)
from jarvis.commands.command import Command
from jarvis.commands.registry import CommandRegistry
from jarvis.modules import Module
from jarvis.kernel import Kernel
from jarvis.utils import CommandHistory


class CommandModule(Module):
    """
    Manages the JARVIS command system.
    """

    def __init__(
        self,
        kernel: Kernel,
        history: CommandHistory,
    ) -> None:
        self.registry = CommandRegistry()
        self._kernel = kernel
        self._history = history

    @property
    def command_registry(self) -> CommandRegistry:
        """
        Return the command registry.
        """

        return self.registry

    def execute(
        self,
        name: str,
        args: list[str],
    ) -> None:
        """
        Execute a registered command.
        """

        command = self.command_registry.resolve(name)

        command.execute(args)


    def initialize(self) -> None:
        """
        Register built-in commands.
        """

        self.registry.register(
            VersionCommand(),
        )
        self.registry.register(
            EchoCommand(),
        )
        self.registry.register(
            HelpCommand(self.registry),
        )
        self.registry.register(
            StatusCommand(self._kernel),
        )
        self.registry.register(
            HistoryCommand(self._history),
        )
        self.registry.register(
            ExitCommand(),
        )

    def start(self) -> None:
        """
        Start the command module.
        """

        pass

    def stop(self) -> None:
        """
        Stop the command module.
        """

        pass