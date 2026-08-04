"""
Type text executor.
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
from jarvis.services.desktop import KeyboardController


class TypeTextExecutor(ActionExecutor):
    """
    Types text into the active window.
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

        return action.name == "type"

    def execute(
        self,
        action: Action,
    ) -> Response:

        text = action.target or ""

        self._keyboard.type(
            text,
        )

        return Response(
            text=f"Typed: {text}",
            status=ResponseStatus.SUCCESS,
        )