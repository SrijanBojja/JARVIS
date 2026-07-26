"""
Application store.
"""

from jarvis.applications.application import Application
from jarvis.applications.store.indexes import (
    AliasIndex,
    NameIndex,
    SourceIndex,
)


class ApplicationStore:
    """
    Stores all discovered applications.
    """

    def __init__(
        self,
        name_index: NameIndex,
        alias_index: AliasIndex,
        source_index: SourceIndex,
    ) -> None:
        self._applications: list[Application] = []

        self._name_index = name_index
        self._alias_index = alias_index
        self._source_index = source_index

    def add(
        self,
        application: Application,
    ) -> None:
        self._applications.append(
            application,
        )

        self._name_index.add(
            application,
        )

        self._alias_index.add(
            application,
        )

        self._source_index.add(
            application,
        )

    def add_many(
        self,
        applications: list[Application],
    ) -> None:
        for application in applications:
            self.add(
                application,
            )

    def remove(
        self,
        application: Application,
    ) -> None:
        if application in self._applications:
            self._applications.remove(
                application,
            )

        self._name_index.remove(
            application,
        )

        self._alias_index.remove(
            application,
        )

        self._source_index.remove(
            application,
        )

    def clear(
        self,
    ) -> None:
        self._applications.clear()

        self._name_index.clear()
        self._alias_index.clear()
        self._source_index.clear()

    @property
    def name_index(
        self,
    ) -> NameIndex:
        """
        Return the name index.
        """

        return self._name_index

    @property
    def alias_index(
        self,
    ) -> AliasIndex:
        """
        Return the alias index.
        """

        return self._alias_index

    @property
    def source_index(
        self,
    ) -> SourceIndex:
        """
        Return the source index.
        """

        return self._source_index

    def all(
        self,
    ) -> list[Application]:
        return list(
            self._applications,
        )