from __future__ import annotations

from dataclasses import dataclass, field

from .finish_reason import FinishReason
from .tool_call import ToolCall


@dataclass(frozen=True, slots=True)
class ChatResponse:
    """
    Structured response returned by an AI runtime.
    """

    text: str

    tool_calls: list[ToolCall] = field(
        default_factory=list,
    )

    finish_reason: FinishReason = (
        FinishReason.STOP
    )