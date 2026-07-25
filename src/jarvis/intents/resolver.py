"""
Intent resolver.
"""

from __future__ import annotations

from jarvis.intents.intent import Intent


class IntentResolver:
    """
    Resolves the user's intent.
    """

    def resolve(
        self,
        command: str,
    ) -> Intent:
        """
        Resolve the user intent.
        """

        return Intent(
            name=command,
            confidence=1.0,
        )