from .schema import Schema
from .mock import *

commentSchema = Schema()

def get_comments(draft):
    comment_field = ["content", "time"]
    return [commentSchema.marshall(comment1, comment_field)]

postSchema = Schema(comments=get_comments)

def get_post(post_id, fields=["id", "image_path", "create_at"]):
    post = post[post_id]

    return postSchema.marshall(draft, fields)

def get_posts(user_id, fields=["id", "image_path", "create_at"]):
    return [
        postSchema.marshall(post1, fields),
        postSchema.marshall(post2, fields)
    ]

def create_post(user_id, image_path, create_at, fields=["id", "image_path", "create_at"]):
    post = MockPost(3, user_id, image_path, create_at, 0)
    return postSchema.marshall(post, fields)

def get_thumnail(user_id, fields=["id", "latest_create", "latest_path", "amount"]):
    thumnail = {
        "id": user_id,
        "latest_create": post1.create_at,
        "latest_path": post1.image_path,
        "amount": 2
    }

    return postSchema.marshall_dict(thumnail, fields)
