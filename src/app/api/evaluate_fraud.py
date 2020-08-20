import xml.etree.ElementTree as ET
from datetime import datetime
import logging

from fastapi import APIRouter, Request, Response

from app.awsfraud.requestor import get_event_prediction
from app.api.resources.errors import errors, InvalidHeader, InternalServerError
from app.api.util import validate_headers

router = APIRouter()
log = logging.getLogger(__name__)
#Move below urn to errors.py file
ET.register_namespace("", errors["admi_namespace"])

@router.post(
    "/fraudsrvcs/v1/initiate_payment/evaluate_fraud", status_code=200
)
async def evaluate_fraud(request: Request):
    try:
        headers = dict(request.headers)
        validated_headers = validate_headers(headers)
        body_xml = await request.body()
        root = ET.fromstring(body_xml)
        timestamp = validated_headers["timestamp"]
        id = validated_headers["idempotent_request_key"]
        transaction = {
            "id": id,
            "timestamp": timestamp
        }
        # use run_to_threadpool to change to async
        awsfraud_result = get_event_prediction(transaction=transaction)
        response = ET.parse('app/api/resources/evaluate_fraud_response.xml').getroot()
        response[2][0][4][0][1].text = str(awsfraud_result["score"])
        response_string = ET.tostring(response)
        return Response(content=response_string, headers=validated_headers, media_type="application/xml")
    except InvalidHeader as e:
        log.error(e)
        response = ET.parse('app/api/resources/error.xml').getroot()
        response[0][0][0].text = str(datetime.now())
        response[0][0][2].append(ET.Comment(e.get_error_xml_string()))
        response_string = ET.tostring(response)
        return Response(content=response_string, media_type="application/xml", status_code=400)

    except Exception as e:
        log.error(e)
        response = ET.parse('app/api/resources/error.xml').getroot()
        response[0][0][0].text = str(datetime.now())
        error = errors["internal_server_error"]
        is_error = InternalServerError(
            code=error["code"],
            message=error["message"],
            target=error["target"]
        )
        response[0][0][2].append(ET.Comment(is_error.get_error_xml_string()))
        response_string = ET.tostring(response)
        return Response(content=response_string, media_type="application/xml",status_code=500)
