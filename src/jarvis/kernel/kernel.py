"""
JARVIS Kernel
Responsible for starting and stopping
the JARVIS Operating System.
"""

from __future__ import annotations

from datetime import datetime

from jarvis.config import settings
from jarvis.logger import get_logger
from jarvis.modules import ModuleManager

logger = get_logger(__name__)


class Kernel:
    """Core coordinator for JARVIS."""

    def __init__(self) -> None:
        self.version = settings.version
        self.started_at = None
        self.running = False

        self.modules = ModuleManager()

    def start(self) -> None:
        """Start the kernel."""

        self.started_at = datetime.now()
        self.running = True

        self.modules.initialize_all()
        self.modules.start_all()

        print()
        logger.info("Initializing Kernel...")
        print("[OK] Kernel Started")
        print(f"[OK] Version : {self.version}")
        print(f"[OK] Started : {self.started_at}")

    def stop(self) -> None:
        """Stop the kernel."""

        self.running = False

        self.modules.stop_all()

        print()
        print("Shutting Down...")
        print("[OK] Kernel Stopped")