"""
Vision provider interface.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class VisionProvider(ABC):
    """
    Base interface for vision providers.
    """

    @abstractmethod
    def describe(
        self,
        image_path: str,
        prompt: str,
    ) -> str:
        """
        Describe an image.
        """