import datetime

from api import db


class Comments(db.Model):  # type: ignore
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.Text, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        return f"{self.content} by {self.user_name}"

    def __init__(self, post_id, user_id, content):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content

    def registerComment(self):
        db.session.add(self)
        db.session.commit()
