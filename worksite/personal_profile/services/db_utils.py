from filters import EqualFilter


def filter_fields_from_db(model: callable, key: str, value: str):
    equal_filter = EqualFilter()
    return model.objects.filter(**equal_filter(key, value))


def get_fields_from_db(model: callable, key: str, value: str | int):
    equal_filter = EqualFilter()
    query = []
    try:
        query = model.objects.get(**equal_filter(key, value))
    except Exception:
        query = []
    finally:
        return query


def select_all_fields_from_db(model: callable):
    return model.objects.all()


def update_data_in_model(filter_key: str, filter_value: str, update_data: dict, **kwargs):
    pass
