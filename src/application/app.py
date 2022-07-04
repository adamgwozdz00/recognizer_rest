from flask import Flask
from flask_cors import CORS

from src.acl.Config import image_recognition_service
from src.application.recognition_controller import RecognitionController
from src.business_logic.recognition_runner import RecognitionRunner

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
controller = RecognitionController()
runner = RecognitionRunner(image_recognition_service())
controller.register(app, route_base='/')


def run():
    runner.start()
    app.run('0.0.0.0', 5001, False)


if __name__ == '__main__':
    run()
