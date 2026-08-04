"""
Mouse right-click executor.
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


class RightClickExecutor(ActionExecutor):
    """
    Executes a right mouse click.
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

        return action.name == "right_click"

    def execute(
        self,
        action: Action,
    ) -> Response:

        self._mouse.right_click()

        return Response(
            text="Right clicked.",
            status=ResponseStatus.SUCCESS,
        )