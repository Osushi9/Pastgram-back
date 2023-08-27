from api.database import db, ma
from datetime import datetime

class Comment(db.Model):  # type: ignore
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'))
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"<Comment #{self.id}: {self.content} user id:{self.user_id}>"
    
class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        fields = ("user_id", "content", "time")