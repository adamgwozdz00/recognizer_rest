from application.recognition_response import RecognitionResponse
from business_logic.image_information import ImageInformation
from business_logic.image_recognition_service import ImageRecognitionService


class RecognitionService:
    def __init__(self, service: ImageRecognitionService):
        self.__service = service

    def load_image(self):
        image = self.__service.get_result()
        if not image:
            return RecognitionResponse.get_fail_response("Image not found...")
        return RecognitionResponse.get_success_response(image)

    def send_image(self, image) -> RecognitionResponse:
        result: ImageInformation = self.__service.put_image(image)
        if result.is_success():
            return RecognitionResponse.get_success_response(None)
        return RecognitionResponse.get_fail_response("Something went wrong during sending image...")

    def clear(self):
        self.__service.clear()
