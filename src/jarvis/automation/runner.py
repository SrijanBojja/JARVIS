"""
Automation runner.
"""

from __future__ import annotations

from jarvis.actions.engine import ActionEngine
from jarvis.conversation.session import ConversationSession
from jarvis.planner.plan import Plan

from .result import AutomationResult
from .verifier import AutomationVerifier
from .recovery import AutomationRecovery


class AutomationRunner:
    """
    Executes an automation plan.
    """

    def __init__(
        self,
        action_engine: ActionEngine,
        conversation_session: ConversationSession,
        verifier: AutomationVerifier,
        recovery: AutomationRecovery,
    ) -> None:

        self._action_engine = action_engine
        self._conversation_session = conversation_session
        self._verifier = verifier
        self._recovery = recovery

    def execute(
        self,
        plan: Plan,
    ) -> AutomationResult:

        responses = []

        for action in plan.actions:

            response = self._action_engine.execute(
                action,
            )

            if not self._verifier.verify(
                action,
                response,
            ):

                recovery_response = self._recovery.recover(
                    action,
                )

                if recovery_response is None:
                    break

                response = recovery_response

                if not self._verifier.verify(
                    action,
                ):
                    break

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