"""
Application model.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Application:
    """
    Represents an installed application.
    """

    name: str
    executable: str
    source: str = "unknown"