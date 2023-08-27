from api.database import db

class Follow(db.Model):  # type: ignore
    __tablename__ = "follow"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    followee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    
    followee = db.relationship('User', backref='following', foreign_keys=[followee_id])
    follower = db.relationship('User', backref='followers', foreign_keys=[follower_id])
