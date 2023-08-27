from .mock import *
from .schema import Schema


def get_followee_amount(draft):
    return 2


def get_follower_amount(draft):
    return 3


userSchema = Schema(
    followee_amount=get_followee_amount, follower_amount=get_follower_amount
)


def get_user(user_id, fields=["id", "name", "icon_path"]):
    user = users[user_id]

    return userSchema.marshall(user, fields)


def update_user(
    user_id,
    name=None,
    password=None,
    profile_name=None,
    icon_path=None,
    fields=["id", "name", "icon_path"],
):
    user = users[user_id]

    if name is not None:
        user.name = name
    if password is not None:
        # user.password = password
        pass
    if profile_name is not None:
        user.profile_name = profile_name
    if icon_path is not None:
        user.icon_path = icon_path

    return userSchema.marshall(user, fields)


def get_current_user_id():
    return 1


def get_current_user(fields=["id", "name", "icon_path"]):
    return userSchema.marshall(draft, fields)


def get_followee_ids(user_id):
    return [2, 3]


def get_followees(user_id, fields=["name", "icon_path"]):
    return [userSchema.marshall(user2, fields), userSchema.marshall(user3, fields)]


def get_followers(user_id, fields=["name", "icon_path"]):
    return [userSchema.marshall(user2, fields)]


def search_users(query, fields=["id", "name", "icon_path"]):
    return [
        userSchema.marshall(user2, fields)
    ]
