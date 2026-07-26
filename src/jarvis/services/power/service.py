"""
Power service contract.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class PowerService(ABC):
    """
    Defines operating system power operations.
    """

    @abstractmethod
    def shutdown(self) -> None:
        """
        Shut down the operating system.
        """

    @abstractmethod
    def restart(self) -> None:
        """
        Restart the operating system.
        """

    @abstractmethod
    def sleep(self) -> None:
        """
        Put the operating system into sleep.
        """

    @abstractmethod
    def hibernate(self) -> None:
        """
        Hibernate the operating system.
        """

    @abstractmethod
    def logout(self) -> None:
        """
        Log the current user out.
        """