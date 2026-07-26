"""
Confirmation manager.
"""

from __future__ import annotations

from datetime import datetime

from .exceptions import (
    ActionExpiredError,
    NoPendingActionError,
    PendingActionError,
)
from .pending import PendingAction
from datetime import datetime, timedelta
from uuid import uuid4

class ConfirmationManager:
    """
    Manages pending confirmation actions.
    """

    def __init__(self) -> None:
        self._pending: PendingAction | None = None

    @property
    def pending(self) -> PendingAction | None:
        return self._pending

    def request(
        self,
        title: str,
        message: str,
        callback,
        timeout: int = 30,
    ) -> PendingAction:
        """
        Creates a pending confirmation action.
        """

        if self._pending is not None:
            raise PendingActionError(
                "A confirmation is already pending.",
            )

        now = datetime.now()

        self._pending = PendingAction(
            action_id=str(uuid4()),
            title=title,
            message=message,
            callback=callback,
            created_at=now,
            expires_at=now + timedelta(seconds=timeout),
        )

        return self._pending

    def confirm(self) -> None:
        """
        Confirms and executes the pending action.
        """

        pending = self._require_pending()

        if self.is_expired():
            self.clear()

            raise ActionExpiredError(
                "Pending action has expired.",
            )

        callback = pending.callback

        self.clear()

        callback()

    def cancel(self) -> None:
        """
        Cancels the pending action.
        """

        self._require_pending()

        self.clear()

    def has_pending(self) -> bool:
        """
        Returns whether an action is awaiting confirmation.
        """

        return self._pending is not None

    def is_expired(self) -> bool:
        """
        Returns whether the pending action has expired.
        """

        pending = self._require_pending()

        return datetime.now() > pending.expires_at

    def clear(self) -> None:
        """
        Removes any pending action without executing it.
        """
        self._pending = None

    def _require_pending(self) -> PendingAction:
        """
        Returns the current pending action.

        Raises:
            NoPendingActionError: If no action is pending.
        """

        if self._pending is None:
            raise NoPendingActionError(
                "No pending action.",
            )

        return self._pending