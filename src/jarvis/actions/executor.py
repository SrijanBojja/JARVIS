"""
Action executor contract.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from jarvis.actions.action import Action
from jarvis.responses import Response

class ActionExecutor(ABC):
    """
    Base class for action executors.
    """

    @abstractmethod
    def supports(
        self,
        action: Action,
    ) -> bool:
        """
        Return whether this executor can execute the action.
        """

    @abstractmethod
    def execute(
        self,
        action: Action,
    ) -> Response:
        """
        Execute the supplied action.
        """