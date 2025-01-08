from functools import wraps
from flask import request, jsonify
from flask_login import current_user
from app.models import Permission

def permission_required(permission_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                return jsonify({"error": "Authentication required"}), 401

            permission = Permission.query.filter_by(name=permission_name).first()
            if not permission or permission not in current_user.permissions:
                return jsonify({"error": "Permission denied"}), 403

            return f(*args, **kwargs)
        return decorated_function
    return decorator
