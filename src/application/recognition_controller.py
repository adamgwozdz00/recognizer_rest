from flask import Blueprint
from flask_classy import FlaskView, route, request

from src.application.Config import recognition_service

images = Blueprint('images', __name__)


class RecognitionController(FlaskView):

    def __init__(self):
        self.__service = recognition_service()

    @route('/images', methods=['POST'])
    def upload_image(self):
        image = request.files['image'].read()
        return self.__service.recognize(image).to_json()

    @route('/', methods=['GET'])
    def get_image(self):
        with open("src/application/resources/index.html", "r") as html_file:
            return html_file.read()
