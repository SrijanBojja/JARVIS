"""
Press key executor.
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
    KeyboardController,
)


class PressKeyExecutor(ActionExecutor):
    """
    Presses a keyboard key.
    """

    def __init__(
        self,
        keyboard: KeyboardController,
    ) -> None:

        self._keyboard = keyboard

    def supports(
        self,
        action: Action,
    ) -> bool:

        return action.name == "press"

    def execute(
        self,
        action: Action,
    ) -> Response:

        key = action.target or ""

        self._keyboard.press(
            key,
        )

        return Response(
            text=f"Pressed {key}.",
            status=ResponseStatus.SUCCESS,
        )