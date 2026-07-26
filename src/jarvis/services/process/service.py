"""
Process service contract.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from jarvis.services.base import Service


class ProcessService(Service, ABC):
    """
    Defines process and application operations.
    """

    @abstractmethod
    def launch(self, target: str) -> None:
        """
        Launch an application, document, folder, or URL.
        """

    @abstractmethod
    def is_running(self, process_name: str) -> bool:
        """
        Return True if the process is running.
        """

    @abstractmethod
    def terminate(self, process_name: str) -> None:
        """
        Terminate a running process.
        """