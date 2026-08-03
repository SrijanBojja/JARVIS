from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class ToolCall:
    """
    Represents a tool invocation requested by the model.
    """

    id: str

    name: str

    arguments: dict[str, object] = field(
        default_factory=dict,
    )