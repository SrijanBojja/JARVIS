"""
Response status.
"""

from __future__ import annotations

from enum import Enum


class ResponseStatus(str, Enum):
    """
    Response status.
    """

    SUCCESS = "success"
    NOT_FOUND = "not_found"
    AMBIGUOUS = "ambiguous"
    FAILED = "failed"