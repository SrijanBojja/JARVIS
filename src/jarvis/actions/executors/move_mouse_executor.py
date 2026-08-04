"""
Move mouse executor.
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


class MoveMouseExecutor(ActionExecutor):
    """
    Moves the mouse.
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

        return action.name == "move_mouse"

    def execute(
        self,
        action: Action,
    ) -> Response:

        target = action.target or ""

        x, y = map(
            int,
            target.split(),
        )

        self._mouse.move_to(
            x,
            y,
        )

        return Response(
            text=f"Moved mouse to ({x}, {y}).",
            status=ResponseStatus.SUCCESS,
        )