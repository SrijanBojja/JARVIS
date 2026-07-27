"""
Clipboard action executor.
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
from jarvis.services.clipboard import ClipboardService


class ClipboardActionExecutor(ActionExecutor):
    """
    Executes clipboard actions.
    """

    def __init__(
        self,
        clipboard: ClipboardService,
    ) -> None:
        self._clipboard = clipboard

    def supports(
        self,
        action: Action,
    ) -> bool:
        return action.name in (
            "clipboard_read",
            "clipboard_clear",
        )

    def execute(
        self,
        action: Action,
    ) -> Response:

        if action.name == "clipboard_read":

            text = self._clipboard.read_text()

            if not text.strip():
                return Response(
                    text="Clipboard is empty.",
                    status=ResponseStatus.SUCCESS,
                )

            return Response(
                text=text,
                status=ResponseStatus.SUCCESS,
            )

        self._clipboard.clear()

        return Response(
            text="Clipboard cleared.",
            status=ResponseStatus.SUCCESS,
        )