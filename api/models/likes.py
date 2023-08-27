from api.database import db


class Likes(db.Model):  # type: ignore
    __tablename__ = "likes"

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True)
    like_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
