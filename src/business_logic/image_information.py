class ImageInformation:
    def __init__(self, what: str, accuracy: float):
        self.__what = what
        self.__accuracy = accuracy

    def get_what(self) -> str:
        return self.__what

    def get_accuracy(self) -> float:
        return self.__accuracy

    def is_empty(self):
        return self.__what == ""

    @staticmethod
    def create_empty() -> any:
        return ImageInformation("", 0)
