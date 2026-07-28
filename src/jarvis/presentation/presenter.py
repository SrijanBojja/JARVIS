"""
Presentation interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from jarvis.responses import Response


class Presenter(ABC):
    """
    Base class for response presenters.
    """

    @abstractmethod
    def present(
        self,
        response: Response,
    ) -> None:
        """
        Present a response.
        """