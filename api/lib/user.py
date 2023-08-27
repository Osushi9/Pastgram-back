from flask_login import current_user

from api.database import db
from api.models.follows import Follows
from api.models.users import Users

from .schema import Schema


def get_followee_amount(user):
    return (
        Follows.query.filter_by(followee_id=user.id).filter_by(confirmed=True).count()
    )


def get_follower_amount(user):
    return (
        Follows.query.filter_by(follower_id=user.id).filter_by(confirmed=True).count()
    )


userSchema = Schema(
    followee_amount=get_followee_amount, follower_amount=get_follower_amount
)


def get_user(user_id, fields=["id", "name", "icon_path"]):
    user = Users.query.filter_by(id=user_id).first()

    return userSchema.marshall(user, fields)


def update_user(
    user_id,
    name=None,
    password=None,
    profile_name=None,
    icon_path=None,
    fields=["id", "name", "icon_path"],
):
    user = Users.query.filter_by(id=user_id).first()

    if name is not None:
        user.name = name
    if password is not None:
        # user.password = password
        pass
    if profile_name is not None:
        user.profile_name = profile_name
    if icon_path is not None:
        user.icon_path = icon_path

    db.session.commit()

    return userSchema.marshall(user, fields)


def get_current_user_id():
    return current_user.id


def get_current_user(fields=["id", "name", "icon_path"]):
    return userSchema.marshall(current_user, fields)


def get_followee_ids(user_id):
    follows = Follows.query.filter_by(followee_id=user_id).all()
    follower_ids = [follow.follower_id for follow in follows]
    return follower_ids


def get_followees(user_id, fields=["name", "icon_path"]):
    # return [userSchema.marshall(user2, fields), userSchema.marshall(user3, fields)]
    return userSchema.marshall_many(
        Follows.query.filter_by(followee_id=user_id).all(), fields
    )


def get_followers(user_id, fields=["name", "icon_path"]):
    return userSchema.marshall_many(
        Follows.query.filter_by(follower_id=user_id).all(), fields
    )


def search_users(query, fields=["id", "name", "icon_path"]):
    return userSchema.marshall_many(
        Users.query.filter(Users.name.like(f"{query}%")).all(),
        fields,
    )
