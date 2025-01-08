from app.routes.auth import auth_bp
from app.routes.users import users_bp
from app.routes.main import main_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(main_bp)

