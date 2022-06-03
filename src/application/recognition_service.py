from src.application.recognition_response import RecognitionResponse
from src.business_logic.image_recognition_service import ImageRecognitionService


class RecognitionService:
    def __init__(self, service: ImageRecognitionService):
        self.__service = service

    def recognize(self, image: any) -> RecognitionResponse:
        result = self.__service.recognize(image)
        if result.is_success():
            return RecognitionResponse(result.is_success(), result.get_info_what(), result.get_info_accuracy())
        return RecognitionResponse.get_fail_response()
