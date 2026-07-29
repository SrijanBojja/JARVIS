"""
Mock AI provider for JARVIS.
"""

from __future__ import annotations

from jarvis.ai.message import Message
from jarvis.ai.provider import AIProvider
from jarvis.responses import Response


class MockAIProvider(AIProvider):
    """
    Temporary AI provider used during development.
    """

    def chat(
        self,
        messages: list[Message],
    ) -> Response:

        if not messages:
            return Response(
                "Hello! I'm JARVIS."
            )

        message = messages[-1].content.lower().strip()

        if "hello" in message or "hi" in message:
            return Response(
                "Hello! I'm JARVIS. How can I help you today?"
            )

        if "who are you" in message:
            return Response(
                "I'm JARVIS, your personal AI operating system."
            )

        return Response(
            f'I heard you say: "{message}"'
        )