"""
Filesystem skills.
"""

from .pwd_skill import PwdSkill
from .ls_skill import LsSkill
from .mkdir_skill import MkdirSkill
from .cat_skill import CatSkill
from .touch_skill import TouchSkill
from .write_skill import WriteSkill
from .append_skill import AppendSkill
from .rm_skill import RmSkill
from .mv_skill import MvSkill
from .cp_skill import CpSkill

FILESYSTEM_SKILLS = (
    PwdSkill,
    LsSkill,
    MkdirSkill,
    CatSkill,
    TouchSkill,
    WriteSkill,
    AppendSkill,
    RmSkill,
    MvSkill,
    CpSkill,
)

__all__ = [
    "PwdSkill",
    "LsSkill",
    "MkdirSkill",
    "CatSkill",
    "TouchSkill",
    "WriteSkill",
    "AppendSkill",
    "RmSkill",
    "MvSkill",
    "CpSkill",
    "FILESYSTEM_SKILLS",
]