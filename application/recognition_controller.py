from flask import Blueprint, send_file
from flask_classy import FlaskView, route, request

from application.Config import recognition_service
from application.recognition_response import RecognitionResponse

images = Blueprint('images', __name__)


class RecognitionController(FlaskView):

    def __init__(self):
        self.__service = recognition_service()

    @route('/images', methods=['POST'])
    def upload_image(self):
        try:
            self.__service.clear()
            image = request.files['image'].read()
            return self.__service.send_image(image).to_json()
        except Exception as e:
           return RecognitionResponse.get_fail_response(str(e)).to_json()

    @route('/images', methods=['GET'])
    def get_recognized_image(self):
        try:
            return send_file(self.__service.load_image(), mimetype='image/jpg')
        except Exception as e:
            return RecognitionResponse.get_fail_response(str(e)).to_json()

    @route('/', methods=['GET'])
    def get_image(self):
        with open("src/application/resources/index.html", "r") as html_file:
            return html_file.read()
