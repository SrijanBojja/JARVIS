from jarvis.workflows.step import WorkflowStep
from jarvis.workflows.step_state import WorkflowStepState
from jarvis.actions import Action

def test_workflow_step_creation():
    step = WorkflowStep(
        name="Open Chrome",
        action=Action(
            name="open",
            target="chrome",
        ),
    )

    assert step.name == "Open Chrome"

    assert step.action.name == "open"
    assert step.action.target == "chrome"
    assert step.action.requires_confirmation is False

    assert step.state == WorkflowStepState.PENDING