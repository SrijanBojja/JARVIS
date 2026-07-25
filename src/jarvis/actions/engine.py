"""
Action execution engine.
"""

from __future__ import annotations

from jarvis.actions.action import Action
from jarvis.actions.executor import ActionExecutor
from jarvis.responses import Response


class ActionEngine:
    """
    Coordinates the execution of actions.
    """

    def __init__(self) -> None:
        """
        Initialize the action engine.
        """

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
            if executor.supports(
                action,
            ):
                return executor.execute(
                    action,
                )
                

        raise NotImplementedError(
            f"I don't know how to execute the '{action.name}' action yet."
        )