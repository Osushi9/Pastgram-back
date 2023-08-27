from flask import Blueprint, request, jsonify
from api.models import User, UserSchema
import json
from api.lib.theme import get_current_tag, get_current_limit
from api.lib.user import get_current_user, get_followee_ids, get_user, get_followees, get_followers, search_users
from api.lib.post import get_thumnail, create_post, get_post, get_posts

# ルーティング設定
page_router = Blueprint("page_router", __name__)

@page_router.route("/home", methods=["GET"])
def getUserList():
    user_fields = ["id"]
    current_user = get_current_user(fields=user_fields)

    tag = get_current_tag()
    limit = get_current_limit()

    followee_ids = get_followee_ids(current_user.id)

    thumnail_fields = ["id", "latest_create", "latest_path", "amount"]
    thumnails = map(lambda id: get_thumnail(id, fields=thumnail_fields), followee_ids)
    thumnails = filter(lambda x: x is not None, thumnails)

    response = {
        "tag": tag,
        "limit": limit,
        "thumnails": thumnails
    }

    return jsonify(response)

@page_router.route("/post", methods=["POST"])
def createPost():
    image_path = request.json["image_path"]
    create_at = request.json["create_at"]

    user_fields = ["id"]
    current_user = get_current_user(fields=user_fields)

    post_fields = ["id", "image_path", "create_at"]
    post = create_post(current_user.id, image_path, create_at, fields=post_fields)

    response = {
        "id": post.id,
        "create_at": post.create_at,
        "image_path": post.image_path
    }

    return jsonify(response)

@page_router.route("/posts", methods=["GET"])
def getPosts():
    user_id = request.args.get("user_id")

    user_fields = ["id", "name", "icon_path"]
    user = get_user(user_id, fields=user_fields)

    post_fields = ["id", "image_path", "likes", "comments"]
    posts = get_posts(user.id, fields=post_fields)

    tag = get_current_tag()
    limit = get_current_limit()

    response = {
        "tag": tag,
        "limit": limit,
        "user": user,
        "posts": posts
    }

    return jsonify(response)

@page_router.route("/profile", methods=["GET"])
def getProfile():
    user_id = request.args.get("user_id")

    user_fields = ["id", "name", "icon_path", "follow_amount", "follower_amount"]
    user = get_user(user_id, fields=user_fields)

    post_fields = ["id", "create_at", "image_path"]
    posts = get_posts(user.id, fields=post_fields)

    response = {
        "user": user,
        "posts": posts
    }

    return jsonify(response)

@page_router.route("/profile", methods=["POST"])
def updateProfile():
    name = request.json["name"]
    password = request.json["password"]
    profile_name = request.json["profile_name"]
    icon_path = request.json["icon_path"]

    user_fields = ["id"]
    current_user = get_current_user(fields=user_fields)

    user_fields = ["id", "name", "profile_name", "icon_path"]
    user = update_user(current_user.id, name, password, profile_name, icon_path)

    response = {
        "user": user
    }

    return jsonify(response)

@page_router.route("/followee", methods=["GET"])
def getFollowee():
    user_id = request.args.get("user_id")

    user_fields = ["name", "icon_path"]
    followees = get_followees(user_id, fields=user_fields)

    response = {
        "users": followees
    }

    return jsonify(response)

@page_router.route("/follower", methods=["GET"])
def getFollower():
    user_id = request.args.get("user_id")

    user_fields = ["name", "icon_path"]
    followers = get_followers(user_id, fields=user_fields)

    response = {
        "users": followers
    }

    return jsonify(response)

@page_router.route("/users", methods=["GET"])
def searchUser():
    query = request.args.get("query")

    user_fields = ["id", "name", "icon_path"]
    users = search_users(query, fields=user_fields)

    response = {
        "users": users
    }

    return jsonify(response)
