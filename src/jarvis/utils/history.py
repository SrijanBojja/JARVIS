"""
Command history for the JARVIS shell.
"""

from __future__ import annotations


class CommandHistory:
    """
    Stores previously executed commands.
    """

    def __init__(self) -> None:
        self._history: list[str] = []

    def add(
        self,
        command: str,
    ) -> None:
        """
        Store a command.
        """

        self._history.append(command)

    def commands(self) -> list[str]:
        """
        Return all commands.
        """

        return self._history.copy()