from typing import Optional
from pydantic import BaseModel


class EvaluateFraudPayloadSchema(BaseModel):
    url: str


class EvaluateFraudResponseSchema(EvaluateFraudPayloadSchema):
    id: int


class Transaction(BaseModel):
    id: str
    timestamp: str
    email: Optional[str] = "test@alacriti.com"
    ip_address: Optional[str] = "0.0.0.0"
    test: Optional[str] = None
