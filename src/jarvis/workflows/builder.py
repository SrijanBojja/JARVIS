"""
Workflow builder.
"""

from __future__ import annotations

from jarvis.actions import ActionBuilder
from jarvis.intents import Intent

from .step import WorkflowStep
from .workflow import Workflow


class WorkflowBuilder:
    """
    Builds workflows from intents.
    """

    def __init__(
        self,
        action_builder: ActionBuilder,
    ) -> None:
        self._action_builder = action_builder

    def build(
        self,
        intent: Intent,
        args: list[str],
    ) -> Workflow | None:
        """
        Build a workflow for the supplied intent.
        """

        action = self._action_builder.build(
            intent,
            args,
        )

        if action is None:
            return None

        return Workflow(
            name=intent.name,
            steps=[
                WorkflowStep(
                    name=intent.name,
                    action=action,
                ),
            ],
        )