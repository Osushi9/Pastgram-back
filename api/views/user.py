from flask import Blueprint, request, make_response, jsonify
from api.models import User, UserSchema
import json

# ルーティング設定
user_router = Blueprint("user_router", __name__)


@user_router.route("/users", methods=["GET"])
def getUserList():
    users = User.getUserList()
    user_schema = UserSchema(many=True)

    return make_response(jsonify({"code": 200, "users": user_schema.dump(users)}))


@user_router.route("/users", methods=["POST"])
def registerUser():
    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)

    User.registerUser(userData)