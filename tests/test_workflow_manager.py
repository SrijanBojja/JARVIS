from jarvis.workflows import Workflow
from jarvis.workflows import WorkflowManager
from jarvis.workflows import WorkflowState


def test_register_workflow():
    manager = WorkflowManager()

    workflow = Workflow(
        name="Demo",
        steps=["one"]
    )

    manager.register(workflow)

    assert manager.get(workflow.id) is workflow


def test_start_workflow():
    manager = WorkflowManager()

    workflow = Workflow(
        name="Demo",
        steps=[]
    )

    manager.register(workflow)

    manager.start(workflow.id)

    assert workflow.state == WorkflowState.RUNNING


def test_complete_workflow():
    manager = WorkflowManager()

    workflow = Workflow(
        name="Demo",
        steps=[]
    )

    manager.register(workflow)

    manager.complete(workflow.id)

    assert workflow.state == WorkflowState.COMPLETED


def test_cancel_workflow():
    manager = WorkflowManager()

    workflow = Workflow(
        name="Demo",
        steps=[]
    )

    manager.register(workflow)

    manager.cancel(workflow.id)

    assert workflow.state == WorkflowState.CANCELLED