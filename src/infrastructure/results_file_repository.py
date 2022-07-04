import os
import pathlib

from src.business_logic.results_repository import ResultsRepository


class ResultsFileRepository(ResultsRepository):
    def __init__(self):
        self.abs_path_to_files = pathlib.Path(__file__). \
            parent \
            .parent \
            .parent \
            .joinpath("yolov5") \
            .joinpath("runs")

    def load(self) -> str:
        return f"{self.abs_path_to_files.joinpath('detect').joinpath('exp')}/image.jpg"

    def is_exists(self) -> bool:
        os.path.exists(f"{self.abs_path_to_files.joinpath('detect').joinpath('exp')}/image.jpg")

    def clear(self):
        if self.is_exists():
            os.remove(f"{self.abs_path_to_files.joinpath('detect').joinpath('exp')}/image.jpg")



