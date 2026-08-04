"""
Mouse click executor.
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
from jarvis.services.desktop import (
    MouseController,
)


class ClickExecutor(ActionExecutor):
    """
    Executes a left mouse click.
    """

    def __init__(
        self,
        mouse: MouseController,
    ) -> None:

        self._mouse = mouse

    def supports(
        self,
        action: Action,
    ) -> bool:

        return action.name == "click"

    def execute(
        self,
        action: Action,
    ) -> Response:

        self._mouse.click()

        return Response(
            text="Clicked.",
            status=ResponseStatus.SUCCESS,
        )