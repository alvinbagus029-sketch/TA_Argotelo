from flask import Blueprint, request, jsonify

from Backend.services.auth_service import AuthService

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/api/register", methods=["POST"])
def register():

    data = request.get_json()

    result = AuthService.register(data)

    return jsonify(result)


@auth_bp.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()

    result = AuthService.login(data)

    return jsonify(result)


@auth_bp.route("/api/logout", methods=["POST"])
def logout():

    result = AuthService.logout()

    return jsonify(result)


@auth_bp.route("/api/me", methods=["GET"])
def me():

    result = AuthService.me()

    return jsonify(result)