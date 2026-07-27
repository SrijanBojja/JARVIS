from jarvis.actions import Action
from jarvis.responses import Response, ResponseStatus
from jarvis.workflows import (
    Workflow,
    WorkflowManager,
    WorkflowRunner,
    WorkflowState,
    WorkflowStep,
)


class FakeActionEngine:
    """
    Simple fake ActionEngine for testing.
    """

    def execute(self, action: Action) -> Response:
        return Response(
            text=f"Executed {action.name}",
            status=ResponseStatus.SUCCESS,
        )


def test_workflow_runner_executes_workflow():

    manager = WorkflowManager()

    runner = WorkflowRunner(
        workflow_manager=manager,
        action_engine=FakeActionEngine(),
    )

    workflow = Workflow(
        name="Open Chrome",
        steps=[
            WorkflowStep(
                name="Open Chrome",
                action=Action(
                    name="open",
                    target="chrome",
                ),
            ),
        ],
    )

    manager.register(workflow)

    result = runner.execute(workflow)

    assert result.status == WorkflowState.COMPLETED

    assert result.completed_steps == 1

    assert result.failed_step is None

    assert len(result.responses) == 1

    assert workflow.state == WorkflowState.COMPLETED

    assert workflow.steps[0].state.name == "COMPLETED"