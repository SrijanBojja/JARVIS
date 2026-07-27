from jarvis.responses import Response, ResponseStatus
from jarvis.workflows import (
    WorkflowResult,
    WorkflowState,
)


def test_workflow_result_creation():

    result = WorkflowResult(
        workflow_id="workflow-1",
        status=WorkflowState.COMPLETED,
        responses=[
            Response(
                text="Opened Chrome.",
                status=ResponseStatus.SUCCESS,
            ),
        ],
        completed_steps=1,
    )

    assert result.workflow_id == "workflow-1"

    assert result.status == WorkflowState.COMPLETED

    assert result.completed_steps == 1

    assert result.failed_step is None

    assert len(result.responses) == 1

    assert result.responses[0].text == "Opened Chrome."