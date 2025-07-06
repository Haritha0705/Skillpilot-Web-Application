from flask import Flask,jsonify
from app.config import Config
from app.models import db,bcrypt
from flask_login import LoginManager
from app.models import Student,Professional,Company
from app.routes import auth_routes

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    auth_routes(app)

    @login_manager.user_loader
    def load_user(user_id):
        return (
                Student.query.get(int(user_id)) or
                Professional.query.get(int(user_id)) or
                Company.query.get(int(user_id))
        )

    with app.app_context():
        db.create_all()

    return app