"""
Action execution engine.
"""

from __future__ import annotations

from jarvis.actions.action import Action
from jarvis.actions.executor import ActionExecutor
from jarvis.responses import Response
from jarvis.confirmation.manager import ConfirmationManager
from jarvis.confirmation.exceptions import PendingActionError

class ActionEngine:
    """
    Coordinates the execution of actions.
    """

    def __init__(
        self,
        confirmation: ConfirmationManager
    ) -> None:
        """
        Initialize the action engine.
        """
        self._confirmation = confirmation
        self._executors: list[ActionExecutor] = []

    def register(
        self,
        executor: ActionExecutor,
    ) -> None:
        """
        Register an action executor.
        """

        self._executors.append(
            executor,
        )

    def execute(
        self,
        action: Action,
    ) -> Response:
        """
        Execute an action.
        """

        for executor in self._executors:
            print(
                f"Checking executor: "
                f"{executor.__class__.__name__}"
            )
            if not executor.supports(action):
                continue

            if action.requires_confirmation:
                try:
                    self._confirmation.request(
                        title=action.name.title(),
                        message=f"Confirm '{action.name}' action.",
                        payload=action,
                    )

                    return Response(
                        text=f"Please confirm the '{action.name}' action.",
                    )

                except PendingActionError:
                    return Response(
                        text=(
                            "A confirmation is already pending.\n"
                            "Reply with 'yes' or 'no'."
                        ),
                    )

            return executor.execute(action)

        raise NotImplementedError(
            f"I don't know how to execute the '{action.name}' action yet."
        )

    def execute_pending(
        self,
    ) -> Response:
        """
        Execute the currently confirmed pending action.
        """

        action = self._confirmation.confirm()

        action = Action(
            name=action.name,
            target=action.target,
            requires_confirmation=False,
        )

        return self.execute(
            action,
        )

    @property
    def confirmation(self) -> ConfirmationManager:
        """
        Return the confirmation manager.
        """

        return self._confirmation