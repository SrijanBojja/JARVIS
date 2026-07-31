"""
Skill exceptions.
"""


class SkillError(Exception):
    """
    Base exception for all skill errors.
    """


class SkillNotFoundError(SkillError):
    """
    Raised when a skill cannot be found.
    """