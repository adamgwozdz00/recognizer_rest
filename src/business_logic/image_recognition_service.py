from src.business_logic.image_information import ImageInformation
from src.business_logic.recognition_result import RecognitionResult
import cv2


class ImageRecognitionService:
    __MOCK_RESULT = RecognitionResult.create_success(ImageInformation("black short screw", 88.2))

    def recognize(self, img: any) -> RecognitionResult:
        try:
            print(img)
            # use model
            return RecognitionResult.create_success(ImageInformation("black short screw", 88.2))
        except Exception as er:
            return RecognitionResult.create_fail()
