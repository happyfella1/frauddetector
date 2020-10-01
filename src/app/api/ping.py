from fastapi import APIRouter, Depends

from app.log_util import get_logger
from app.config import get_settings, Settings

log = get_logger(__name__)
router = APIRouter()


@router.get("/fraudsrvcs/health")
async def pong(settings: Settings = Depends(get_settings)):
    log.info("request for health check")
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
