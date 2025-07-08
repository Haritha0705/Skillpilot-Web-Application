from flask import request,jsonify,session
from app.models import User,StudentProfile,ProfessionalProfile,CompanyProfile
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

            existing_user = User.query.filter(
                (User.username == data['username']) | (User.email == data['email'])
            ).first()
            if existing_user:
                return jsonify({"error": "Username or Email already exists"}), 409

            hashed_password = generate_password_hash(data['password'])
            new_user = User(
                username=data['username'],
                email=data['email'],
                password=hashed_password,
                role=data['role']
            )
            db.session.add(new_user)
            db.session.commit()

            if data['role'] == 'student':
                profile = StudentProfile(
                    user_id=new_user.id,
                    name=data.get('name'),
                    address=data.get('address')
                )
                db.session.add(profile)
            elif data['role'] == 'professional':
                profile = ProfessionalProfile(
                    user_id=new_user.id,
                    skill=data.get('skill'),
                    experience=data.get('experience')
                )
                db.session.add(profile)

            elif data['role'] == 'company':
                profile = CompanyProfile(
                    user_id=new_user.id,
                    skill=data.get('skill'),
                    experience=data.get('experience')
                )
                db.session.add(profile)

            db.session.commit()
            login_user(new_user)

            return jsonify({"message":"Register successfully"},new_user), 201

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

            user = User.query.filter_by(username=data['username']).first()
            if user and check_password_hash(user.password, data['password']):
                login_user(user)
                session['role'] = user.role
                return jsonify({"message": "Logged in successfully", "role": user.role}), 200

            return jsonify({"message": "Invalid credentials"}), 401

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
