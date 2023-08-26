from api.database import db, ma


class User(db.Model):  # type: ignore
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50))
    follow = db.Column(db.Text)
    follower = db.Column(db.Text)
    comments = db.relationship('comment', backref='user', lazy='dynamic')
    photos = db.relationship('photo', backref='user', lazy='dynamic')
    

    def __repr__(self):
        return "<User %r>" % self.name

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


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id","name", "password", "icon", "follow", "followers")
