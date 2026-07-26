"""
Application search engine.
"""

from __future__ import annotations

from jarvis.applications.store import ApplicationStore
from jarvis.applications.search.matcher import (
    ApplicationMatcher,
)
from jarvis.applications.search.response import (
    ApplicationSearchResponse,
)
from jarvis.applications.search.result import (
    ApplicationSearchResult,
)


class ApplicationSearchEngine:
    """
    Coordinates application matchers.
    """

    def __init__(
        self,
    ) -> None:

        self._matchers: list[
            ApplicationMatcher
        ] = []

    def register(
        self,
        matcher: ApplicationMatcher,
    ) -> None:
        """
        Register a matcher.
        """

        self._matchers.append(
            matcher,
        )

    def search(
        self,
        query: str,
        store: ApplicationStore,
    ) -> ApplicationSearchResponse:
        """
        Search for matching applications.
        """

        applications = store.alias_index.find(
            query,
        )

        results: list[
            ApplicationSearchResult
        ] = []

        seen_targets: set[str] = set()

        for application in applications:

            if application.target in seen_targets:
                continue

            seen_targets.add(
                application.target,
            )

            for matcher in self._matchers:

                result = matcher.match(
                    query,
                    application,
                )

                if result is not None:

                    results.append(
                        result,
                    )

                    break

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return ApplicationSearchResponse(
            matches=results,
        )