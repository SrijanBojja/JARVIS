"""
Application alias index.
"""

from jarvis.applications.alias import ApplicationAliasGenerator
from jarvis.applications.application import Application
from jarvis.applications.store.indexes.base import (
    ApplicationIndex,
)


class AliasIndex(ApplicationIndex):
    """
    Index applications by alias.
    """

    def __init__(
        self,
        alias_generator: ApplicationAliasGenerator,
    ) -> None:

        self._applications: dict[
            str,
            list[Application],
        ] = {}

        self._alias_generator = alias_generator

    def add(
        self,
        application: Application,
    ) -> None:
        """
        Add an application to the alias index.
        """

        for alias in self._alias_generator.generate(
            application,
        ):

            self._applications.setdefault(
                alias,
                [],
            ).append(
                application,
            )

    def remove(
        self,
        application: Application,
    ) -> None:
        """
        Remove an application from the alias index.
        """

        for applications in self._applications.values():

            if application in applications:

                applications.remove(
                    application,
                )

        empty_aliases = [
            alias
            for alias, applications
            in self._applications.items()
            if not applications
        ]

        for alias in empty_aliases:

            self._applications.pop(
                alias,
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
        alias: str,
    ) -> list[Application]:
        """
        Find all applications matching an alias.
        """

        return list(
            self._applications.get(
                alias.lower(),
                [],
            )
        )