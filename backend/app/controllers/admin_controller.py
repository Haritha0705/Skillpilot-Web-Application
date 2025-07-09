from flask import jsonify,request
from app.utils.decorators import admin_required
from app.models import db, CompanyProfile,StudentProfile,ProfessionalProfile
from app.config import Config
from flask_login import login_user, UserMixin

class AdminController(UserMixin):
    def __init__(self):
        self.id = "admin"
        self.role = "admin"
        self.username = Config.ADMIN_USERNAME

    def get_id(self):
        return self.id

    def login(self):
        try:
            data = request.get_json()
            if not data or not data.get('username') or not data.get('password'):
                return jsonify({"error": "Username and password are required"}), 400

            username = data.get('username')
            password = data.get('password')

            if username == Config.ADMIN_USERNAME and password == Config.ADMIN_PASSWORD:
                admin_user = AdminController()
                login_user(admin_user)
                return jsonify({"message": "Logged in successfully"}), 200

            return jsonify({"error": "Invalid credentials"}), 401

        except Exception as e:
            return jsonify({
                "error": "Login failed",
                "details": str(e)
            }), 500


    @admin_required
    def get_all_students(self):
        try:
            students = StudentProfile.query.all()
            return jsonify([s.to_dict() for s in students]), 200
        except Exception as e:
            return jsonify({
                "error": "Login failed",
                "details": str(e)
            }), 500


    @admin_required
    def get_all_professionals(self):
        try:
            professionals = ProfessionalProfile.query.all()
            return jsonify([p.to_dict() for p in professionals]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @admin_required
    def get_all_company(self):
        try:
            companys = CompanyProfile.query.all()
            return jsonify([c.to_dict() for c in companys]), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    @admin_required
    def admin_delete_students(self, user_id):
        try:
            student = StudentProfile.query.get(user_id)

            if not student:
                return jsonify({"error": "Student not found"}), 404

            db.session.delete(student)
            db.session.commit()

            return jsonify({"message": "Student deleted by admin"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500


    @admin_required
    def admin_delete_professional(self, user_id):
        try:
            professional = ProfessionalProfile.query.get(user_id)

            if not professional:
                return jsonify({"error": "Professional not found"}), 404

            db.session.delete(professional)
            db.session.commit()

            return jsonify({"message": "Professional deleted by admin"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500


    @admin_required
    def admin_delete_company(self, user_id):
        try:
            company = CompanyProfile.query.get(user_id)

            if not company:
                return jsonify({"error": "Company not found"}), 404

            db.session.delete(company)
            db.session.commit()

            return jsonify({"message": "Company deleted by admin"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
