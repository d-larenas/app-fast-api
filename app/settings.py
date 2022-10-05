"""Settings."""
import enum
from pathlib import Path
from tempfile import gettempdir
from typing import Optional

from pydantic import BaseSettings

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False
    version: str = "0.1.0"
    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    # Sentry's configuration.
    sentry_dsn: Optional[str] = None
    sentry_sample_rate: float = 1.0

    class Config:
        """Config setting."""

        env_file = ".env"
        env_prefix = "APP_SERVICE_"
        env_file_encoding = "utf-8"


settings = Settings()
