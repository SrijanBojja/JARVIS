"""
Application registry.
"""

from jarvis.applications.alias import ApplicationAliasGenerator
from jarvis.applications.application import Application


class ApplicationRegistry:
    """
    Stores known applications.
    """

    def __init__(
    self,
        alias_generator: ApplicationAliasGenerator,
    ) -> None:
        self._applications: dict[str, Application] = {}
        self._aliases: dict[str, Application] = {}

        self._alias_generator = alias_generator

    def register(
        self,
        application: Application,
    ) -> None:
        """
        Register an application.
        """

        name = application.name.lower()

        self._applications[name] = application

        for alias in self._alias_generator.generate(
            application,
        ):
            self._aliases[alias] = application

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

        return self._aliases.get(
            name.lower(),
        )

    def remove(
        self,
        name: str,
    ) -> None:
        """
        Remove an application.
        """

        application = self.find(
            name,
        )

        if application is None:
            return

        self._applications.pop(
            application.name.lower(),
            None,
        )

        aliases = [
            alias
            for alias, value in self._aliases.items()
            if value is application
        ]

        for alias in aliases:
            self._aliases.pop(
                alias,
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