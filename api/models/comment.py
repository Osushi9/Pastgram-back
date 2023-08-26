from api.database import db, ma

class Comment(db.Model):  # type: ignore
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'))
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"{self.content} by {self.user_name}"
    
class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        fields = ("id","user_id", "user_name", "photo_id", "content", "time")