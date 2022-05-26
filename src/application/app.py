from flask import Flask
from application.image_controller import images

app = Flask(__name__)
app.register_blueprint(images)