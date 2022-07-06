import logging

from acl.ai_service_adapter import AIServiceAdapter
from application.recognition_service import RecognitionService
from business_logic.ai_service import AIService
from business_logic.image_recognition_service import ImageRecognitionService
from business_logic.images_repository import ImagesRepository
from business_logic.results_repository import ResultsRepository
from infrastructure.images_file_repository import ImagesFileRepository
from infrastructure.results_file_repository import ResultsFileRepository
from logger.Logger import Logger
from logger.log_path import get_path


class Injector:
    ai_service: AIService
    image_recognition_service: ImageRecognitionService
    images_repository: ImagesRepository
    results_repository: ResultsRepository
    recognition_service: RecognitionService
    logger : Logger

    def __init__(self):
        self.logger = Logger(get_path())
        self.logger.debug("init injector...")
        self.ai_service = AIServiceAdapter()
        self.results_repository = ResultsFileRepository()
        self.images_repository = ImagesFileRepository()
        self.image_recognition_service = ImageRecognitionService(self.images_repository, self.ai_service,
                                                                 self.results_repository)
        self.recognition_service = RecognitionService(self.image_recognition_service)

    def inject_image_recognition_service(self) -> ImageRecognitionService:
        return self.image_recognition_service

    def inject__recognition_service(self) -> RecognitionService:
        return self.recognition_service


injector = Injector()
