from __future__ import annotations

from enum import Enum


class FinishReason(str, Enum):
    """
    Indicates why the model stopped generating.
    """

    STOP = "stop"

    TOOL_CALLS = "tool_calls"

    LENGTH = "length"

    ERROR = "error"