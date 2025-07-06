from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from app.models import Student,Professional,Company,bcrypt,db

auth_bp = Blueprint('auth', __name__, url_prefix='/v1/api/auth')

#Register
@auth_bp.route('/register',methods=["POST"])
def register():

    data = request.get_json()

    # Basic input validation
    required_fields = ["username", "email", "password","role"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    username = data["username"]
    email = data["email"]
    password = data["password"]
    role = data["role"].lower()

    # Hash password
    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

    # Choose model based on role
    if role == "student":
        if Student.query.filter((Student.username == username) | (Student.email == email)).first():
            return jsonify({"error": "Username or email already exists"}), 409
        user = Student(username=username, email=email, password=hashed_pw)
    elif role == "professional":
        if Professional.query.filter((Professional.username == username) | (Professional.email == email)).first():
            return jsonify({"error": "Username or email already exists"}), 409
        user = Professional(username=username, email=email, password=hashed_pw)
    elif role == "company":
        if Company.query.filter((Company.comname == username) | (Company.email == email)).first():
            return jsonify({"error": "Company name or email already exists"}), 409
        user = Company(comname=username, email=email, password=hashed_pw)
    else:
        return jsonify({"error": "Invalid role"}), 400

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

#Login
@auth_bp.route('/login',methods=["POST"])
def login():
    data = request.get_json()
    role = data.get("role")
    email = data.get("email")
    password = data.get("password")

    if not role or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    email = data["email"]
    password = data["password"]
    role = data["role"].lower()

    if role == "student":
        user = Student.query.filter_by(email=email).first()
    elif role == "professional":
        user = Professional.query.filter_by(email=email).first()
    elif role == "company":
        user = Company.query.filter_by(email=email).first()
    else:
        return jsonify({"error": "Invalid role"}), 400

    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": f"{role.capitalize()} logged in successfully"}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

#Logout
@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "User logged out successfully"}), 200

