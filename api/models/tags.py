from datetime import datetime
from sqlalchemy import Date
from datetime import timedelta

from api import db


class Tags(db.Model):  # type: ignore
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    limit = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"{self.name}"

    def __init__(self, name, start_date):
        self.name = name
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.limit = start_date_obj + timedelta(days=3)

    def registerTag(self):
        db.session.add(self)
        db.session.commit()
