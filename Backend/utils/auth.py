from functools import wraps
from flask import session, jsonify


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if "user_id" not in session:
            return jsonify({
                "success": False,
                "message": "Unauthorized"
            }), 401

        return func(*args, **kwargs)

    return wrapper


def role_required(role_id):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            if session.get("role_id") != role_id:

                return jsonify({
                    "success": False,
                    "message": "Access Denied"
                }), 403

            return func(*args, **kwargs)

        return wrapper

    return decorator