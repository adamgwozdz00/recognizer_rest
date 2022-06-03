from dataclasses import dataclass
from typing import Optional
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class RecognitionResponse:
    success: bool
    recognition: Optional[str]
    percentage: Optional[float]

    @staticmethod
    def get_fail_response():
        return RecognitionResponse(False, None, None)
