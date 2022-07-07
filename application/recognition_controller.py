from flask import Blueprint, send_file
from flask_classy import FlaskView, route, request

from application.injector import injector
from application.recognition_response import RecognitionResponse

images = Blueprint('images', __name__)


class RecognitionController(FlaskView):

    def __init__(self):
        self.service = injector.inject__recognition_service()

    @route('/images', methods=['POST'])
    def upload_image(self):
        try:
            self.service.clear()
            image = request.files['image'].read()
            return self.service.send_image(image).to_json()
        except Exception as e:
            return RecognitionResponse.get_fail_response(str(e)).to_json()

    @route('/images', methods=['GET'])
    def get_recognized_image(self):
        return self.service.load_image().to_json()

    @route('/', methods=['GET'])
    def get_image(self):
        with open("src/application/resources/index.html", "r") as html_file:
            return html_file.read()
