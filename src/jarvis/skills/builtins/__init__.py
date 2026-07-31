"""
Built-in JARVIS skills.
"""

from .calculator import CalculatorSkill
from .system import SYSTEM_SKILLS
from .filesystem import FILESYSTEM_SKILLS

BUILTIN_SKILLS = (
    CalculatorSkill,
    *SYSTEM_SKILLS,
    *FILESYSTEM_SKILLS,
)

__all__ = [
    "CalculatorSkill",
    "SYSTEM_SKILLS",
    "FILESYSTEM_SKILLS",
    "BUILTIN_SKILLS",
]