"""
Conversation module.
"""

from __future__ import annotations

from jarvis.modules import Module


class ConversationModule(Module):
    """
    Initializes the conversation subsystem.
    """

    def start(self) -> None:
        """
        Start the conversation subsystem.
        """

        print("[Conversation] Ready.")

    def stop(self) -> None:
        """
        Stop the conversation subsystem.
        """

        print("[Conversation] Stopped.")