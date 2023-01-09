from ..filters import EqualFilter


def select_all_fields_from_model(model: callable):
    queryset = model.objects.all()
    return queryset


def select_field_value_from_model(model: callable, field_name: str, field_value: str):
    equal_filter = EqualFilter()
    return model.objects.filter(**equal_filter(field_name, field_value))
