"""
Application name index.
"""

from jarvis.applications.application import Application
from jarvis.applications.store.indexes.base import ApplicationIndex


class NameIndex(ApplicationIndex):
    """
    Index applications by name.
    """

    def __init__(
        self,
    ) -> None:
        self._applications: dict[str, Application] = {}

    def add(
        self,
        application: Application,
    ) -> None:
        """
        Add an application to the index.
        """

        self._applications[
            application.name.lower()
        ] = application

    def remove(
        self,
        application: Application,
    ) -> None:
        """
        Remove an application from the index.
        """

        self._applications.pop(
            application.name.lower(),
            None,
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all indexed applications.
        """

        self._applications.clear()

    def find(
        self,
        name: str,
    ) -> Application | None:
        """
        Find an application by name.
        """

        return self._applications.get(
            name.lower(),
        )

    def all(
        self,
    ) -> list[Application]:
        """
        Return all indexed applications.
        """

        return list(
            self._applications.values(),
        )