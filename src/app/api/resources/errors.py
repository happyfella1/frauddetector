errors = {
    "admi_namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
    "internal_server_error": {
        "code": "RSK-00-1001",
        "message": "Internal Server error",
        "target": "server.exception",
        "status_code": "500"
    },
    "invalid_header_timestamp": {
        "code": "RSK-10-1003",
        "message": "Invalid header timestamp",
        "target": "header.timestamp",
        "status_code": "400"
    },
    "invalid_header_idempotentkey": {
        "code": "RSK-10-1011",
        "message": "Invalid header idempotent key",
        "target": "header.idempotent_key",
        "status_code": "400"
    },
    "invalid_header_client_key":{
        "code": "RSK-10-1002",
        "message": "Invalid header client key",
        "target": "header.client_key",
        "status_code": "400"
    },
    "invalid_header_product":{
        "code": "RSK-10-1001",
        "message": "Invalid header product",
        "target": "header.product",
        "status_code": "400"
    },
    "invalid_header_payment_channel":{
        "code": "RSK-10-1004",
        "message": "Invalid header payment channel",
        "target": "header.payment_channel",
        "status_code": "400"
    },
    "invalid_header_requestor_type":{
        "code": "RSK-10-1006",
        "message": "Invalid header requestor type",
        "target": "header.requestor_type",
        "status_code": "400"
    }
}


class CustomError(Exception):
    def __init__(self, code, message, target ):
        self.message = message
        self.code = code
        self.target = target
        super().__init__(self.message)

    def get_error_xml_string(self):
        return ' --><![CDATA[' + '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><errors><error>' \
                '<code>' + self.code + '</code>' \
                '<message>' + self.message + '</message>' \
                '<target>' + self.target + '</target>' \
                '</error></errors>' + ']]><!-- '


class InvalidHeader(CustomError):
    pass


class InternalServerError(CustomError):
    pass




