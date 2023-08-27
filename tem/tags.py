from api.database import db


class Tags(db.Model):  # type: ignore
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    limit = db.Column(db.Integer)

    posts = db.relationship("Posts", backref="tags", lazy="dynamic")
