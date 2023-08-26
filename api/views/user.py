from flask import Blueprint, request, make_response, jsonify
from api.models import User, UserSchema
import json

# ルーティング設定
user_router = Blueprint("user_router", __name__)
user_schema = UserSchema(many=True)

@user_router.route("/users", methods=["GET"])
def getUserList():
    users = User.getUserList()
    
    return make_response(jsonify({"code": 200, "users": user_schema.dump(users)}))


@user_router.route("/users", methods=["POST"])
def registerUser():
    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    userData = json.loads(jsonData)

    User.registerUser(userData)
    
@user_router.route("/profile", methods=["GET"])
def getUserProfile(id):
    user = User.query.get(id)
    if user == None:
        return make_response(jsonify({"code": 400, "message": "User doesn't exist."}))
    else:
        return make_response(jsonify({"code": 200, "user": user_schema.dump(user)}))