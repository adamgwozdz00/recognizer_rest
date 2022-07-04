import os
from time import sleep

from src.business_logic.ai_service import AIService
from src.business_logic.image_information import ImageInformation
from src.business_logic.images_repository import ImagesRepository
from src.business_logic.results_repository import ResultsRepository


class ImageRecognitionService:

    def __init__(self, images_repository: ImagesRepository, ai_service: AIService,
                 results_repository: ResultsRepository):
        self.image_repository = images_repository
        self.ai_service = ai_service
        self.results_repository = results_repository

    def put_image(self, image) -> ImageInformation:
        try:
            self.image_repository.store(image)
            return ImageInformation(True, "")
        except Exception as e:
            return ImageInformation.create_fail(str(e))

    def recognize(self):
        try:
            image_path = self.image_repository.load()
            result_path = self.results_repository.load()
            if not os.path.exists(image_path):
                return
            if not os.path.exists(result_path):
                self.ai_service.work(image_path)
            sleep(5)


        except Exception as er:
            print(er)

    def get_result(self) -> str:
        return self.results_repository.load()

    def clear(self):
        self.results_repository.clear()
        self.image_repository.clear()
