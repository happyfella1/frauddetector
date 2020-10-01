import os

from pydantic import BaseSettings

from app.log_util import get_logger

log = get_logger(__name__)


class Settings(BaseSettings):
    environment: str = os.getenv("ALA_ENVIRONMENT_TYPE", "dev")
    testing: bool = os.getenv("TESTING", 0)
    region_name: str = os.getenv("AWS_FD_REGION")
    if os.getenv("ALA_ENVIRONMENT_TYPE") == "dev":
        aws_access_key_id: str = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key: str = os.getenv("AWS_SECRET_ACCESS_KEY")
        # region_name: str = os.getenv("REGION_NAME")


def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()