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

        if intent.name == "open":
            if not args:
                return None

            return Action(
                name="open",
                target=" ".join(args),
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
            return Action(
                name=intent.name,
            )

        return None