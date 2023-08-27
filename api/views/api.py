from flask import Blueprint, request, jsonify
from api.lib.user import get_current_user_id, request_follow, accept_follow

api = Blueprint("api", __name__)

@api.route("/follow", methods=["POST"])
def follow():
    followee_id = get_current_user_id()
    follower_id = int(request.form.get("follower_id"))
    request_follow(followee_id, follower_id)

    return '', 200

@api.route("/accept", methods=["POST"])
def accept():
    follower_id = get_current_user_id()
    followee_id = int(request.form.get("followee_id"))
    accept_follow(followee_id, follower_id)

    return '', 200
