"""
Command parser for the JARVIS shell.
"""

from __future__ import annotations


class CommandParser:
    """
    Parses user input into command and arguments.
    """

    def parse(
        self,
        text: str,
    ) -> tuple[str, list[str]]:
        """
        Parse user input.

        Example:
            "echo hello world"

        Returns:
            ("echo", ["hello", "world"])
        """

        parts = text.strip().split()

        if not parts:
            return "", []

        return parts[0].lower(), parts[1:]