from flask import Blueprint
from app.controllers.student_controller import StudentController

student_bp = Blueprint('student',__name__,url_prefix='/v1/api/student')
controller = StudentController()

@student_bp.route('/student/profile', methods=['GET'])
def get_profile_route():
    return controller.get_profile()

@student_bp.route('/student/profile', methods=['PUT'])
def update_profile_route():
    return controller.update_profile()

@student_bp.route('/student/delete', methods=['DELETE'])
def delete_profile_route():
    return controller.delete_student()