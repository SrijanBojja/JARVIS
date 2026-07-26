"""
System action executor.
"""

from __future__ import annotations

import os

from jarvis.actions import (
    Action,
    ActionExecutor,
)
from jarvis.responses import (
    Response,
    ResponseStatus,
)


class SystemActionExecutor(ActionExecutor):
    """
    Executes Windows system actions.
    """

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
                os.system("shutdown /s /t 0")

            case "restart":
                os.system("shutdown /r /t 0")

            case "sleep":
                os.system(
                    "rundll32.exe powrprof.dll,SetSuspendState Sleep"
                )

            case "hibernate":
                os.system("shutdown /h")

            case "logout":
                os.system("shutdown /l")

        return Response(
            text=f"Executing {action.name}...",
            status=ResponseStatus.SUCCESS,
        )