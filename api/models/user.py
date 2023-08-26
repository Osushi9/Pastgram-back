from api.database import db, ma
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin


class User(db.Model, UserMixin):  # type: ignore
    __tablename__ = "user"

    id = db.Column(db.String(50), primary_key=True, nullable=False, unique=True)
    profile_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User %r>" % self.profile_name

    def __init__(self, id, profile_name, password):
        self.id = id
        self.profile_name = profile_name
        self.password = generate_password_hash(password)

    def registerUser(self):
        # insert into user(profile_name, password) values(...)
        db.session.add(self)
        db.session.commit()

    def checkPassword(self, password):
        return check_password_hash(self.password, password)

    def select_by_id(self, id):
        return db.session.query(User).filter_by(id=id).first()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        fields = ("id", "profile_name", "password")
