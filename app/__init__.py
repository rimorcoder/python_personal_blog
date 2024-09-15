from flask import Flask
from .config import Config
from .routes import blog, home

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(home.bp)
    app.register_blueprint(blog.bp)

    return app