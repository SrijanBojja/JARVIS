from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from .state import WorkflowState
from .step import WorkflowStep


@dataclass(slots=True)
class Workflow:
    """
    Represents a multi-step task executed by JARVIS.
    """

    name: str
    steps: list[WorkflowStep]

    id: str = field(default_factory=lambda: str(uuid4()))

    state: WorkflowState = WorkflowState.CREATED

    current_step: int = 0

    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def total_steps(self) -> int:
        return len(self.steps)

    @property
    def finished(self) -> bool:
        return self.state in (
            WorkflowState.COMPLETED,
            WorkflowState.CANCELLED,
            WorkflowState.FAILED,
        )