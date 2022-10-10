from flask import Flask
from flask_restx import Api


class Server:
    """Configures flask app and api for building with swagger"""
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.api = Api(
            self.app,
            default="Endpoints",
            default_label="from API",
            version="v0.2.3",
            title="Grupo SBF Challenge API",
            doc="/docs"
        )

    @staticmethod
    def run(app) -> None:
        """Runs the application"""
        app.run(
            debug=True,
            host="0.0.0.0",
            port=8465
        )


server = Server()  # Server class sigleton
