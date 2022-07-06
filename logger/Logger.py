import logging
from pathlib import Path


class Logger:

    def __init__(self, path_to_file: Path):
        self.path_to_file = path_to_file
        self.__setup()
        self.logger = logging.getLogger()

    def info(self, message: str):
        self.logger.info(message)

    def debug(self, message: str):
        self.logger.debug(message)

    def __setup(self):
        logging.basicConfig(
            filename=self.path_to_file,
            format=f'%(asctime)s : %(levelname)s : %(message)s',
            level=logging.DEBUG)
