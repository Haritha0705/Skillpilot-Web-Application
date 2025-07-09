from flask import Blueprint
from app.controllers.admin_controller import AdminController

admin_bp = Blueprint('admin', __name__, url_prefix='/v1/api/admin')
controller = AdminController()

@admin_bp.route('/login', methods=['POST'])
def login_admin():
    return controller.login()

@admin_bp.route('/allCompany', methods=['GET'])
def get_all_company_route():
    return controller.get_all_company()

@admin_bp.route('/allProfessional', methods=['GET'])
def get_all_professional_route():
    return controller.get_all_professionals()

@admin_bp.route('/allStudent', methods=['GET'])
def get_all_student_route():
    return controller.get_all_students()

@admin_bp.route('/company/delete/<int:user_id>', methods=['DELETE'])
def admin_delete_company_route(user_id):
    return controller.admin_delete_company(user_id)

@admin_bp.route('/professional/delete/<int:user_id>', methods=['DELETE'])
def admin_delete_professional_route(user_id):
    return controller.admin_delete_professional(user_id)

@admin_bp.route('/student/delete/<int:user_id>', methods=['DELETE'])
def admin_delete_student_route(user_id):
    return controller.admin_delete_students(user_id)