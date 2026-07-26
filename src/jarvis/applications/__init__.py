"""
Application subsystem.
"""

from .application import Application
from .launcher import ApplicationLauncher
from .cache import ApplicationCache
from .manager import ApplicationManager
from .shortcut import ShortcutResolver
from .alias import ApplicationAliasGenerator
from .method import LaunchMethod

__all__ = [
    "Application",
    "ApplicationLauncher",
    "ApplicationCache",
    "ApplicationManager",
    "ShortcutResolver",
    "ApplicationAliasGenerator",
    "LaunchMethod",
]