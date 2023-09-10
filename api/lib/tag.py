from api.models.tags import Tags

def get_current_tag():
    return Tags.query.first()

def get_current_tag_name():
    return get_current_tag().name

def get_current_limit():
    return get_current_tag().limit
