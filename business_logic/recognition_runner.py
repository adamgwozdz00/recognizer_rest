import logging
from threading import Thread
from time import sleep

from business_logic.image_recognition_service import ImageRecognitionService


class RecognitionRunner(Thread):
    def __init__(self, recognition_service: ImageRecognitionService):
        super().__init__()
        self.recognition_service = recognition_service

    def run(self) -> None:
        while True:
            self.recognition_service.recognize()
            sleep(1)
