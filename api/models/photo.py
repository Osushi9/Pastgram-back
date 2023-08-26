from api.database import db, ma
from datetime import datetime

class Photo(db.Model):  # type: ignore
    __tablename__ = "photo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    path = db.Column(db.String(80), nullable=False, unique=True)
    create_time = db.Column(db.Date, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False, default=datetime.now)
    likes = db.Column(db.Integer, nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    comments = db.relationship('Comment', backref='photo', lazy='dynamic')

    def __repr__(self):
        return f"{self.content} by {self.user_name}"
    
class PhotoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Photo
        fields = ("id","user_Id", "user_name", "path", "create_time", "upload_time", "likes", "tag")

