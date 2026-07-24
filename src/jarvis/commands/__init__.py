"""
Public interface for the JARVIS command package.
"""

from .command import Command
from .registry import CommandRegistry

__all__ = [
    "Command",
    "CommandRegistry",
]