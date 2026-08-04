"""
Hotkey executor.
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


class HotkeyExecutor(ActionExecutor):
    """
    Executes keyboard shortcuts.
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

        return action.name == "hotkey"

    def execute(
        self,
        action: Action,
    ) -> Response:

        keys = (
            action.target or ""
        ).split("+")

        self._keyboard.hotkey(
            *keys,
        )

        return Response(
            text=f"Pressed {'+'.join(keys)}.",
            status=ResponseStatus.SUCCESS,
        )