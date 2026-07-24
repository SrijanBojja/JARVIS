"""
Status command for the JARVIS Operating System.
"""

from __future__ import annotations

from jarvis.commands import Command
from jarvis.kernel import Kernel


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
    ) -> None:
        """
        Execute the status command.
        """

        print()
        print("=" * 40)
        print("JARVIS STATUS")
        print("=" * 40)
        print()

        print(f"Running : {self._kernel.running}")
        print(f"Version : {self._kernel.version}")
        print(f"Started : {self._kernel.started_at}")