"""
Conversation reference resolver.
"""

from __future__ import annotations

from jarvis.conversation.references import (
    ApplicationReferences,
)
from jarvis.conversation.session import (
    ConversationSession,
)

APPLICATION_COMMANDS = {
    "close",
    "minimize",
    "maximize",
    "restore",
}

class ReferenceResolver:
    """
    Resolves conversational references.
    """

    def __init__(
        self,
        application_references: ApplicationReferences,
        conversation_session: ConversationSession,
    ) -> None:
        self._application_references = (
            application_references
        )

        self._conversation_session = (
            conversation_session
        )

    def resolve(
        self,
        command: str,
        args: list[str],
    ) -> list[str]:
        """
        Resolve conversational references.
        """

        if not args:
            return args

        resolved_args = args.copy()

        reference = resolved_args[-1].lower()

        if reference != "it":
            return resolved_args

        if command in APPLICATION_COMMANDS:

            application = (
                self._application_references.latest()
            )

            if application is not None:
                resolved_args[-1] = application

        elif (
            command == "delete"
            and len(resolved_args) >= 2
        ):

            kind = resolved_args[0].lower()

            if kind == "file":

                file = (
                    self._conversation_session.get_entity(
                        "file",
                    )
                )

                if file is not None:
                    resolved_args[-1] = file

            elif kind == "directory":

                directory = (
                    self._conversation_session.get_entity(
                        "directory",
                    )
                )

                if directory is not None:
                    resolved_args[-1] = directory

        elif command == "open":

            directory = (
                self._conversation_session.get_entity(
                    "directory",
                )
            )

            if directory is not None:
                resolved_args[-1] = directory

        return resolved_args