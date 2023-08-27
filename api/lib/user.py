def get_user(user_id, fields=["id", "name", "icon_path"]):
    pass

def update_user(
    user_id,
    name=None,
    password=None,
    profile_name=None,
    icon_path=None):
    pass

def get_current_user(fields=["id", "name", "icon_path"]):
    return {
        "id": 1,
        "name": "hanako"
    }

def get_followee_ids(user_id):
    return [1, 2, 3]

def get_followees(user_id, fields=["name", "icon_path"]):
    pass

def get_followers(user_id, fields=["name", "icon_path"]):
    pass

def search_users(query, fields=["id", "name", "icon_path"]):
    pass
