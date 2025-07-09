from flask import request, jsonify
from flask_login import current_user
from app.models import db, CompanyProfile

class CompanyController:


    def get_profile(self):
        try:
            profile = CompanyProfile.query.get(current_user.id)
            if not profile:
                return jsonify({"error": "Company profile not found"}), 404

            return jsonify({
                "profile": {
                    "name": profile.name,
                    "address": profile.address
                }
            }), 200

        except Exception as e:
            return jsonify({"error": "Failed to fetch profile", "details": str(e)}), 500


    def update_profile(self):
        try:
            data = request.get_json()
            profile = CompanyProfile.query.get(current_user.id)
            if not profile:
                return jsonify({"error": "Company profile not found"}), 404

            profile.name = data.get("name", profile.name)
            profile.address = data.get("address", profile.address)

            db.session.commit()
            return jsonify({"message": "Profile updated successfully"}), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "Failed to update profile", "details": str(e)}), 500


    def delete_company(self):
        try:
            profile = CompanyProfile.query.get(current_user.id)
            if not profile:
                return jsonify({"error": "Company profile not found"}), 404

            db.session.delete(profile)
            db.session.commit()

            return jsonify({"message": "Company deleted successfully"}), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "Failed to delete company", "details": str(e)}), 500

