"""
Application index interface.
"""

from abc import ABC, abstractmethod

from jarvis.applications.application import Application


class ApplicationIndex(ABC):
    """
    Base class for all application indexes.
    """

    @abstractmethod
    def add(
        self,
        application: Application,
    ) -> None:
        """
        Add an application to the index.
        """

    @abstractmethod
    def remove(
        self,
        application: Application,
    ) -> None:
        """
        Remove an application from the index.
        """

    @abstractmethod
    def clear(
        self,
    ) -> None:
        """
        Remove all indexed applications.
        """