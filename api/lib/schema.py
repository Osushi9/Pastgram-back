class Schema:
    def __init__(self, **marshall_funcs):
        self.marshall_funcs = marshall_funcs

    def marshall(self, obj, fields):
        result = {}

        for field in self.marshall_funcs.keys():
            if field in fields:
                result[field] = self.marshall_funcs[field](obj)
                fields.remove(field)

        for field in fields:
            result[field] = getattr(obj, field)

        return result

    def marshall_dict(self, dict, fields):
        result = {}

        for field in self.marshall_funcs.keys():
            if field in fields:
                result[field] = self.marshall_funcs[field](dict)
                fields.remove(field)

        for field in fields:
            result[field] = dict[field]

        return result
