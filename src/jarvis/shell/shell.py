"""
Interactive shell for the JARVIS Operating System.
"""

from jarvis import commands
from jarvis.commands.module import CommandModule
from jarvis.commands.exceptions import CommandNotFoundError

class Shell:
    """
    Interactive command-line interface for JARVIS.
    """

    def __init__(
        self,
        command_module: CommandModule,
    ) -> None:
        self._command_module = command_module

    def run(self) -> None:
        """
        Run the interactive shell.
        """

        print()
        print("=" * 50)
        print("JARVIS SHELL")
        print("=" * 50)

        while True:
            command = input("JARVIS > ").strip()

            try:
                self._command_module.execute(command)

            except CommandNotFoundError:
                print(f"Unknown command: {command}")

            except SystemExit:
                break