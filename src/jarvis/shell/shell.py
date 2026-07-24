"""
Interactive shell for the JARVIS Operating System.
"""

from jarvis import commands
from jarvis.commands.module import CommandModule
from jarvis.commands.exceptions import CommandNotFoundError
from jarvis.utils import (
    CommandParser,
    CommandHistory,
)


class Shell:
    """
    Interactive command-line interface for JARVIS.
    """

    def __init__(
        self,
        command_module: CommandModule,
        history: CommandHistory,
    ) -> None:
        self._command_module = command_module
        self._parser = CommandParser()
        self._history = history
    @property
    def history(self) -> CommandHistory:
        """
        Return the shell command history.
        """

        return self._history
        
    def run(self) -> None:
        """
        Run the interactive shell.
        """

        print()
        print("=" * 50)
        print("JARVIS SHELL")
        print("=" * 50)

        while True:
            text = input("JARVIS > ").strip()
            

            command, args = self._parser.parse(text)
            
            if not command:
                continue
            
            self._history.add(text)

            try:
                self._command_module.execute(command, args)

            except CommandNotFoundError:
                print(f"Unknown command: {command}")

            except SystemExit:
                break