"""
Application source index.
"""

from jarvis.applications.application import Application
from jarvis.applications.store.indexes.base import ApplicationIndex


class SourceIndex(ApplicationIndex):
    """
    Index applications by source.
    """

    def __init__(
        self,
    ) -> None:
        self._applications: dict[
            str,
            list[Application],
        ] = {}

    def add(
        self,
        application: Application,
    ) -> None:
        self._applications.setdefault(
            application.source,
            [],
        ).append(
            application,
        )

    def remove(
        self,
        application: Application,
    ) -> None:
        applications = self._applications.get(
            application.source,
        )

        if applications is None:
            return

        if application in applications:
            applications.remove(
                application,
            )

        if not applications:
            self._applications.pop(
                application.source,
                None,
            )

    def clear(
        self,
    ) -> None:
        self._applications.clear()

    def find(
        self,
        source: str,
    ) -> list[Application]:
        return list(
            self._applications.get(
                source,
                [],
            )
        )