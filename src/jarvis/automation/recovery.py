"""
Automation recovery.
"""

from __future__ import annotations

from jarvis.actions import Action
from jarvis.actions.engine import ActionEngine
from jarvis.responses import Response


class AutomationRecovery:
    """
    Attempts to recover from failed automation.
    """

    def __init__(
        self,
        action_engine: ActionEngine,
    ) -> None:

        self._action_engine = action_engine

    def recover(
        self,
        action: Action,
    ) -> Response | None:
        """
        Retry a failed action once.
        """

        print(
            f"[AUTOMATION RECOVERY] "
            f"Retrying {action.name}({action.target})..."
        )

        return self._action_engine.execute(
            action,
        )