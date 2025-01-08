from flask import Flask
from flask_login import LoginManager
from app.extensions import db, migrate
from app.routes import register_routes
from app.cli import register_commands
from config import Config
from app.extensions import db, migrate, login_manager


login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."

    register_routes(app)
    register_commands(app)
