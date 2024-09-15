from flask import Flask
from .config import Config
from .routes import blog, home
from flask_sqlalchemy import SQLAlchemy
import json
import os
from .models.Blog import Blog, db

def create_app():
    app = Flask(__name__)

    # database
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # load routes
    app.register_blueprint(home.bp)
    app.register_blueprint(blog.bp)

    # preload database with fake test data. 
    if app.config['ENV'] == 'development':
        preload_database_with_test_data(app, db)

    # return app to run
    return app

def preload_database_with_test_data(app, db):
    with app.app_context():
        # Assuming the JSON file is located in the same directory as this script
        json_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tests', 'test_data.json')
        
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        
        for item in data:
            if not Blog.exists(item['title']):
                db_object = Blog(**item)
                db.session.add(db_object)
            
        db.session.commit()