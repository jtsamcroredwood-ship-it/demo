from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    SESSION_SECRET: str
    DEBUG: bool = False

    @field_validator("DEBUG", mode="before")
    def _parse_debug(cls, v):
        # Allow common non-boolean DEBUG conventions like DEBUG=release/dev.
        if isinstance(v, str):
            value = v.strip().lower()
            if value in {"release", "prod", "production"}:
                return False
            if value in {"debug", "dev", "development"}:
                return True
        return v

    class Config:
        # Resolve relative to project root so tools like Alembic work from any CWD.
        env_file = Path(__file__).resolve().parents[1] / ".env"

settings = Settings()
