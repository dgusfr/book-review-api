from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    project_dir: Path = Path(__file__).resolve().parents[2]
    database_url: str = f"sqlite:///{project_dir / 'schema.db'}"

    class Config:
        env_file = ".env"
