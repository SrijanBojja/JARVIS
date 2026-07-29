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
from jarvis.decision import DecisionEngine
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
        decision_engine: DecisionEngine,
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
        self._decision_engine = decision_engine

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

        return self._decision_engine.handle(
            command,
            args,
        )