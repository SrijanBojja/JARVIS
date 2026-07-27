from __future__ import annotations

from .workflow import Workflow
from .state import WorkflowState
from .exceptions import (
    InvalidWorkflowError,
    WorkflowCancelledError,
)


class WorkflowManager:
    """
    Registers and tracks workflows.

    This class does not execute workflows.
    It only manages their lifecycle.
    """

    def __init__(self) -> None:
        self._workflows: dict[str, Workflow] = {}

    def register(self, workflow: Workflow) -> None:
        if workflow.id in self._workflows:
            raise InvalidWorkflowError(
                f"Workflow '{workflow.id}' is already registered."
            )

        self._workflows[workflow.id] = workflow

    def get(self, workflow_id: str) -> Workflow:
        return self._workflows[workflow_id]

    def start(self, workflow_id: str) -> None:
        workflow = self.get(workflow_id)
        workflow.state = WorkflowState.RUNNING

    def complete(self, workflow_id: str) -> None:
        workflow = self.get(workflow_id)
        workflow.state = WorkflowState.COMPLETED

    def cancel(self, workflow_id: str) -> None:
        workflow = self.get(workflow_id)

        if workflow.finished:
            raise WorkflowCancelledError(
                "Workflow has already finished."
            )

        workflow.state = WorkflowState.CANCELLED

    def all(self) -> list[Workflow]:
        return list(self._workflows.values())