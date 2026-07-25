"""
Application registry.
"""

from jarvis.applications.application import Application


class ApplicationRegistry:
    """
    Stores known applications.
    """

    def __init__(
        self,
    ) -> None:
        self._applications: dict[str, Application] = {}

    def register(
        self,
        application: Application,
    ) -> None:
        """
        Register an application.
        """

        self._applications[
            application.name.lower()
        ] = application

    def register_many(
        self,
        applications: list[Application],
    ) -> None:
        """
        Register multiple applications.
        """

        for application in applications:
            self.register(
                application,
            )

    def find(
        self,
        name: str,
    ) -> Application | None:
        """
        Find an application.
        """

        return self._applications.get(
            name.lower(),
        )

    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove an application.
        """

        self._applications.pop(
            name.lower(),
            None,
        )

    def all(
        self,
    ) -> list[Application]:
        """
        Return all known applications.
        """

        return list(
            self._applications.values(),
        )