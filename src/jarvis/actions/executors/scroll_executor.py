"""
Mouse scroll executor.
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


class ScrollExecutor(ActionExecutor):
    """
    Scrolls the mouse wheel.
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

        return action.name == "scroll"

    def execute(
        self,
        action: Action,
    ) -> Response:

        amount = int(action.target or "0")

        self._mouse.scroll(
            amount,
        )

        return Response(
            text=f"Scrolled {amount}.",
            status=ResponseStatus.SUCCESS,
        )