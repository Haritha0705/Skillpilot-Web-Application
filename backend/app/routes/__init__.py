from .auth_routes import auth_bp
from .admin_routes import admin_bp
from .student_routes import student_bp
from .professional_routes import professional_bp
from .company_routes import company_bp

all_blueprints = [auth_bp,admin_bp,student_bp,professional_bp,company_bp]