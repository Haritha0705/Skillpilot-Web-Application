from flask import Flask
from flask_login import LoginManager
from app.models import db, User
from app.routes import all_blueprints
from app.config import Config
from dotenv import load_dotenv

load_dotenv()

class AppFactory:
    def __init__(self):
        self.app = Flask(__name__)
        self._configure_app()
        self._init_db()
        self._init_login_manager()
        self._register_blueprints()
        self._create_tables()

    def _configure_app(self):
        self.app.config.from_object(Config)

    def _init_db(self):
        db.init_app(self.app)

    def _init_login_manager(self):
        login_manager = LoginManager()
        login_manager.login_view = 'auth.login'
        login_manager.init_app(self.app)

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

    def _register_blueprints(self):
        for bp in all_blueprints:
            self.app.register_blueprint(bp)

    def _create_tables(self):
        with self.app.app_context():
            db.create_all()

    def get_app(self):
        return self.app

