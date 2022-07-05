import os
import pathlib
import shutil

from business_logic.results_repository import ResultsRepository


class ResultsFileRepository(ResultsRepository):
    def __init__(self):
        self.abs_path_to_files = pathlib.Path(__file__). \
            parent \
            .parent \
            .joinpath("yolov5") \
            .joinpath("runs")

    def load(self) -> str:
        return f"{self.abs_path_to_files.joinpath('detect').joinpath('exp')}/image.jpg"

    def is_exists(self) -> bool:
        return os.path.exists(self.abs_path_to_files.joinpath('detect').joinpath('exp').joinpath('image.jpg'))

    def clear(self):
        if self.is_exists():
            shutil.rmtree(self.abs_path_to_files.joinpath('detect').joinpath('exp'))



