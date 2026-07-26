"""
Application search result.
"""

from __future__ import annotations

from dataclasses import dataclass

from jarvis.applications.application import Application


@dataclass(slots=True, frozen=True)
class ApplicationSearchResult:
    """
    Represents a ranked application search result.
    """

    application: Application
    score: int
    matched_text: str
    reason: str