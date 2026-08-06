"""
Application configuration for JARVIS.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Settings:
    """
    Immutable application settings.
    """

    app_name: str
    version: str
    debug: bool
    project_root: Path
    data_dir: Path
    logs_dir: Path
    voice_engine: str
    voice_model: str
    ai_model: str
    ai_host: str


PROJECT_ROOT = Path(__file__).resolve().parents[3]

settings = Settings(
    app_name="JARVIS",
    version="0.2.0",
    debug=True,
    project_root=PROJECT_ROOT,
    data_dir=PROJECT_ROOT / "data",
    logs_dir=PROJECT_ROOT / "logs",
    voice_engine="piper",
    voice_model="en_US-ryan-medium",
    ai_model="qwen2.5:3b",
    ai_host="http://127.0.0.1:11434",
)