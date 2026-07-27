"""
Builds executable actions.
"""

from jarvis.actions.action import Action
from jarvis.intents import Intent


class ActionBuilder:
    """
    Builds actions from intents.
    """

    def build(
        self,
        intent: Intent,
        args: list[str],
    ) -> Action | None:
        """
        Build an action from an intent.
        """

        if intent.name in {
            "open",
            "close",
            "check",
        }:
            if not args:
                return None

            return Action(
                name=intent.name,
                target=" ".join(args[:-1]) if intent.name == "check" else " ".join(args),
                requires_confirmation=False,
            )

        if intent.name in {
            "shutdown",
            "restart",
            "sleep",
            "hibernate",
            "logout",
            "notify"
        }:
            return Action(
                name=intent.name,
                requires_confirmation=True,
            )

        if intent.name == "clipboard_read":
            return Action(
                name="clipboard_read",
            )

        if intent.name == "clipboard_clear":
            return Action(
                name="clipboard_clear",
            )

        if intent.name in {
            "read_file",
            "write_file",
            "list_directory",
            "create_directory",
            "delete_file",
            "delete_directory",
            "move_file",
        }:

            filesystem_args = args

            if filesystem_args:
                first = filesystem_args[0].lower()

                if first in {
                    "file",
                    "directory",
                }:
                    filesystem_args = filesystem_args[1:]

            return Action(
                name=intent.name,
                target=" ".join(filesystem_args)
                if filesystem_args
                else None,
            )

        return None