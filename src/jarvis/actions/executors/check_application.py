"""
Application status executor.
"""

from __future__ import annotations

from jarvis.actions import (
    Action,
    ActionExecutor,
)
from jarvis.applications import (
    ApplicationLauncher,
)
from jarvis.applications.search import (
    ApplicationSearchEngine,
)
from jarvis.applications.store import (
    ApplicationStore,
)
from jarvis.responses import (
    Response,
    ResponseStatus,
)


class CheckApplicationExecutor(ActionExecutor):
    """
    Checks whether an application is running.
    """

    def __init__(
        self,
        search_engine: ApplicationSearchEngine,
        store: ApplicationStore,
        launcher: ApplicationLauncher,
    ) -> None:
        self._search_engine = search_engine
        self._store = store
        self._launcher = launcher

    def supports(
        self,
        action: Action,
    ) -> bool:
        return action.name == "check"

    def execute(
        self,
        action: Action,
    ) -> Response:

        target = (action.target or "").lower()

        result = self._search_engine.search(
            target,
            self._store,
        )

        if not result.has_match:
            return Response(
                text=f"I couldn't find '{target}'.",
                status=ResponseStatus.NOT_FOUND,
            )

        if result.is_ambiguous:

            names = [
                match.application.name
                for match in result.matches
            ]

            message = "I found multiple applications:\n\n"

            for index, name in enumerate(
                names,
                start=1,
            ):
                message += f"{index}. {name}\n"

            message += (
                "\nWhich one are you referring to?"
            )

            return Response(
                text=message,
                status=ResponseStatus.AMBIGUOUS,
                data=result.matches,
            )

        application = result.best_match.application

        running = self._launcher.is_running(
            application,
        )

        if running:
            return Response(
                text=f"{application.name} is currently running.",
                status=ResponseStatus.SUCCESS,
            )

        return Response(
            text=f"{application.name} is not running.",
            status=ResponseStatus.SUCCESS,
        )