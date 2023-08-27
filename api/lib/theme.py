from api.models.tags import Tags


def get_current_tag():
    return Tags.query.first().name


def get_current_limit():
    return Tags.query.first().limit
