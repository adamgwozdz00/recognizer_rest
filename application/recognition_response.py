from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RecognitionResponse:
    success: bool
    message: str
    image: bytes

    @staticmethod
    def get_success_response(image: bytes):
        return RecognitionResponse(True, "", image)

    @staticmethod
    def get_fail_response(ex: str):
        return RecognitionResponse(False, ex, None)
