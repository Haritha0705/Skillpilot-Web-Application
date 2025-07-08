from flask import Blueprint
from app.controllers.admin_controller import AdminController

admin_bp = Blueprint('admin', __name__, url_prefix='/v1/api/admin')
controller = AdminController()

@admin_bp.route('/admin/allCompany', methods=['GET'])
def get_all_company_route():
    return controller.get_all_company()

@admin_bp.route('/admin/allProfessional', methods=['GET'])
def get_all_professional_route():
    return controller.get_all_professionals()

@admin_bp.route('/admin/allStudent', methods=['GET'])
def get_all_student_route():
    return controller.get_all_students()

@admin_bp.route('/admin/company/delete/<int:user_id>', methods=['DELETE'])
def admin_delete_company_route(user_id):
    return controller.admin_delete_company(user_id)

@admin_bp.route('/admin/professional/delete/<int:user_id>', methods=['DELETE'])
def admin_delete_professional_route(user_id):
    return controller.admin_delete_professional(user_id)

@admin_bp.route('/admin/student/delete/<int:user_id>', methods=['DELETE'])
def admin_delete_student_route(user_id):
    return controller.admin_delete_students(user_id)