from .check_cleaned_data import check_cleaned_data
from .db_utils import filter_fields_from_db, get_fields_from_db


def update_form_data(form: callable, model: callable, filter_args: tuple):
    """
    The function that implements the system of updating data in the
    model model. Receives the form form, cleans its built-in
    dictionary cleaned_data, which stores the data entered by the user,
    leaving only those that the user passed not empty,
    and updates the entry in the model model based on this cleaned dictionary
    filter_args - is a tuple with 2 elements where first element is a key for function
    filter_fields_from_db, and second element is a value for this function
    """
    fields = dict(form.cleaned_data).keys()
    list_fields = list(fields)
    check_cleaned_data(list_fields, form.cleaned_data)
    if len(filter_args) != 2:
        raise ValueError('filter_args arguments must have strictly 2 elements')
    else:
        filter_data = filter_fields_from_db(model, *filter_args)
        filter_data.update(**form.cleaned_data)


def update_cv_field_in_model(model: callable, tuple_args: tuple, cv_file: open):
    query = get_fields_from_db(model, *tuple_args)
    if cv_file:
        try:
            query.cv_file = cv_file
            query.save()
        except Exception:
            return False
    return True


