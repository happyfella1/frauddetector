import xml.etree.ElementTree as ET
from datetime import datetime
import logging

from fastapi import APIRouter, Request, Response

from app.awsfraud.requestor import get_event_prediction
from app.api.resources.errors import errors

router = APIRouter()
log = logging.getLogger(__name__)
#Move below urn to errors.py file
ET.register_namespace('', "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01")

@router.post(
    "/fraudsrvcs/v1/initiate_payment/evaluate_fraud", status_code=200
)
async def evaluate_fraud(request: Request):
    try:
        headers = request.headers
        body_xml = await request.body()
        root = ET.fromstring(body_xml)
        timestamp = headers["timestamp"]
        id = headers["idempotent_request_key"]
        transaction = {
            "id": id,
            "timestamp": timestamp
        }
        # use run_to_threadpool to change to async
        awsfraud_result = get_event_prediction(transaction=transaction)
        response = ET.parse('app/api/resources/evaluate_fraud_response.xml').getroot()
        response[2][0][4][0][1].text = str(awsfraud_result["score"])
        response_string = ET.tostring(response)
        return Response(content=response_string, media_type="application/xml")
    except Exception as e:
        log.error(e)
        response = ET.parse('app/api/resources/error.xml').getroot()
        response[0][0][0].text = str(datetime.now())
        response[0][0][2][0][0][0].text = errors["internal_server_error"]["code"]
        response[0][0][2][0][0][1].text = errors["internal_server_error"]["message"]
        response[0][0][2][0][0][2].text = errors["internal_server_error"]["target"]
        response_string = ET.tostring(response)
        return Response(content=response_string, media_type="application/xml", status_code=500)
