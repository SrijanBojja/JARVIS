"""
Decision Engine.

Responsible for deciding which subsystem should handle a user request.
"""

from __future__ import annotations

from jarvis.ai import AIService
from jarvis.applications import ApplicationLauncher
from jarvis.commands.exceptions import CommandNotFoundError
from jarvis.commands.module import CommandModule
from jarvis.conversation.resolver import ReferenceResolver
from jarvis.conversation.session import ConversationSession
from jarvis.intents import IntentResolver
from jarvis.responses import (
    Response,
    ResponseStatus,
)
from jarvis.skills.module import SkillModule
from jarvis.workflows import (
    WorkflowBuilder,
    WorkflowRunner,
)


class DecisionEngine:

    def __init__(
        self,
        command_module: CommandModule,
        skill_module: SkillModule,
        ai_service: AIService,
        intent_resolver: IntentResolver,
        workflow_builder: WorkflowBuilder,
        workflow_runner: WorkflowRunner,
        conversation_session: ConversationSession,
        reference_resolver: ReferenceResolver,
        application_launcher: ApplicationLauncher,
    ) -> None:

        self._command_module = command_module
        self._skill_module = skill_module
        self._ai_service = ai_service
        self._intent_resolver = intent_resolver
        self._workflow_builder = workflow_builder
        self._workflow_runner = workflow_runner
        self._conversation_session = conversation_session
        self._reference_resolver = reference_resolver
        self._application_launcher = application_launcher

    def handle(
        self,
        command: str,
        args: list[str],
    ) -> Response | None:

        args = self._reference_resolver.resolve(
            command,
            args,
        )

        intent = self._intent_resolver.resolve(
            command,
            args,
        )

        workflow = self._workflow_builder.build(
            intent,
            args,
        )

        if workflow is not None:

            result = self._workflow_runner.execute(
                workflow,
            )

            for action, response in zip(
                result.executed_actions,
                result.responses,
            ):
                self._conversation_session.update_from_action(
                    action,
                    response,
                )

            if result.responses:

                response = result.responses[-1]

                if (
                    response.status
                    == ResponseStatus.AMBIGUOUS
                ):
                    self._conversation_session.pending_applications = (
                        response.data
                    )
                else:
                    self._conversation_session.clear()

                return response

        try:
            return self._command_module.execute(
                intent.name,
                args,
            )

        except CommandNotFoundError:

            response = self._skill_module.execute(
                intent.name,
                args,
            )

            if response is not None:
                return response

        return self._ai_service.chat(
            " ".join(
                [command, *args],
            ).strip(),
        )