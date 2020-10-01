from app.log_util import get_logger
from app.api.resources.errors import InvalidHeader, errors

log = get_logger(__name__)


def validate_headers(headers:dict):
    validated_headers = {}
    response_headers = {}
    #mandatory headers
    if "timestamp" in headers:
        validated_headers["timestamp"] = headers["timestamp"]
    else:
        raise_error(errors["invalid_header_timestamp"])

    if "idempotent_request_key" in headers:
        validated_headers["idempotent_request_key"] = headers["idempotent_request_key"]
        response_headers["idempotent_request_key"] = headers["idempotent_request_key"]
    else:
        raise_error(errors["invalid_header_idempotentkey"])

    if "client_key" in headers:
        validated_headers["client_key"] = headers["client_key"]
        response_headers["client_key"] = headers["client_key"]
    else:
        raise_error(errors["invalid_header_client_key"])

    if "api_key" in headers:
        validated_headers["api_key"] = headers["api_key"]

    if "product" in headers:
        validated_headers["product"] = headers["product"]
        response_headers["product"] = headers["product"]
    else:
        raise_error(errors["invalid_header_product"])

    if "payment_channel" in headers:
        validated_headers["payment_channel"] = headers["payment_channel"]
        response_headers["payment_channel"] = headers["payment_channel"]
    else:
        raise_error(errors["invalid_header_payment_channel"])

    if "requestor_type" in headers:
        validated_headers["requestor_type"] = headers["requestor_type"]
        response_headers["requestor_type"] = headers["requestor_type"]
    else:
        raise_error(errors["invalid_header_requestor_type"])

    # non mandatory headers

    if "access_channel" in headers:
        validated_headers["access_channel"] = headers["access_channel"]
        response_headers["access_channel"] = headers["access_channel"]

    if "client_requestor_reference" in headers:
        validated_headers["client_requestor_reference"] = headers["client_requestor_reference"]
        response_headers["client_requestor_reference"] = headers["client_requestor_reference"]

    if "requestor" in headers:
        validated_headers["requestor"] = headers["requestor"]
        response_headers["requestor"] = headers["requestor"]

    if "context_variant" in headers:
        validated_headers["context_variant"] = headers["context_variant"]
        response_headers["context_variant"] = headers["context_variant"]

    if "X-PaaS-Header" in headers:
        validated_headers["X-PaaS-Header"] = headers["X-PaaS-Header"]
        response_headers["X-PaaS-Header"] = headers["X-PaaS-Header"]

    return [validated_headers, response_headers]


def raise_error(message):
    raise InvalidHeader(
        code=message["code"],
        message=message["message"],
        target=message["target"]
    )


