from flask import request,jsonify,session
from app.models import StudentProfile,ProfessionalProfile,CompanyProfile
from app import db
import sqlalchemy.exc
from flask_login import login_user,logout_user,login_required
from werkzeug.security import check_password_hash,generate_password_hash

class AuthController:

    def register(self):
        try:
            data = request.get_json()
            required_fields = ['username', 'email', 'password', 'role']
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Missing required fields"}), 400

            if data['role'] not in ['student', 'professional','company']:
                return jsonify({"error": "Invalid role"}), 400

            hashed_password = generate_password_hash(data['password'])

            new_user = None

            if data['role'] == 'student':
                existing_student = StudentProfile.query.filter(
                    (StudentProfile.username == data['username']) |
                    (StudentProfile.email == data['email'])
                ).first()
                if existing_student:
                    return jsonify({"error": "Username or Email already exists"}), 409

                new_user = StudentProfile(
                    username=data['username'],
                    email=data['email'],
                    password=hashed_password,
                    role='student',

                    name=data.get('name'),
                    address=data.get('address')
                )

            elif data['role'] == 'professional':
                existing_professional = ProfessionalProfile.query.filter(
                    (ProfessionalProfile.username == data['username']) |
                    (ProfessionalProfile.email == data['email'])
                ).first()
                if existing_professional:
                    return jsonify({"error": "Username or Email already exists"}), 409

                new_user = ProfessionalProfile(
                    username=data['username'],
                    email=data['email'],
                    password=hashed_password,
                    role='professional',

                    skill=data.get('skill'),
                    experience=data.get('experience')
                )

            elif data['role'] == 'company':
                existing_company = CompanyProfile.query.filter(
                    (CompanyProfile.username == data['username']) |
                    (CompanyProfile.email == data['email'])
                ).first()
                if existing_company:
                    return jsonify({"error": "Username or Email already exists"}), 409

                new_user = CompanyProfile(
                    username=data['username'],
                    email=data['email'],
                    password=hashed_password,
                    role='company',

                    skill=data.get('skill'),
                    experience=data.get('experience')
                )

            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)

            return jsonify({"message":"Register successfully"},new_user.to_dict()), 201

        except sqlalchemy.exc.SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({"error": "Database error", "details": str(e)}), 500

        except Exception as e:
            return jsonify({"error": "Unexpected error", "details": str(e)}), 500

    def login(self):
        try:
            data = request.get_json()
            if not data.get('username') or not data.get('password'):
                return jsonify({"error": "Username and password required"}), 400

            username = data['username']
            password = data['password']

            user = (
                    StudentProfile.query.filter_by(username=username).first() or
                    ProfessionalProfile.query.filter_by(username=username).first() or
                    CompanyProfile.query.filter_by(username=username).first()
            )

            if user and check_password_hash(user.password, password):
                login_user(user)
                session['role'] = user.role
                return jsonify({
                    "message": "Logged in successfully",
                    "role": user.role
                }), 200

            return jsonify({"error": "Invalid credentials"}), 401

        except Exception as e:
            return jsonify({"error": "Login failed", "details": str(e)}), 500

    @login_required
    def logout(self):
        try:
            logout_user()
            session.clear()
            return jsonify({"message": "Logged out successfully"})

        except Exception as e:
            return jsonify({"error": "Logout failed", "details": str(e)}), 500
