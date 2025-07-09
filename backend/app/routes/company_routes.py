from flask import Blueprint
from app.controllers.company_controller import CompanyController
from flask_login import login_required

company_bp = Blueprint('company',__name__,url_prefix='/v1/api/company')
controller = CompanyController()

@company_bp.route('/profile', methods=['GET'])
@login_required
def get_profile_route():
    return controller.get_profile()

@company_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile_route():
    return controller.update_profile()

@company_bp.route('/delete', methods=['DELETE'])
@login_required
def delete_profile_route():
    return controller.delete_company()