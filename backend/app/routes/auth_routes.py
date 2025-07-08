from flask import Blueprint
from app.controllers.auth_controller import AuthController

auth_bp = Blueprint('auth', __name__, url_prefix='/v1/api/auth')
controller = AuthController()

@auth_bp.route('/login', methods=['POST'])
def login_route():
    return controller.login()

@auth_bp.route('/register', methods=['POST'])
def register_route():
    return controller.register()

@auth_bp.route('/logout', methods=['POST'])
def logout_route():
    return controller.logout()