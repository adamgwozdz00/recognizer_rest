from dataclasses import dataclass


@dataclass
class ImageInformation:
    success: bool
    ex: str

    def is_success(self):
        return self.success

    @classmethod
    def create_fail(cls, ex : str):
        return ImageInformation(False, ex)
