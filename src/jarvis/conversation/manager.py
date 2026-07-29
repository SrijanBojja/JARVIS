"""
Conversation manager.
"""

from __future__ import annotations

from jarvis.workflows import WorkflowRunner
from jarvis.applications import ApplicationLauncher
from jarvis.responses import (
    Response,
    ResponseStatus,
)
from jarvis.decision import DecisionEngine
from .session import ConversationSession

class ConversationManager:
    """
    Coordinates user conversations.
    """

    def __init__(
        self,
        conversation_session: ConversationSession,
        application_launcher: ApplicationLauncher,
        workflow_runner: WorkflowRunner,
        decision_engine: DecisionEngine,
    ) -> None:

        self._conversation_session = conversation_session
        self._application_launcher = application_launcher
        self._workflow_runner = workflow_runner
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