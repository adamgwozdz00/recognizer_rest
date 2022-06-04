from flask import Flask

from src.application.recognition_controller import RecognitionController

app = Flask(__name__)
controller = RecognitionController()
controller.register(app, route_base='/')


def run():
    app.run('0.0.0.0', 5001, False)


if __name__ == '__main__':
    run()
