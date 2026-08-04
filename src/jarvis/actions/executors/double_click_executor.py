"""
Mouse double-click executor.
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


class DoubleClickExecutor(ActionExecutor):
    """
    Executes a mouse double click.
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

        return action.name == "double_click"

    def execute(
        self,
        action: Action,
    ) -> Response:

        self._mouse.double_click()

        return Response(
            text="Double clicked.",
            status=ResponseStatus.SUCCESS,
        )