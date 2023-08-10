from flask import Flask
from app.controllers.data_controller import app as TriangulateBlueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(TriangulateBlueprint)
    return app
