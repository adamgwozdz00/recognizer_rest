import pathlib
import subprocess

from business_logic.ai_service import AIService
from logger.Logger import Logger
from logger.log_path import get_path


class AIServiceAdapter(AIService):
    abs_path = pathlib.Path(__file__).parent.parent.joinpath("detect.sh")
    logger : Logger = Logger(get_path())

    def work(self) -> any:
        self.logger.debug('Ask yolo for detect data...')
        subprocess.run(["sh", f"{self.abs_path}"])
