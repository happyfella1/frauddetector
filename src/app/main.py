import logging

from fastapi import FastAPI

from app.api import evaluate_fraud, ping

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(evaluate_fraud.router)

    return application


app = create_application()
