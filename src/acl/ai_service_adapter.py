import pathlib
import subprocess

from src.business_logic.ai_service import AIService


class AIServiceAdapter(AIService):
    # abs_path = str(pathlib.Path(__file__).parent.parent.parent.joinpath('yolov5').joinpath('detect.py'))
    # weights = str(
    #     pathlib.Path(__file__).parent.parent.parent.joinpath('yolov5').joinpath("runs/train/exp/weights/best.pt"))
    abs_path = '../../detect.sh'

    def work(self, image_path: str) -> any:
        # conf = 0.3
        # subprocess.run(
        #     ["python3", f"{self.abs_path} --weights {self.weights} --img 480 --conf {conf} --source {image_path}"])
        subprocess.run(["sh",f"{self.abs_path}"])
