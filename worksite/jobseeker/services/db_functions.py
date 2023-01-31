from random import randint

from filters import EqualFilter


def select_all_fields_from_model(model: callable):
    queryset = model.objects.all()
    return queryset


def select_field_value_from_model(model: callable, field_name: str, field_value: str):
    equal_filter = EqualFilter()
    return model.objects.filter(**equal_filter(field_name, field_value))


def get_write_from_model(model: callable, field_name: str, field_value: str):
    equal_filter = EqualFilter()
    return model.objects.get(**equal_filter(field_name, field_value))


def create_user_login(email: str):
    email_name = email.split('@')[0]
    return str(email_name) + str(randint(1, 100))


