from flask import Flask
from flask_cors import CORS

from application.injector import injector

from application.recognition_controller import RecognitionController
from business_logic.recognition_runner import RecognitionRunner
from logger.Logger import Logger
from logger.log_path import get_path

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

LOGGER = Logger(get_path())
controller = RecognitionController()

runner = RecognitionRunner(injector.inject_image_recognition_service())
controller.register(app, route_base='/')


def run():
    LOGGER.debug("app run...")
    runner.start()
    app.run('0.0.0.0', 5001, False)


if __name__ == '__main__':
    run()
