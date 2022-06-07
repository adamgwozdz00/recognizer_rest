from flask import Flask
from flask_cors import CORS

from src.application.recognition_controller import RecognitionController

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
controller = RecognitionController()
controller.register(app, route_base='/')


def run():
    app.run('0.0.0.0', 5001, False)


if __name__ == '__main__':
    run()
