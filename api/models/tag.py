from api.database import db

class Tag(db.Model):  # type: ignore
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    photos = db.relationship('Photo', backref='tag', lazy='dynamic')
    
    def __repr__(self):
        return f"<Tag #{self.id}: {self.name}"