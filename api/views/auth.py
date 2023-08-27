from flask import Blueprint, jsonify, request
from flask_login import current_user, login_user, logout_user

from api.lib.user import *
from api.models.users import Users

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def name_login():
    data = request.json

    posted_name = data.get("name")
    posted_password = data.get("password")

    user = Users.query.filter_by(name=posted_name).first()
    print(user)

    if user and user.checkPassword(posted_password):
        login_user(user)
        response_data = {"message": "Authentication successful"}
        return jsonify(response_data), 200
    else:
        response_data = {"message": "Authentication failed"}
        return jsonify(response_data), 401


@auth.route("/signup", methods=["POST"])
def signup():
    data = request.json

    posted_name = data.get("name")
    posted_profile_name = data.get("profile_name")
    posted_password = data.get("password")

    user = Users(
        name=posted_name,
        profile_name=posted_profile_name,
        password=posted_password,
    )
    user.registerUser()

    return jsonify({"message": "User created successfully"}), 201


@auth.route("/logout", methods=["POST"])
def logout():
    if current_user.is_authenticated:
        logout_user()  # ユーザーをログアウトさせる
    return jsonify({"message": "User logged out"}), 200
