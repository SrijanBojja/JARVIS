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
        "clipboard_clear",
        (
            "clear",
            "empty",
        ),
    ),

    IntentDefinition(
        "read_file",
        (
            "read",
        ),
    ),

    IntentDefinition(
        "write_file",
        (
            "write",
        ),
    ),

    IntentDefinition(
        "list_directory",
        (
            "list",
        ),
    ),

    IntentDefinition(
        "create_directory",
        (
            "create",
        ),
    ),

    IntentDefinition(
        "delete_file",
        (
            "delete",
        ),
    ),

    IntentDefinition(
        "delete_directory",
        (
            "delete directory",
        ),
    ),

    IntentDefinition(
        "move_file",
        (
            "move",
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