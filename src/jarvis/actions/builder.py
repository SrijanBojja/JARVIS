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

        if intent.name != "open":
            return None

        if not args:
            return None

        return Action(
            name="open",
            target=" ".join(args),
        )