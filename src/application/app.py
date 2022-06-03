from flask import Flask

from src.application.recognition_controller import RecognitionController

app = Flask(__name__)
controller = RecognitionController()
controller.register(app, route_base='/')

if __name__ == '__main__':
    app.run('127.0.0.1', 5000, True)
