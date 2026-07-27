"""
Workflow runner.
"""

from __future__ import annotations

from jarvis.actions import ActionEngine
from jarvis.responses import Response, ResponseStatus

from .manager import WorkflowManager
from .result import WorkflowResult
from .state import WorkflowState
from .step_state import WorkflowStepState
from .workflow import Workflow


class WorkflowRunner:
    """
    Runs workflows one step at a time.
    """

    def __init__(
        self,
        workflow_manager: WorkflowManager,
        action_engine: ActionEngine,
    ) -> None:
        self._workflow_manager = workflow_manager
        self._action_engine = action_engine

    def has_pending_confirmation(self) -> bool:
        """
        Return whether a confirmation is pending.
        """

        return (
            self._action_engine.confirmation.has_pending()
        )

    def execute_pending(self) -> Response:
        """
        Execute the currently pending confirmed action.
        """

        return self._action_engine.execute_pending()

    def cancel_pending(self) -> None:
        """
        Cancel the pending confirmation.
        """

        self._action_engine.confirmation.cancel()

    def execute(
        self,
        workflow: Workflow,
    ) -> WorkflowResult:
        """
        Execute the supplied workflow.
        """

        self._workflow_manager.register(
            workflow,
        )

        self._workflow_manager.start(
            workflow.id,
        )

        responses: list[Response] = []

        for index, step in enumerate(
            workflow.steps,
        ):
            workflow.current_step = index

            step.state = WorkflowStepState.RUNNING

            response = self._action_engine.execute(
                step.action,
            )

            responses.append(
                response,
            )

            if (
                response.status
                != ResponseStatus.SUCCESS
            ):
                step.state = (
                    WorkflowStepState.FAILED
                )

                workflow.state = (
                    WorkflowState.FAILED
                )

                return WorkflowResult(
                    workflow_id=workflow.id,
                    status=WorkflowState.FAILED,
                    responses=responses,
                    completed_steps=index,
                    failed_step=index,
                )

            step.state = (
                WorkflowStepState.COMPLETED
            )



        self._workflow_manager.complete(
            workflow.id,
        )

        return WorkflowResult(
            workflow_id=workflow.id,
            status=WorkflowState.COMPLETED,
            responses=responses,
            completed_steps=len(
                workflow.steps,
            ),
            failed_step=None,
        )