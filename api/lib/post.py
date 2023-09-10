from api.models.comments import Comments
from api.models.posts import Posts

from .schema import Schema

commentSchema = Schema()

def get_comments(user):
    comment_field = ["content", "updated_at"]  # フィールド拡張でやってるので第2引数がとれないでここで指定
    comment = Comments.query.filter_by(user_id=user.id).all()
    return commentSchema.marshall_many(comment, comment_field)

postSchema = Schema(comments=get_comments)

def get_post(post_id, fields=["id", "image_path", "taken_at"]):
    post = Posts.query.filter_by(id=post_id).first()
    return postSchema.marshall(post, fields)

def get_posts(user_id, fields=["id", "image_path", "taken_at"]):
    posts = Posts.query.filter_by(user_id=user_id).all()
    return postSchema.marshall_many(posts, fields)

def create_post(user_id, image_path, taken_at, fields=["id", "image_path", "taken_at"]):
    if user_id is None:
        return {"error": "user_id is required"}
    else:
        post = Posts(user_id, image_path, taken_at)
        post.registerPost()
        return postSchema.marshall(post, fields)

def add_comment(post_id, user_id, content):
    pass

def add_like(post_id, user_id):
    pass

def remove_like(post_id, user_id):
    pass
