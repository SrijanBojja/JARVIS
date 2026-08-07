"""
Automation runner.
"""

from __future__ import annotations

from jarvis.actions.engine import ActionEngine
from jarvis.conversation.session import ConversationSession
from jarvis.planner.plan import Plan

from .result import AutomationResult


class AutomationRunner:
    """
    Executes an automation plan.
    """

    def __init__(
        self,
        action_engine: ActionEngine,
        conversation_session: ConversationSession,
    ) -> None:

        self._action_engine = action_engine
        self._conversation_session = conversation_session

    def execute(
        self,
        plan: Plan,
    ) -> AutomationResult:

        responses = []

        for action in plan.actions:

            response = self._action_engine.execute(
                action,
            )

            responses.append(
                response,
            )

            self._conversation_session.update_from_action(
                action,
                response,
            )

        return AutomationResult(
            actions=plan.actions,
            responses=responses,
        )