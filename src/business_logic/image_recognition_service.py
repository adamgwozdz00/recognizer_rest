import cv2.cv2

from src.business_logic.image_information import ImageInformation
from src.business_logic.recognition_result import RecognitionResult
from cv2.cv2 import imwrite


class ImageRecognitionService:
    __MOCK_RESULT = RecognitionResult.create_success(ImageInformation("black short screw", 88.2))

    def recognize(self, img: any) -> RecognitionResult:
        try:
            imwrite('resources/result.png', img)
            # use model
            return RecognitionResult.create_success(ImageInformation("black short screw", 88.2))
        except Exception as er:
            return RecognitionResult.create_fail()
