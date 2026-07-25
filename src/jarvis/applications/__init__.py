"""
Application subsystem.
"""

from .application import Application
from .registry import ApplicationRegistry
from .launcher import ApplicationLauncher
from .scanner import ApplicationScanner
from .cache import ApplicationCache
from .manager import ApplicationManager
from .shortcut import ShortcutResolver
from .alias import ApplicationAliasGenerator
from .method import LaunchMethod

__all__ = [
    "Application",
    "ApplicationRegistry",
    "ApplicationLauncher",
    "ApplicationScanner",
    "ApplicationCache",
    "ApplicationManager",
    "ShortcutResolver",
    "ApplicationAliasGenerator",
    "LaunchMethod",
]
