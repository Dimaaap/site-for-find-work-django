from filters import EqualFilter


def filter_fields_from_db(model: callable, key: str, value: str):
    equal_filter = EqualFilter()
    return model.objects.filter(**equal_filter(key, value))


def get_fields_from_db(model: callable, key: str, value: str):
    equal_filter = EqualFilter()
    return model.objects.get(**equal_filter(key, value))


def select_all_fields_from_db(model: callable):
    return model.objects.all()