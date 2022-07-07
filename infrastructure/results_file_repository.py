import base64
import os
import pathlib
import shutil
from io import BytesIO
from PIL import Image
from business_logic.results_repository import ResultsRepository


class ResultsFileRepository(ResultsRepository):
    def __init__(self):
        self.abs_path_to_files = pathlib.Path(__file__). \
            parent \
            .parent \
            .joinpath("yolov5") \
            .joinpath("runs")

    def load(self) -> any:
        if self.is_exists():
            img = Image.open(f"{self.abs_path_to_files.joinpath('detect').joinpath('exp')}/image.jpg")
            return self.convert(img)

    def is_exists(self) -> bool:
        return os.path.exists(self.abs_path_to_files.joinpath('detect').joinpath('exp').joinpath('image.jpg'))

    def clear(self):
        if self.is_exists():
            shutil.rmtree(self.abs_path_to_files.joinpath('detect').joinpath('exp'))

    def convert(self, img) -> bytes:
        buffer = BytesIO()
        img.save(buffer, 'png')
        buffer.seek(0)
        data = buffer.read()
        return base64.b64encode(data).decode()
