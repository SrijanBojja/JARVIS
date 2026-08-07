"""
Vision-based automation verification.
"""

from __future__ import annotations

from jarvis.actions import Action
from jarvis.vision import VisionService

from .verifier import AutomationVerifier


class VisionAutomationVerifier(
    AutomationVerifier,
):
    """
    Verifies actions using the VisionService.
    """

    def __init__(
        self,
        vision_service: VisionService,
    ) -> None:

        self._vision_service = vision_service

    def verify(
        self,
        action: Action,
    ) -> bool:
        """
        Verify an executed action.

        Temporary implementation.
        """

        #
        # Vision verification will be added
        # in the next step.
        #

        result = self._vision_service.verify_action(
            action,
        )

        print(
            f"[VISION VERIFY] {action.name}({action.target}) -> {result}"
        )

        return result