from .auth import auth_bp
from .student import student_bp
from .admin import admin_bp
from .professional import professional_bp
from .company import company_bp

def auth_routes(app):
    app.register_blueprint(auth_bp)

def student_routes(app):
    app.student_blueprint(student_bp)

def admin_routes(app):
    app.admin_blueprint(admin_bp)

def company_routes(app):
    app.professional_blueprint(professional_bp)

def professional_routes(app):
    app.company_blueprint(company_bp)