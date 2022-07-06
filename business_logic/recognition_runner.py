import logging
from threading import Thread
from time import sleep

from business_logic.image_recognition_service import ImageRecognitionService
from logger.Logger import Logger
from logger.log_path import get_path


class RecognitionRunner(Thread):
    def __init__(self, recognition_service: ImageRecognitionService):
        super().__init__()
        self.recognition_service = recognition_service
        self.logger = Logger(get_path())

    def run(self) -> None:
        self.logger.debug("init runner...")
        while True:
            self.recognition_service.recognize()
            sleep(1)
