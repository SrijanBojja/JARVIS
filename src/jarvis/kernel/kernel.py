"""
JARVIS Kernel
Responsible for starting and stopping
the JARVIS Operating System.
"""

from datetime import datetime
from jarvis.config import settings

class Kernel:
    """Core coordinator for JARVIS."""

    def __init__(self):
        self.version = settings.version
        self.started_at = None
        self.running = False

    def start(self):
        """Start the kernel."""

        self.started_at = datetime.now()
        self.running = True

        print()
        print("Initializing Kernel...")
        print("[✓] Kernel Started")
        print(f"[✓] Version : {self.version}")
        print(f"[✓] Started : {self.started_at}")

    def stop(self):
        """Stop the kernel."""

        self.running = False

        print()
        print("Shutting Down...")
        print("[✓] Kernel Stopped")