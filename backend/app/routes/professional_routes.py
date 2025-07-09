from flask import Blueprint
from flask_login import login_required
from app.controllers.professional_controller import ProfessionalController

professional_bp = Blueprint('professional',__name__,url_prefix='/v1/api/professional')
controller = ProfessionalController()

@professional_bp.route('/profile', methods=['GET'])
@login_required
def get_profile_route():
    return controller.get_profile()

@professional_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile_route():
    return controller.update_profile()

@professional_bp.route('/delete', methods=['DELETE'])
@login_required
def delete_profile_route():
    return controller.delete_professional()