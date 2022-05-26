from flask import Blueprint

images = Blueprint('images', __name__)


@images.route('/images', methods=['POST'])
def upload_image():
    return "<p>Works!</p>"


@images.route('/images', methods=['GET'])
def get_image():
    return "<p>Works GET!</p>"
