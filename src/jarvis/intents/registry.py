"""
Built-in intent registry.
"""

from __future__ import annotations

from .definition import IntentDefinition


INTENTS: tuple[IntentDefinition, ...] = (
    IntentDefinition(
        "open",
        (
            "open",
            "launch",
            "start",
            "run",
        ),
    ),
    IntentDefinition(
        "shutdown",
        (
            "shutdown",
            "turn off",
            "power off",
        ),
    ),
    IntentDefinition(
        "restart",
        (
            "restart",
            "reboot",
        ),
    ),
    IntentDefinition(
        "sleep",
        (
            "sleep",
        ),
    ),
    IntentDefinition(
        "hibernate",
        (
            "hibernate",
        ),
    ),
    IntentDefinition(
        "logout",
        (
            "logout",
            "log out",
            "sign out",
        ),
    ),
)