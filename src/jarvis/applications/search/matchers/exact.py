"""
Exact application matcher.
"""

from __future__ import annotations

from jarvis.applications.alias import (
    ApplicationAliasGenerator,
)
from jarvis.applications.application import (
    Application,
)
from jarvis.applications.search.matcher import (
    ApplicationMatcher,
)
from jarvis.applications.search.result import (
    ApplicationSearchResult,
)


class ExactMatchMatcher(ApplicationMatcher):
    """
    Performs exact application matching.
    """

    def __init__(
        self,
        alias_generator: ApplicationAliasGenerator,
    ) -> None:
        self._alias_generator = alias_generator

    def match(
        self,
        query: str,
        application: Application,
    ) -> ApplicationSearchResult | None:

        query = query.lower()

        aliases = self._alias_generator.generate(
            application,
        )

        if query not in aliases:
            return None

        score = (
            100
            if query == application.name.lower()
            else 95
        )

        reason = (
            "Exact name match"
            if score == 100
            else "Exact alias match"
        )

        return ApplicationSearchResult(
            application=application,
            score=score,
            matched_text=query,
            reason=reason,
        )