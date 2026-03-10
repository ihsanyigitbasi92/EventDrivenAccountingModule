
"""
Initialize the Flask application and configure necessary settings.
"""

from flask import Flask
from config.settings import Config
from app.routes import setup_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    setup_routes(app)
    return app
