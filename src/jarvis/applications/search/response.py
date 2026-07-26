"""
Application search response.
"""

from __future__ import annotations

from dataclasses import dataclass

from jarvis.applications.search.result import (
    ApplicationSearchResult,
)


@dataclass(slots=True, frozen=True)
class ApplicationSearchResponse:
    """
    Represents the outcome of an application search.
    """

    matches: list[ApplicationSearchResult]

    @property
    def has_match(
        self,
    ) -> bool:
        """
        Whether any application matched.
        """

        return bool(
            self.matches,
        )

    @property
    def best_match(
        self,
    ) -> ApplicationSearchResult | None:
        """
        Highest-ranked match.
        """

        if not self.matches:
            return None

        return self.matches[0]

    @property
    def is_ambiguous(
        self,
    ) -> bool:

        if len(self.matches) <= 1:
            return False

        names = {
            result.application.name.lower()
            for result in self.matches
        }

        return len(names) > 1