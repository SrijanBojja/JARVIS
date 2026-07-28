"""
Conversation manager.
"""

from __future__ import annotations

from jarvis.ai import AIService
from jarvis.applications import ApplicationLauncher
from jarvis.commands.exceptions import CommandNotFoundError
from jarvis.commands.module import CommandModule
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
from .session import ConversationSession
from .resolver import ReferenceResolver

class ConversationManager:
    """
    Coordinates user conversations.
    """

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

        message = " ".join(
            [command, *args],
        ).strip().lower()

        #
        # Pending confirmation.
        #

        if self._workflow_runner.has_pending_confirmation():

            if message in {
                "yes",
                "y",
                "confirm",
                "ok",
                "okay",
            }:
                return self._workflow_runner.execute_pending()

            if message in {
                "no",
                "n",
                "cancel",
                "exit",
            }:
                self._workflow_runner.cancel_pending()

                return Response(
                    text="Cancelled.",
                    status=ResponseStatus.SUCCESS,
                )

        #
        # Waiting for application selection.
        #

        if self._conversation_session.waiting_for_application:

            matches = (
                self._conversation_session.pending_applications
            )

            if matches is None:
                self._conversation_session.clear()

            elif message in {
                "cancel",
                "exit",
            }:
                self._conversation_session.clear()

                return Response(
                    text="Cancelled.",
                )

            elif message.isdigit():

                index = int(message) - 1

                if 0 <= index < len(matches):

                    application = (
                        matches[index].application
                    )

                    self._conversation_session.clear()

                    self._application_launcher.launch(
                        application,
                    )

                    return Response(
                        text=f"Opening {application.name}...",
                        status=ResponseStatus.SUCCESS,
                    )

                return Response(
                    text="Invalid selection.",
                )

            else:

                for result in matches:

                    application = result.application

                    if (
                        message
                        == application.name.lower()
                    ):
                        self._conversation_session.clear()

                        self._application_launcher.launch(
                            application,
                        )

                        return Response(
                            text=f"Opening {application.name}...",
                            status=ResponseStatus.SUCCESS,
                        )

                return Response(
                    text=(
                        "Please choose one of the listed "
                        "applications or type 'cancel'."
                    ),
                )

        #
        # Resolve conversational references.
        #

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