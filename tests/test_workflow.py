from jarvis.workflows.workflow import Workflow
from jarvis.workflows.state import WorkflowState


def test_workflow_creation():
    workflow = Workflow(
        name="Test Workflow",
        steps=["step1", "step2"],
    )

    assert workflow.name == "Test Workflow"
    assert workflow.total_steps == 2
    assert workflow.current_step == 0
    assert workflow.state == WorkflowState.CREATED
    assert workflow.finished is False


def test_finished_property():
    workflow = Workflow(
        name="Completed Workflow",
        steps=[],
    )

    workflow.state = WorkflowState.COMPLETED

    assert workflow.finished is True