"""
Close application executor.
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
from jarvis.services.process.exceptions import (
    ProcessNotFoundError,
)



class CloseApplicationExecutor(ActionExecutor):
    """
    Closes desktop applications.
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
        return action.name == "close"

    def execute(
        self,
        action: Action,
    ) -> Response:

        target = (
            action.target or ""
        ).lower()

        response = self._search_engine.search(
            target,
            self._store,
        )

        if not response.has_match:
            return Response(
                text=f"I couldn't find '{target}'.",
                status=ResponseStatus.NOT_FOUND,
            )

        if response.is_ambiguous:

            names = [
                result.application.name
                for result in response.matches
            ]

            message = (
                "I found multiple applications:\n\n"
            )

            for index, name in enumerate(
                names,
                start=1,
            ):
                message += f"{index}. {name}\n"

            message += (
                "\nWhich one would you like to close?"
            )

            return Response(
                text=message,
                status=ResponseStatus.AMBIGUOUS,
                data=response.matches,
            )

        application = (
            response.best_match.application
        )

        try:
            self._launcher.close(
                application,
            )

        except ProcessNotFoundError:

            return Response(
                text=(
                    f"{application.name} "
                    "is not running."
                ),
                status=ResponseStatus.NOT_FOUND,
            )

        return Response(
            text=f"Closing {application.name}...",
            status=ResponseStatus.SUCCESS,
        )