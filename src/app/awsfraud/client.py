import boto3

from app.config import Settings, get_settings


def get_aws_fd_client(settings: Settings = get_settings()):
    if settings.environment == "dev":
        return boto3.client(
            'frauddetector',
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            aws_session_token='',
            region_name=settings.region_name
        )
    else:
        return boto3.client('frauddetector',region_name=settings.region_name)