from fastapi import APIRouter, Depends

from app.config import get_settings, Settings

router = APIRouter()


@router.get("/fraudsrvcs/health")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
