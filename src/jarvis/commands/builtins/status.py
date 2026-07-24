"""
Status command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.kernel import Kernel
from jarvis.responses import Response


class StatusCommand(Command):
    """
    Display the current JARVIS status.
    """

    def __init__(
        self,
        kernel: Kernel,
    ) -> None:
        self._kernel = kernel

    @property
    def name(self) -> str:
        return "status"

    @property
    def description(self) -> str:
        return "Display the current JARVIS status."

    def execute(
        self,
        args: list[str],
    ) -> Response:
        """
        Execute the status command.
        """

        return Response(
            "\n"
            "========================================\n"
            "JARVIS STATUS\n"
            "========================================\n\n"
            f"Running : {self._kernel.running}\n"
            f"Version : {self._kernel.version}\n"
            f"Started : {self._kernel.started_at}"
        )