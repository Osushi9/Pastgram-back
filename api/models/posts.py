from datetime import datetime

from api.database import db


class Posts(db.Model):  # type: ignore
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    image_path = db.Column(db.String(80), nullable=False)
    taken_at = db.Column(db.Date, nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    like_counts = db.Column(db.Integer, nullable=False, default=0)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), nullable=False)

    def __repr__(self):
        return f"{self.image_path} by User ID: {self.user_id}"

    def __init__(self, user_id, image_path, taken_at, tag_id):
        self.user_id = user_id
        self.image_path = image_path
        self.taken_at = taken_at
        self.tag_id = tag_id

    def registerPost(self):
        db.session.add(self)
        db.session.commit()
