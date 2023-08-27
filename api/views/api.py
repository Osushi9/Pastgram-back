from flask import Blueprint, request, jsonify
from api.lib.user import get_current_user_id, request_follow, accept_follow
from api.lib.post import add_comment, add_like, remove_like

api = Blueprint("api", __name__)

@api.route("/comment", methods=["POST"])
def comment():
    post_id = int(request.form.get("post_id"))
    content = request.form.get("content")

    user_id = get_current_user_id()

    add_comment(post_id, user_id, content)

    return '', 200

@api.route("/like", methods=["POST"])
def like():
    post_id = int(request.form.get("post_id"))

    user_id = get_current_user_id()
    add_like(post_id, user_id)

    return '', 200

@api.route("/unlike", methods=["POST"])
def unlike():
    post_id = int(request.form.get("post_id"))

    user_id = get_current_user_id()
    remove_like(post_id, user_id)

    return '', 200

@api.route("/follow", methods=["POST"])
def follow():
    follower_id = int(request.form.get("follower_id"))

    followee_id = get_current_user_id()
    request_follow(followee_id, follower_id)

    return '', 200

@api.route("/accept", methods=["POST"])
def accept():
    followee_id = int(request.form.get("followee_id"))

    follower_id = get_current_user_id()
    accept_follow(followee_id, follower_id)

    return '', 200
