import logging

from app.api.resources.errors import InvalidHeader, errors

log = logging.getLogger(__name__)


def validate_headers(headers:dict):
    validated_headers = {}
    if "timestamp" in headers:
        validated_headers["timestamp"] = headers["timestamp"]
    else:
        invalid = errors["invalid_header_timestamp"]
        raise InvalidHeader(
            code=invalid["code"],
            message=invalid["message"],
            target=invalid["message"]
        )

    if "idempotent_request_key" in headers:
        validated_headers["idempotent_request_key"] = headers["idempotent_request_key"]
    else:
        invalid = errors["invalid_header_idempotentkey"]
        raise InvalidHeader(
            code=invalid["code"],
            message=invalid["message"],
            target=invalid["message"]
        )

    if "client_key" in headers:
        validated_headers["client_key"] = headers["client_key"]

    if "api_key" in headers:
        validated_headers["api_key"] = headers["api_key"]

    if "product" in headers:
        validated_headers["product"] = headers["product"]

    if "payment_channel" in headers:
        validated_headers["payment_channel"] = headers["payment_channel"]

    if "access_channel" in headers:
        validated_headers["access_channel"] = headers["access_channel"]

    if "requestor_type" in headers:
        validated_headers["requestor_type"] = headers["requestor_type"]

    if "X-PaaS-Header" in headers:
        validated_headers["X-PaaS-Header"] = headers["X-PaaS-Header"]

    return validated_headers
