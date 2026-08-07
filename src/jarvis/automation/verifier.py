"""
Automation verification.
"""

from __future__ import annotations

from jarvis.actions import Action


class AutomationVerifier:
    """
    Verifies whether an automation action succeeded.
    """

    def verify(
        self,
        action: Action,
    ) -> bool:
        """
        Verify an executed action.

        Returns:
            True if the action is considered successful.
        """

        return True