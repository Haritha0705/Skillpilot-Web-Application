from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class StudentProfile(UserMixin, db.Model):
    __tablename__ = 'student_profiles'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='student')

    name = db.Column(db.String(100))
    address = db.Column(db.String(200))

    def get_id(self):
        return str(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "name": self.name,
            "address": self.address
        }


class ProfessionalProfile(UserMixin, db.Model):
    __tablename__ = 'professional_profiles'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='professional')

    skill = db.Column(db.String(200))
    experience = db.Column(db.String(200))

    def get_id(self):
        return str(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "skill": self.skill,
            "experience": self.experience
        }


class CompanyProfile(UserMixin, db.Model):
    __tablename__ = 'company_profiles'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='company')

    skill = db.Column(db.String(200))
    experience = db.Column(db.String(200))

    def get_id(self):
        return str(self.id)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "skill": self.skill,
            "experience": self.experience
        }
