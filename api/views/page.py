from flask import Blueprint, jsonify, request
import json

from api.lib.post import *
from api.lib.theme import *
from api.lib.user import *

# ルーティング設定
page = Blueprint("page", __name__)


@page.route("/", methods=["GET"])
def index():
    if get_current_user_id() is not None:
        return jsonify({"message": "Hello World!"}), 200
    else:
        return jsonify({"message": "User not logged in"}), 401

@page.route("/header", methods=["GET"])
def getHeaderInfo():
    tag = get_current_tag()
    limit = get_current_limit()

    response = {
        "tag": tag,
        "limit": limit
    }

    return jsonify(response)

@page.route("/home", methods=["GET"])
def getPostList():
    current_user_id = get_current_user_id()

    followee_ids = get_followee_ids(current_user_id)

    thumnail_fields = ["id", "latest_create", "latest_path", "amount"]
    thumnails = map(lambda id: get_thumnail(id, fields=thumnail_fields), followee_ids)
    thumnails = list(filter(lambda x: x is not None, thumnails))

    response = {
        "thumnails": thumnails
    }

    return jsonify(response)


@page.route("/header", methods=["GET"])
def getHeader():
    response = {"tag": get_current_tag(), "limit": get_current_limit()}
    return jsonify(response)


@page.route("/post", methods=["POST"])
def createPost():
    image_path = request.form.get("image_path")
    taken_at = request.form.get("taken_at")

    current_user_id = get_current_user_id()

    post_fields = ["id", "image_path", "taken_at"]
    post = create_post(current_user_id, image_path, taken_at, fields=post_fields)

    response = {"post": post}

    return jsonify(response)


@page.route("/post", methods=["GET"])
def getPosts():
    user_id = int(request.args.get("user_id"))

    user_fields = ["id", "name", "icon_path"]
    user = get_user(user_id, fields=user_fields)

    post_fields = ["id", "image_path", "like_counts", "comments"]
    posts = get_posts(user_id, fields=post_fields)

    response = {
        "user": user,
        "posts": posts
    }

    return jsonify(response)


@page.route("/profile", methods=["GET"])
def getProfile():
    user_id = int(request.args.get("user_id"))

    user_fields = ["id", "name", "icon_path", "followee_amount", "follower_amount"]
    user = get_user(user_id, fields=user_fields)

    post_fields = ["id", "taken_at", "image_path"]
    posts = get_posts(user_id, fields=post_fields)

    response = {"user": user, "posts": posts}

    return jsonify(response)


@page.route("/profile", methods=["POST"])
def updateProfile():
    name = request.form.get("name")
    password = request.form.get("password")
    profile_name = request.form.get("profile_name")
    icon_path = request.form.get("icon_path")

    current_user_id = get_current_user_id()

    user_fields = ["id", "name", "profile_name", "icon_path"]
    user = update_user(
        current_user_id, name, password, profile_name, icon_path, fields=user_fields
    )

    response = {"user": user}

    return jsonify(response)


@page.route("/followee", methods=["GET"])
def getFollowee():
    user_id = int(request.args.get("user_id"))

    user_fields = ["name", "icon_path"]
    followees = get_followees(user_id, fields=user_fields)

    response = {"users": followees}

    return jsonify(response)


@page.route("/follower", methods=["GET"])
def getFollower():
    user_id = int(request.args.get("user_id"))

    user_fields = ["name", "icon_path"]
    followers = get_followers(user_id, fields=user_fields)

    response = {"users": followers}

    return jsonify(response)


@page.route("/users", methods=["GET"])
def searchUser():
    query = request.args.get("query")

    user_fields = ["id", "name", "icon_path"]
    users = search_users(query, fields=user_fields)

    response = {"users": users}

    return jsonify(response)
