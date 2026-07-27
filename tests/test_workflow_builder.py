from jarvis.intents import Intent
from jarvis.workflows import WorkflowBuilder


def test_builder_returns_none_for_now():
    builder = WorkflowBuilder()

    workflow = builder.build(
        Intent(
            name="open",
            confidence=1.0,
        ),
        ["chrome"],
    )

    assert workflow is None