from api.models.comments import Comments
from api.models.posts import Posts

from .schema import Schema
from .user import userSchema, get_user

commentSchema = Schema()

def get_user_by_post(post):
    user_id = post.user_id
    user_field = ["id", "name", "icon_path"]
    return get_user(user_id, user_field)

def get_comments(post):
    comment_field = ["content", "time"]  # フィールド拡張でやってるので第2引数がとれないでここで指定
    comment = Comments.query.filter_by(post_id=post.id).all()
    return commentSchema.marshall_many(comment, comment_field)

postSchema = Schema(comments=get_comments, user=get_user_by_post)

def get_post(post_id, fields=["id", "image_path", "taken_at"]):
    post = Posts.query.filter_by(id=post_id).first()

    return postSchema.marshall(post, fields)


def get_posts(user_id, fields=["id", "image_path", "taken_at"]):
    posts = Posts.query.filter_by(user_id=user_id).all()
    return postSchema.marshall_many(posts, fields)


def create_post(user_id, image_path, taken_at, fields=["id", "image_path", "taken_at"]):
    post = Posts(user_id, image_path, taken_at)
    post.registerPost()

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
    comment = Comments(post_id, user_id, content)
    comment.registerComment()

def add_like(post_id, user_id):
    post = Posts.query.filter_by(id=post_id).first()
    post.like_counts += 1
    post.savePost()

def remove_like(post_id, user_id):
    post = Posts.query.filter_by(id=post_id).first()
    post.like_counts -= 1
    post.savePost()
