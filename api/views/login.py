from flask import Blueprint, request, jsonify
from api.models.user import User
from flask_login import login_required, login_user, logout_user, current_user


login = Blueprint("login", __name__)


@login.route("/", methods=["POST"])
def id_login():
    data = request.json

    posted_id = data.get("id")
    posted_password = data.get("password")

    user = User.query.filter_by(id=posted_id).first()

    if user and user.checkPassword(posted_password):
        login_user(user)
        response_data = {
            "message": "Authentication successful",
            "token": current_user.id,
        }
        return jsonify(response_data), 200
    else:
        response_data = {"message": "Authentication failed"}
        return jsonify(response_data), 401


@login.route("/signup", methods=["POST"])
def signup():
    data = request.json

    posted_id = data.get("id")
    posted_profile_name = data.get("profile_name")
    posted_password = data.get("password")

    user = User(
        posted_id,
        posted_profile_name,
        posted_password,
    )
    user.registerUser()

    return jsonify({"message": "User created successfully"}), 201


@login.route("/logout")
def logout():
    print(current_user.is_authenticated)
    if current_user.is_authenticated:
        logout_user()  # ユーザーをログアウトさせる
    return jsonify({"message": "User logged out"}), 200


@login.route("/test", methods=["GET"])
@login_required
def test():
    return jsonify({"message": "test"}), 200