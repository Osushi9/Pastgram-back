from api.database import db

class Follow(db.Model):  # type: ignore
    __tablename__ = "follow"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    follow_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    confirmed = db.Column(db.boolean, default=False)
