from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

db = SQLAlchemy()
bcrypt = Bcrypt()

class Student(db.Model, UserMixin):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="student")

    # Additional fields
    full_name = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    education_level = db.Column(db.String(100), nullable=True)
    graduation_year = db.Column(db.String(10), nullable=True)
    university = db.Column(db.String(200), nullable=True)
    skills = db.Column(db.Text, nullable=True)
    interests = db.Column(db.Text, nullable=True)
    resume_url = db.Column(db.String(300), nullable=True)
    profile_picture = db.Column(db.String(300), nullable=True)
    linkedin_profile = db.Column(db.String(300), nullable=True)
    github_profile = db.Column(db.String(300), nullable=True)
    portfolio_url = db.Column(db.String(300), nullable=True)

class Professional(db.Model, UserMixin):
    __tablename__ = 'professionals'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="professional")

    # Additional fields
    full_name = db.Column(db.String(200), nullable=True)
    company_name = db.Column(db.String(200), nullable=True)
    job_title = db.Column(db.String(150), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    industry = db.Column(db.String(100), nullable=True)
    years_of_experience = db.Column(db.String(50), nullable=True)
    linkedin_profile = db.Column(db.String(300), nullable=True)
    website = db.Column(db.String(300), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    profile_picture = db.Column(db.String(300), nullable=True)

class Company(db.Model, UserMixin):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    comname = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="company")

    # Additional fields
    contact_person = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    website = db.Column(db.String(300), nullable=True)
    industry = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    company_size = db.Column(db.String(50), nullable=True)
    description = db.Column(db.Text, nullable=True)
    logo_url = db.Column(db.String(300), nullable=True)
    linkedin_url = db.Column(db.String(300), nullable=True)
