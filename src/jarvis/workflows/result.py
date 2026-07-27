"""
Workflow execution result.
"""

from __future__ import annotations

from dataclasses import dataclass

from jarvis.responses import Response

from .state import WorkflowState


@dataclass(slots=True)
class WorkflowResult:
    """
    Represents the result of executing a workflow.
    """

    workflow_id: str

    status: WorkflowState

    responses: list[Response]

    completed_steps: int

    failed_step: int | None = None