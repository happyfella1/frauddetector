from pydantic import BaseModel


class EvaluateFraudPayloadSchema(BaseModel):
    url: str


class EvaluateFraudResponseSchema(EvaluateFraudPayloadSchema):
    id: int
