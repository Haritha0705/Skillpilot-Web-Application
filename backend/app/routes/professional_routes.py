from flask import Blueprint
from app.controllers.professional_controller import ProfessionalController

professional_bp = Blueprint('professional',__name__,url_prefix='/v1/api/professional')
controller = ProfessionalController()

@professional_bp.route('/professional/profile', methods=['GET'])
def get_profile_route():
    return controller.get_profile()

@professional_bp.route('/professional/profile', methods=['PUT'])
def update_profile_route():
    return controller.update_profile()

@professional_bp.route('/professional/delete', methods=['DELETE'])
def delete_profile_route():
    return controller.delete_professional()