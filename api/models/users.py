from api.database import db
from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy
from api.models.follows import Follows


class Users(db.Model):  # type: ignore
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    profile_name = db.Column(db.String(50))
    password = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    comments = db.relationship("Comments", backref="users", lazy="dynamic")
    posts = db.relationship("Posts", backref="users", lazy="dynamic")
    followee_association = db.relationship(
        "Follows",
        foreign_keys="Follows.follower_id",
        backref="follower",
        lazy="dynamic",
    )
    follower_association = db.relationship(
        "Follows",
        foreign_keys="Follows.followee_id",
        backref="followee",
        lazy="dynamic",
    )

    follows = association_proxy(
        "followee_association",
        "followee",
        creator=lambda followee: Follows(followee=followee),
    )
    followers = association_proxy(
        "follower_association",
        "follower",
        creator=lambda follower: Follows(follower=follower),
    )

    def __repr__(self):
        return f"<User {self.name}>"
