"""
Echo action executor.
"""

from jarvis.actions import (
    Action,
    ActionExecutor,
)
from jarvis.responses import Response


class EchoActionExecutor(ActionExecutor):
    """
    Executes echo actions.
    """

    def supports(
        self,
        action: Action,
    ) -> bool:
        """
        Return whether this executor supports the action.
        """

        return action.name == "echo"

    def execute(
        self,
        action: Action,
    ) -> Response:
        """
        Execute the action.
        """

        return Response(
            action.target,
        )