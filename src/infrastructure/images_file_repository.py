import os
import pathlib

import numpy
from cv2.cv2 import imdecode, IMREAD_COLOR, imwrite

from src.business_logic.images_repository import ImagesRepository


class ImagesFileRepository(ImagesRepository):

    def __init__(self):
        self.abs_path_to_files = pathlib.Path(__file__). \
            parent \
            .parent \
            .joinpath("application") \
            .joinpath("resources") \
            .joinpath("images")

    def store(self, recognition_result: any):
        np_img = numpy.fromstring(recognition_result, numpy.uint8)
        decoded_img = imdecode(np_img, IMREAD_COLOR)
        imwrite(self.__get_result_path(), decoded_img)

    def load(self) -> str:
        return self.__get_result_path()

    def clear(self):
        if os.path.exists(self.__get_result_path()):
         os.remove(self.__get_result_path())

    def __get_result_path(self):
        return f"{self.abs_path_to_files}/image.jpg"
