from api.database import db, ma
from datetime import datetime
from models.follow import Follow


class User(db.Model):  # type: ignore
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    profile_name = db.Column(db.String(50), default=name)
    password = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50))
    comments = db.relationship('Comment', backref='user', lazy='dynamic')
    photos = db.relationship('Photo', backref='user', lazy='dynamic')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    

    def __repr__(self):
        return f"<User #{self.id}: {self.profile_name}@{self.name} created at: {self.created_at}>"

    def getUserList():  # type: ignore
        # select * from users
        user_list = db.session.query(User).all()

        if user_list == None:
            return []
        else:
            return user_list

    def registerUser(user):
        record = User(
            name=user["name"],
            password=user["password"],
        )

        # insert into users(name, password) values(...)
        db.session.add(record)
        db.session.commit()

        return user
    
    def getFollowers(id, confirmed):
        followers = Follow.query.filter_by(followee_id=id, confirmed=confirmed) 
        
        if followers == None:
            return []
        else:
            return followers
    

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("name", "profile_name", "password", "icon", "followers", "following")
