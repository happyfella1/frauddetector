from app.log_util import get_logger
import os

from fastapi import FastAPI

from app.api import evaluate_fraud, ping

log = get_logger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(evaluate_fraud.router)
    return application


app = create_application()
