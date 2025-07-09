from flask import Blueprint
from app.controllers.student_controller import StudentController
from flask_login import login_required

student_bp = Blueprint('student',__name__,url_prefix='/v1/api/student')
controller = StudentController()

@student_bp.route('/profile', methods=['GET'])
@login_required
def get_profile_route():
    return controller.get_profile()

@student_bp.route('/profile', methods=['PUT'])
@login_required
def update_profile_route():
    return controller.update_profile()

@student_bp.route('/delete', methods=['DELETE'])
@login_required
def delete_profile_route():
    return controller.delete_student()