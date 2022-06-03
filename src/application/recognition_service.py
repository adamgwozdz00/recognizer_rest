import numpy
from cv2.cv2 import imdecode, IMREAD_COLOR
from cv2.cv2 import FileStorage

from src.application.recognition_response import RecognitionResponse
from src.business_logic.image_recognition_service import ImageRecognitionService


class RecognitionService:
    def __init__(self, service: ImageRecognitionService):
        self.__service = service

    def recognize(self, image: any) -> RecognitionResponse:
        result = self.__service.recognize(self.__convert(image))
        if result.is_success():
            return RecognitionResponse(result.is_success(), result.get_info_what(), result.get_info_accuracy())
        return RecognitionResponse.get_fail_response()

    def __convert(self, image: FileStorage) -> any:
        np_img = numpy.fromstring(image, numpy.uint8)
        return imdecode(np_img, IMREAD_COLOR)
