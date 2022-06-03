from src.application.recognition_service import RecognitionService
from src.business_logic.Config import image_recognition_service


def recognition_service() -> RecognitionService:
    return RecognitionService(image_recognition_service())
