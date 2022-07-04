from src.application.recognition_response import RecognitionResponse
from src.business_logic.image_information import ImageInformation
from src.business_logic.image_recognition_service import ImageRecognitionService


class RecognitionService:
    def __init__(self, service: ImageRecognitionService):
        self.__service = service

    def load_image(self):
        return self.__service.get_result()

    def send_image(self, image) -> RecognitionResponse:
        result: ImageInformation = self.__service.put_image(image)
        if result.is_success():
            return RecognitionResponse.get_success_response()
        return RecognitionResponse.get_fail_response()

    def clear(self):
        self.__service.clear()
