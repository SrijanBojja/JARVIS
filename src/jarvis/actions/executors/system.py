"""
System action executor.
"""

from __future__ import annotations

from jarvis.actions import (
    Action,
    ActionExecutor,
)
from jarvis.responses import (
    Response,
    ResponseStatus,
)
from jarvis.services.power.service import PowerService


class SystemActionExecutor(ActionExecutor):
    """
    Executes operating system power actions.
    """

    def __init__(
        self,
        power_service: PowerService,
    ) -> None:
        self._power_service = power_service

    def supports(
        self,
        action: Action,
    ) -> bool:
        return action.name in {
            "shutdown",
            "restart",
            "sleep",
            "hibernate",
            "logout",
        }

    def execute(
        self,
        action: Action,
    ) -> Response:

        match action.name:

            case "shutdown":
                self._power_service.shutdown()

            case "restart":
                self._power_service.restart()

            case "sleep":
                self._power_service.sleep()

            case "hibernate":
                self._power_service.hibernate()

            case "logout":
                self._power_service.logout()

        return Response(
            text=f"Executing {action.name}...",
            status=ResponseStatus.SUCCESS,
        )