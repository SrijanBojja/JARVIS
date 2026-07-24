"""
Mock AI provider for JARVIS.
"""

from __future__ import annotations

from jarvis.ai import AIProvider
from jarvis.responses import Response


class MockAIProvider(AIProvider):
    """
    Temporary AI provider used during development.
    """

    def chat(
        self,
        message: str,
    ) -> Response:

        message = message.lower().strip()

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