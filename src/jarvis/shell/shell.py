"""
Interactive shell for the JARVIS Operating System.
"""

from jarvis.conversation import ConversationManager
from jarvis.utils import (
    CommandHistory,
    CommandParser,
)


class Shell:
    """
    Interactive command-line interface for JARVIS.
    """

    def __init__(
        self,
        conversation_manager: ConversationManager,
        history: CommandHistory,
    ) -> None:
        """
        Initialize the shell.
        """

        self._conversation_manager = conversation_manager
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

            if not text:
                continue

            self._history.add(text)

            command, args = self._parser.parse(text)

            try:
                response = self._conversation_manager.handle(
                    command,
                    args,
                )

                if response is not None:
                    print(response.text)

                else:
                    print(f"Unknown command: {command}")

            except SystemExit:
                print("Goodbye.")
                break