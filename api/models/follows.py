from api.database import db


class Follows(db.Model):  # type: ignore
    __tablename__ = "follows"

    followee_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    confirmed = db.Column(db.Boolean)

    def __init__(self, followee=None, follower=None, confirmed=False):
        if followee:
            self.followee = followee
        if follower:
            self.follower = follower
        self.confirmed = confirmed
