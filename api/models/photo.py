from api.database import db, ma
from datetime import datetime
from models.tag import Tag

class Photo(db.Model):  # type: ignore
    __tablename__ = "photo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    path = db.Column(db.String(80), nullable=False, unique=True)
    created_at = db.Column(db.Date, nullable=False)
    uploaded_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    likes = db.Column(db.Integer, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    comments = db.relationship('Comment', backref='photo', lazy='dynamic')

    def __repr__(self):
        return f"<Photo #{self.id} user id:{self.user_id} likes:{self.likes} created at:{self.created_at} uploaded at:{self.uploaded_at}>"
    
    def getPhotos(tag_id):
        photos = Tag.query.get(tag_id).photos.all()

        if photos == None:
            return []
        else:
            return photos
        
    def getPhotoInfo(id):
        return db.session.query(Photo).get(id)
    
class PhotoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Photo
        fields = ("path", "created_at", "likes")
