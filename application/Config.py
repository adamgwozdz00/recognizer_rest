from acl.Config import image_recognition_service
from application.recognition_service import RecognitionService


def recognition_service() -> RecognitionService:
    return RecognitionService(image_recognition_service())
