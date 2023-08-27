from api.database import db


class Follows(db.Model):  # type: ignore
    __tablename__ = "follows"

    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    followee_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"{self.followee} follows {self.follower}"

    def __init__(self, followee=None, follower=None, confirmed=False):
        if followee:
            self.followee = followee
        if follower:
            self.follower = follower
        self.confirmed = confirmed

    def registerFollow(self):
        db.session.add(self)
        db.session.commit()

    def saveFollow(self):
        db.session.commit()
