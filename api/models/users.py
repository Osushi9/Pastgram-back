from datetime import datetime

from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin

from api.database import db


class Users(db.Model, UserMixin):  # type: ignore
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    profile_name = db.Column(db.String(50))
    password = db.Column(db.String(255), nullable=False)
    icon_path = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User %r>" % self.profile_name

    def __init__(self, name, profile_name, password):
        self.name = name
        self.profile_name = profile_name
        # self.password = generate_password_hash(password).decode("utf-8")
        self.password = password

    def registerUser(self):
        db.session.add(self)
        db.session.commit()

    def saveUser(self):
        db.session.commit()

    def checkPassword(self, password):
        # return check_password_hash(self.password, password)
        return self.password == password

    def select_by_id(self, id):
        return db.session.query(Users).filter_by(id=id).first()
