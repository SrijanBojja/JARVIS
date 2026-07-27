from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from jarvis.actions import Action

from .step_state import WorkflowStepState


@dataclass(slots=True)
class WorkflowStep:
    """
    Represents a single executable step in a workflow.
    """

    name: str

    action: Action

    id: str = field(default_factory=lambda: str(uuid4()))

    state: WorkflowStepState = WorkflowStepState.PENDING

    metadata: dict[str, Any] = field(default_factory=dict)