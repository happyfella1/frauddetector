errors = {
    "admi_namespace": "urn:iso:std:iso:20022:tech:xsd:admi.002.001.01",
    "internal_server_error": {
        "code": "RSK-00-1001",
        "message": "Internal Server error",
        "target": "server.exception",
        "status_code": "500"
    },
    "invalid_header_timestamp": {
        "code": "RSK-00-1003",
        "message": "Invalid header timestamp",
        "target": "timestamp",
        "status_code": "400"
    },
    "invalid_header_idempotentkey": {
        "code": "RSK-00-1001",
        "message": "Invalid header idempotent key",
        "target": "idempotent_key",
        "status_code": "400"
    }

}


class CustomError(Exception):
    def __init__(self, code, message, target ):
        self.message = message
        self.code = code
        self.target = target
        super().__init__(self.message)

    def get_error_xml_string(message):
        return ' --><![CDATA[' + '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><errors><error>' \
                '<code>' + message.code + '</code>' \
                '<message>' + message.message + '</message>' \
                '<target>' + message.target + '</target>' \
                '</error></errors>' + ']]><!-- '


class InvalidHeader(CustomError):
    pass


class InternalServerError(CustomError):
    pass




