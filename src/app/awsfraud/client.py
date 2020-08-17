import boto3
from fastapi import Depends

from app.config import Settings, get_settings


def get_aws_fd_client(settings: Settings = get_settings()):
    return boto3.client(
        'frauddetector',
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key,
        aws_session_token='',
        region_name=settings.region_name
    )