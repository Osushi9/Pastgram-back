from api.models.posts import Posts

from .mock import *
from .schema import Schema

commentSchema = Schema()


def get_comments(draft):
    comment_field = ["content", "time"]
    return [commentSchema.marshall(comment1, comment_field)]


postSchema = Schema(comments=get_comments)


def get_post(post_id, fields=["id", "image_path", "taken_at"]):
    post = Posts.query.filter_by(id=post_id).first()
    return postSchema.marshall(post, fields)


def get_posts(user_id, fields=["id", "image_path", "taken_at"]):
    posts = Posts.query.filter_by(user_id=user_id).all()
    return postSchema.marshall_many(posts, fields)


def create_post(user_id, image_path, taken_at, fields=["id", "image_path", "taken_at"]):
    post = Posts(user_id, image_path, taken_at)

    return postSchema.marshall(post, fields)


def get_thumnail(
    user_id, fields=["id", "latest_taken_at", "latest_image_path", "amount"]
):
    posts = Posts.query.filter_by(user_id=user_id).all()
    latest_post = posts.query.order_by(Posts.taken_at.desc()).first()

    latest_taken_at = latest_post.taken_at
    latest_image_path = latest_post.image_path
    amount = len(posts)

    thumnail = {
        "id": user_id,
        "latest_taken_at": latest_taken_at,
        "latest_image_path": latest_image_path,
        "amount": amount,
    }

    return postSchema.marshall_dict(thumnail, fields)

def add_comment(post_id, user_id, content):
    pass

def add_like(post_id, user_id):
    pass

def remove_like(post_id, user_id):
    pass
