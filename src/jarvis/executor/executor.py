"""
Plan executor.
"""

from __future__ import annotations

from jarvis.system.desktop import DesktopController
from jarvis.planner.plan import Plan
from jarvis.responses import Response


class Executor:
    """
    Executes planner actions.
    """

    def __init__(
        self,
        desktop: DesktopController,
    ) -> None:

        self._desktop = desktop

    def execute(
        self,
        plan: Plan,
    ) -> Response:

        for action in plan.actions:

            name, _, argument = action.partition(":")

            match name:

                case "open":

                    self._desktop.open_application(
                        argument,
                    )

                case _:

                    return Response(
                        text=f"Unknown action: {action}",
                    )

        return Response(
            text="Task completed.",
        )