"""
Intent resolver.
"""

from __future__ import annotations

from jarvis.intents.intent import Intent
from jarvis.intents.registry import INTENTS


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

        text = command.strip().lower()

        for definition in INTENTS:
            if text in definition.aliases:
                return Intent(
                    name=definition.name,
                    confidence=1.0,
                )

        return Intent(
            name=text,
            confidence=0.0,
        )