from flask import Blueprint,request,jsonify
from flask_login import login_required,current_user
from app.models import db

profile_bp = Blueprint("profile",__name__, url_prefix="/v1/api/profile")

@profile_bp.route("/me", methods=["GET"])
@login_required
def get_profile():
    user = current_user

    fields = [
        "id", "username", "comname", "email", "role",
        "gender", "location", "education_level", "university", "graduation_year",
        "skills", "interests", "resume_url", "linkedin_profile",
        "profile_picture", "github_profile", "portfolio_url"
    ]

    profile = {}

    for field in fields:
        if hasattr(user, field):
            if field == "role":
                profile["role"] = user.__class__.__name__.lower()
            elif field == "username":
                profile["username"] = getattr(user, "username", getattr(user, "comname", None))
            else:
                profile[field] = getattr(user, field)

    return jsonify(profile), 200


@profile_bp.route("/me", methods=["PUT"])
@login_required
def update_profile():
    data = request.get_json()
    user = current_user

    fields = [
        "gender", "location", "education_level", "university", "graduation_year",
        "skills", "interests", "resume_url", "linkedin_profile",
        "profile_picture", "github_profile", "portfolio_url"
    ]

    for field in fields:
        if hasattr(user, field) and field in data:
            setattr(user, field, data[field])

    db.session.commit()
    return jsonify({"message": "Profile updated successfully"}), 200

