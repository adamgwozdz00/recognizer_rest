from acl.ai_service_adapter import AIServiceAdapter
from business_logic.image_recognition_service import ImageRecognitionService
from infrastructure.images_file_repository import ImagesFileRepository
from infrastructure.results_file_repository import ResultsFileRepository


def image_recognition_service() -> ImageRecognitionService:
    images_repository = ImagesFileRepository()
    results_repository = ResultsFileRepository()
    ai_service = AIServiceAdapter()
    return ImageRecognitionService(images_repository, ai_service, results_repository)
