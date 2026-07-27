"""
Intent resolver.
"""

from __future__ import annotations

from jarvis.intents.intent import Intent
from jarvis.intents.registry import INTENTS


class IntentResolver:
    """
    Resolves the user's intent.
    """

    def resolve(
        self,
        command: str,
        args: list[str],
    ) -> Intent:
        """
        Resolve the user intent.
        """

        command = command.strip().lower()

        first_arg = ""

        if args:
            first_arg = args[0].strip().lower()

        # ---------- Open ----------
        if command in {
            "open",
            "launch",
            "start",
            "run",
        }:
            return Intent(
                name="open",
                confidence=1.0,
            )

        # ---------- Close ----------
        if command in {
            "close",
            "terminate",
        }:
            return Intent(
                name="close",
                confidence=1.0,
            )

        # ---------- Check ----------
        if (
            command == "is"
            and len(args) >= 2
            and args[-1].lower() in {
                "open",
                "running",
            }
        ):
            return Intent(
                name="check",
                confidence=1.0,
            )

        # ---------- Clipboard ----------
        if command == "clipboard":
            return Intent(
                name="clipboard_read",
                confidence=1.0,
            )

        if command in {
            "clear",
            "empty",
        } and first_arg == "clipboard":
            return Intent(
                name="clipboard_clear",
                confidence=1.0,
            )

        # ---------- Files ----------
        if command == "read" and first_arg == "file":
            return Intent(
                name="read_file",
                confidence=1.0,
            )

        if command == "write" and first_arg == "file":
            return Intent(
                name="write_file",
                confidence=1.0,
            )

        if command == "create" and first_arg == "directory":
            return Intent(
                name="create_directory",
                confidence=1.0,
            )

        if command == "list" and first_arg == "directory":
            return Intent(
                name="list_directory",
                confidence=1.0,
            )

        if command == "delete" and first_arg == "file":
            return Intent(
                name="delete_file",
                confidence=1.0,
            )

        if command == "delete" and first_arg == "directory":
            return Intent(
                name="delete_directory",
                confidence=1.0,
            )

        if command == "move" and first_arg == "file":
            return Intent(
                name="move_file",
                confidence=1.0,
            )

        # ---------- Notification ----------
        if command == "notify":
            return Intent(
                name="notify",
                confidence=1.0,
            )

        # ---------- Power ----------
        if command in {
            "shutdown",
            "restart",
            "sleep",
            "hibernate",
            "logout",
        }:
            return Intent(
                name=command,
                confidence=1.0,
            )

        return Intent(
            name=command,
            confidence=0.0,
        )