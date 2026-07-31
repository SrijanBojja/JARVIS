"""
Built-in system skills.
"""

from .time_skill import TimeSkill
from .date_skill import DateSkill
from .day_skill import DaySkill
from .uuid_skill import UUIDSkill
from .random_skill import RandomSkill

SYSTEM_SKILLS = (
    TimeSkill,
    DateSkill,
    DaySkill,
    UUIDSkill,
    RandomSkill,
)

__all__ = [
    "TimeSkill",
    "DateSkill",
    "DaySkill",
    "UUIDSkill",
    "RandomSkill",
    "SYSTEM_SKILLS",
]