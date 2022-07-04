from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RecognitionResponse:
    success: bool
    message: str

    @staticmethod
    def get_success_response():
        return RecognitionResponse(True, "")

    @staticmethod
    def get_fail_response(ex: str):
        return RecognitionResponse(False, ex)
