import logging

from pydantic import validate_arguments

from app.awsfraud.client import get_aws_fd_client
from app.models.pydantic import Transaction

client = get_aws_fd_client()
log = logging.getLogger(__name__)


@validate_arguments
def get_event_prediction(transaction: Transaction):
    log.info("Calling AWS fraud detector")
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

