import xml.etree.ElementTree as ET

from fastapi import APIRouter, Request, Response

# from app.models.pydantic import EvaluateFraudPayloadSchema, EvaluateFraudResponseSchema

router = APIRouter()


@router.post(
    "/evaluate_fraud", status_code=200
)
async def evaluate_fraud(request: Request):
    print(request.headers)
    headers = request.headers
    body_xml = await request.body()
    root = ET.fromstring(body_xml)

    print('########### START of Reading Request ##########')
    email_address = root[0][1][7][4][1]
    print(email_address.text)
    CreDtTm = root[0][0][1]
    print('creDTM ', CreDtTm.text)
    print('######### END of Reading Request###########')

    print('START of Calling fraud detector')
    
    print('End of calling Fraud dector')

    print('START Reading Response and Apending fraud results')
    response = ET.parse('response.xml').getroot()
    print(response[2][1])
    elem = response[2][1]
    elem[0].text = 'text'
    elem[1].text = 'RULE_NAME'
    elem[2].text = 'RESULT'
    elem[3].text = 'CATEGORY'
    response[2].append(elem)
    print('######### END ###########')

    response_string = ET.tostring(response)
    return Response(content=response_string, media_type="application/xml")
