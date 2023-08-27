def get_post(post_id, fields=["id", "image_path", "create_at"]):
    pass

def get_posts(user_id, fields=["id", "image_path", "create_at"]):
    pass

def create_post(user_id, image_path, create_at):
    pass

def get_thumnail(user_id, fields=["id", "latest_create", "latest_path", "amount"]):
    return {
        "id": 1,
        "latest_create": "2021/11/09 00:00:00",
        "latest_path": "/images/gheowi-hfeowv-hgweosd",
        "amount": 2
    }
