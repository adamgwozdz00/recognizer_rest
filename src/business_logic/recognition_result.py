from src.business_logic.image_information import ImageInformation


class RecognitionResult:
    def __init__(self, success: bool, info: ImageInformation):
        self.__success = success
        self.__info = info

    def is_success(self) -> bool:
        return self.__success
