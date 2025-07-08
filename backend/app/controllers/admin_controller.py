from flask import jsonify
from app.utils.decorators import admin_required
from app.models import db, CompanyProfile,StudentProfile,ProfessionalProfile , User

class AdminController:

    @admin_required
    def get_all_students(self):
        try:
            students = StudentProfile.query.all()
            return jsonify([{"id": s.id, "name": s.name} for s in students])
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @admin_required
    def get_all_professionals(self):
        try:
            professionals = ProfessionalProfile.query.all()
            return jsonify([{"id": p.id, "name": p.name} for p in professionals])
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @admin_required
    def get_all_company(self):
        try:
            companys = CompanyProfile.query.all()
            return jsonify([{"id": c.id, "name": c.name} for c in companys])
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @admin_required
    def admin_delete_students(self, user_id):
        try:
            student = StudentProfile.query.filter_by(user_id=user_id).first()
            user = User.query.get(user_id)

            if not student or not user:
                return jsonify({"error": "Student not found"}), 404

            db.session.delete(student)
            db.session.delete(user)
            db.session.commit()

            return jsonify({"message": "Student deleted by admin"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @admin_required
    def admin_delete_professional(self, user_id):
        try:
            professional = ProfessionalProfile.query.filter_by(user_id=user_id).first()
            user = User.query.get(user_id)

            if not professional or not user:
                return jsonify({"error": "Professional not found"}), 404

            db.session.delete(professional)
            db.session.delete(user)
            db.session.commit()

            return jsonify({"message": "Professional deleted by admin"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

    @admin_required
    def admin_delete_company(self, user_id):
        try:
            company = CompanyProfile.query.filter_by(user_id=user_id).first()
            user = User.query.get(user_id)

            if not company or not user:
                return jsonify({"error": "Company not found"}), 404

            db.session.delete(company)
            db.session.delete(user)
            db.session.commit()

            return jsonify({"message": "Company deleted by admin"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
