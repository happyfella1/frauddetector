import logging
import os

from pydantic import BaseSettings

log = logging.getLogger(__name__)


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY")
    region_name: str = os.getenv("REGION_NAME")


def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()