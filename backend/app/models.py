from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    # Relationships
    company_profile = db.relationship('CompanyProfile', backref='user', uselist=False)
    professional_profile = db.relationship('ProfessionalProfile', backref='user', uselist=False)
    student_profile = db.relationship('StudentProfile', backref='user', uselist=False)

    def is_admin(self):
        return self.role == 'admin'

class CompanyProfile(db.Model):
    __tablename__ = 'company_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(255))

# Profile for technicians
class ProfessionalProfile(db.Model):
    __tablename__ = 'professional_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    skill = db.Column(db.String(100))
    experience = db.Column(db.String(100))

class StudentProfile(db.Model):
    __tablename__ = 'student_profiles'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    skill = db.Column(db.String(100))
    experience = db.Column(db.String(100))