from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from . import routes
    app.register_blueprints(routes.bp)
    return app