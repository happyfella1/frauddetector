import xml.etree.ElementTree as ET

from fastapi import APIRouter, Request, Response

# from app.models.pydantic import EvaluateFraudPayloadSchema, EvaluateFraudResponseSchema

router = APIRouter()


@router.post(
    "/evaluate_fraud", status_code=200
)
async def evaluate_fraud(request: Request):
    print(request.headers)
    body_xml = await request.body()
    root = ET.fromstring(body_xml)
    print(root.attrib)
    print(request.url.port)
    response_object = {"id": "12345", "url": "google.com"}
    return response_object
