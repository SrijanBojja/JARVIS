"""
Open application executor.
"""

from __future__ import annotations

import subprocess

from jarvis.actions import (
    Action,
    ActionExecutor,
)
from jarvis.applications import (
    ApplicationLauncher,
    ApplicationRegistry,
)
from jarvis.responses import Response


class OpenApplicationExecutor(ActionExecutor):
    """
    Opens desktop applications.
    """

    def __init__(
        self,
        registry: ApplicationRegistry,
        launcher: ApplicationLauncher,
    ) -> None:
        """
        Initialize the executor.
        """

        self._registry = registry
        self._launcher = launcher

    def supports(
        self,
        action: Action,
    ) -> bool:
        return action.name == "open"

    def execute(
        self,
        action: Action,
    ) -> Response:

        target = (
            action.target or ""
        ).lower()

        application = self._registry.find(
            target,
        )

        if application is None:
            return Response(
                f"I couldn't find '{target}'."
            )

        self._launcher.launch(
            application,
        )

        return Response(
            f"Opening {application.name}..."
        )