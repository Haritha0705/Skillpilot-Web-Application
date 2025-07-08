from flask import Blueprint
from app.controllers.company_controller import CompanyController

company_bp = Blueprint('company',__name__,url_prefix='/v1/api/company')
controller = CompanyController()

@company_bp.route('/company/profile', methods=['GET'])
def get_profile_route():
    return controller.get_profile()

@company_bp.route('/company/profile', methods=['PUT'])
def update_profile_route():
    return controller.update_profile()

@company_bp.route('/company/delete', methods=['DELETE'])
def delete_profile_route():
    return controller.delete_company()