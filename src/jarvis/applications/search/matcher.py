"""
Application matcher interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from jarvis.applications.application import Application
from jarvis.applications.search.result import (
    ApplicationSearchResult,
)


class ApplicationMatcher(ABC):
    """
    Base class for application matchers.
    """

    @abstractmethod
    def match(
        self,
        query: str,
        application: Application,
    ) -> ApplicationSearchResult | None:
        """
        Try to match an application.
        """