from flask import Flask
from .config import Config
from .routes import auth, blog, home, search, admin
import json
import os
from .models.Blog import Blog
from .models.User import User
from .extensions import login_manager, db
from werkzeug.security import generate_password_hash
import time

def create_app():
    app = Flask(__name__)

    # authentication
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    # database
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Create initial admin user
    create_initial_admin_user(app, db)

    # load routes
    app.register_blueprint(home.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(search.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)

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
                time.sleep(0.1)
            
        db.session.commit()

def create_initial_admin_user(app, db):
    with app.app_context():
        # Check if the admin user already exists
        admin_user = User.query.filter_by(username='admin').first()
        if not admin_user:
            # Create the admin user
            admin_user = User(
                username="admin",
                password=generate_password_hash("password") #just for demo purposes, dont use this for real
            )
            db.session.add(admin_user)
            db.session.commit()