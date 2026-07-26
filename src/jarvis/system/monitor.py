"""
System status monitor.
"""

from __future__ import annotations

from datetime import datetime

import platform
import psutil

import string

from pathlib import Path

class SystemMonitor:
    """
    Provides system status information.
    """

    def _cpu(self) -> dict[str, int | float]:
        """
        Returns CPU information.
        """

        return {
            "percent": psutil.cpu_percent(interval=0.5),
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
        }

    def _memory(self) -> dict[str, float]:
        memory = psutil.virtual_memory()

        return {
            "percent": memory.percent,
            "used_gb": round(
                memory.used / (1024**3),
                2,
            ),
            "total_gb": round(
                memory.total / (1024**3),
                2,
            ),
            "available_gb": round(
                memory.available / (1024**3),
                2,
            ),
        }

    def _storage(self) -> list[dict[str, float | str]]:
        """
        Returns storage information for all available drives.
        """

        drives: list[dict[str, float | str]] = []

        for letter in string.ascii_uppercase:

            drive = f"{letter}:\\"

            try:

                usage = psutil.disk_usage(drive)

                drives.append(
                    {
                        "drive": f"{letter}:",
                        "percent": usage.percent,
                        "used_gb": round(
                            usage.used / (1024**3),
                            2,
                        ),
                        "free_gb": round(
                            usage.free / (1024**3),
                            2,
                        ),
                        "total_gb": round(
                            usage.total / (1024**3),
                            2,
                        ),
                    },
                )

            except (
                FileNotFoundError,
                PermissionError,
                OSError,
            ):
                continue

        return drives

    def _battery(self) -> dict[str, object] | None:
        battery = psutil.sensors_battery()

        if battery is None:
            return None

        return {
            "percent": battery.percent,
            "charging": battery.power_plugged,
        }

    def _uptime(self) -> dict[str, int]:
        boot = datetime.fromtimestamp(
            psutil.boot_time(),
        )

        delta = datetime.now() - boot

        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60

        return {
            "days": delta.days,
            "hours": hours,
            "minutes": minutes,
        }

    def _operating_system(self) -> dict[str, str]:
        """
        Returns operating system information.
        """

        return {
            "name": platform.system(),
            "version": platform.release(),
            "architecture": platform.machine(),
        }
    
    def snapshot(self) -> dict[str, object]:
        """
        Returns a complete snapshot of the system.
        """

        return {
            "cpu": self._cpu(),
            "memory": self._memory(),
            "storage": self._storage(),
            "battery": self._battery(),
            "uptime": self._uptime(),
            "os": self._operating_system(),
        }