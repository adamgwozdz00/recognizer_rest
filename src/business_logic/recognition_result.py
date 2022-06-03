from src.business_logic.image_information import ImageInformation


class RecognitionResult:
    def __init__(self, success: bool, info: ImageInformation):
        self.__success = success
        self.__info = info

    @staticmethod
    def create_success(info: ImageInformation) -> any:
        return RecognitionResult(True, info)

    @staticmethod
    def create_fail() -> any:
        return RecognitionResult(False, ImageInformation.create_empty())

    def is_success(self) -> bool:
        return self.__success

    def get_info_what(self) -> str:
        return self.__info.get_what()

    def get_info_accuracy(self) -> float:
        return self.__info.get_accuracy()
