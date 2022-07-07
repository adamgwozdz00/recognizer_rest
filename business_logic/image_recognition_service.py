import os
from time import sleep

from business_logic.ai_service import AIService
from business_logic.image_information import ImageInformation
from business_logic.images_repository import ImagesRepository
from business_logic.results_repository import ResultsRepository
from logger.Logger import Logger
from logger.log_path import get_path


class ImageRecognitionService:

    def __init__(self, images_repository: ImagesRepository, ai_service: AIService,
                 results_repository: ResultsRepository):
        self.image_repository = images_repository
        self.ai_service = ai_service
        self.results_repository = results_repository
        self.logger = Logger(get_path())

    def put_image(self, image) -> ImageInformation:
        try:
            self.image_repository.store(image)
            return ImageInformation(True, "")
        except Exception as e:
            return ImageInformation.create_fail(str(e))

    def recognize(self):
        try:
            image_path = self.image_repository.load()
            result = self.results_repository.load()
            if not os.path.exists(image_path):
                self.logger.debug("Image not found ...")
                return
            if not result:
                self.ai_service.work()
            sleep(1)
        except Exception as er:
            self.logger.debug(str(er))

    def get_result(self) -> bytes:
        return self.results_repository.load()

    def clear(self):
        self.results_repository.clear()
        self.image_repository.clear()
