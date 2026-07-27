"""
Notification action executor.
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
from jarvis.services.notification import NotificationService


class NotificationActionExecutor(ActionExecutor):
    """
    Executes notification actions.
    """

    def __init__(
        self,
        notification: NotificationService,
    ) -> None:
        self._notification = notification

    def supports(
        self,
        action: Action,
    ) -> bool:

        return action.name == "notify"

    def execute(
        self,
        action: Action,
    ) -> Response:

        self._notification.notify(
            title="JARVIS",
            message="Notification Service Working!",
        )

        return Response(
            text="Notification sent.",
            status=ResponseStatus.SUCCESS,
        )