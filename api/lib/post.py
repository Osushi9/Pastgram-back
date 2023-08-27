from .schema import Schema
from .mock import *
from .user import userSchema

commentSchema = Schema()

def get_user(post):
    user_id = post.user_id
    user = user1
    user_field = ["id", "name", "icon_path"]
    return userSchema.marshall(user, user_field)

def get_comments(draft):
    comment_field = ["content", "time"]
    return [commentSchema.marshall(comment1, comment_field)]

postSchema = Schema(comments=get_comments, user=get_user)

def get_post(post_id, fields=["id", "image_path", "taken_at"]):
    post = posts[post_id]

    return postSchema.marshall(post, fields)

def get_posts(user_id, fields=["id", "image_path", "taken_at"]):
    return [
        postSchema.marshall(post1, fields),
        postSchema.marshall(post2, fields)
    ]

def create_post(user_id, image_path, taken_at, fields=["id", "image_path", "taken_at"]):
    post = MockPost(3, user_id, image_path, taken_at, 0)
    return postSchema.marshall(post, fields)

def get_thumnail(user_id, fields=["id", "latest_create", "latest_path", "amount"]):
    thumnail = {
        "id": user_id,
        "latest_create": post1.taken_at,
        "latest_path": post1.image_path,
        "amount": 2
    }

    return postSchema.marshall_dict(thumnail, fields)

def get_post_detail(post_id, fields=["id", "image_path", "taken_at"]):
    return postSchema.marshall(post, fields)