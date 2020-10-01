from pydantic import validate_arguments

from app.log_util import get_logger
from app.awsfraud.client import get_aws_fd_client
from app.models.pydantic import Transaction
from app.api.resources.errors import errors, InvalidHeader, InternalServerError

client = get_aws_fd_client()
log = get_logger(__name__)


@validate_arguments
def get_event_prediction(transaction: Transaction):
    log.info("Calling AWS fraud detector")
    try:
        response = client.get_event_prediction(
            detectorId='paymentfrauddetector',
            eventId=transaction.id,
            eventTypeName='payment',
            entities=[
                {
                    'entityType': 'account',
                    'entityId': 'unknown'
                },
            ],
            eventTimestamp=transaction.timestamp,
            eventVariables={
                'email_address': transaction.email,
                'ip_address':transaction.ip_address,
            }
        )
        return {"score": response['modelScores'][0]['scores']['fraudmodel1_insightscore']}
    except Exception as e:
        log.error(e)
        error = errors["internal_server_error"]
        raise InternalServerError(
            code=error["code"],
            message=error["message"],
            target=error["target"]
        )

