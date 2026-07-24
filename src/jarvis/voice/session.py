"""
Voice conversation session.
"""

from __future__ import annotations

import time


class VoiceSession:
    """
    Tracks an active voice conversation.
    """

    def __init__(
        self,
        timeout: float = 15.0,
    ) -> None:
        self._timeout = timeout
        self._last_activity = 0.0
        self._active = False

    @property
    def active(
        self,
    ) -> bool:
        """
        Return whether a session is active.
        """

        return self._active

    def start(
        self,
    ) -> None:
        """
        Start a conversation session.
        """

        self._active = True
        self.refresh()

    def stop(
        self,
    ) -> None:
        """
        Stop the conversation session.
        """

        self._active = False

    def refresh(
        self,
    ) -> None:
        """
        Update the last activity timestamp.
        """

        self._last_activity = time.monotonic()

    def expired(
        self,
    ) -> bool:
        """
        Return True if the session has timed out.
        """

        if not self._active:
            return False

        return (
            time.monotonic() - self._last_activity
        ) > self._timeout