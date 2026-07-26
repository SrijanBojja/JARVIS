"""
System controller.
"""

from __future__ import annotations

from .desktop import DesktopController
from .power import PowerController
from .session import SessionController
from .monitor import SystemMonitor


class SystemController:
    """
    Entry point for all operating system operations.
    """

    def __init__(
        self,
        power: PowerController,
        session: SessionController,
        desktop: DesktopController,
        monitor: SystemMonitor,
    ) -> None:
        """
        Initialize the system controller.
        """

        self._power = power
        self._session = session
        self._desktop = desktop
        self._monitor = monitor

    @property
    def power(self) -> PowerController:
        return self._power

    @property
    def session(self) -> SessionController:
        return self._session

    @property
    def desktop(self) -> DesktopController:
        return self._desktop

    @property
    def monitor(self) -> SystemMonitor:
        return self._monitor