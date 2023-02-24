def custom_error_service(errors: dict):
    first_error_form_list = list(errors.values())[0]
    string_error_message = ''.join(first_error_form_list[0])
    return string_error_message


def get_form_errors_service(form: callable):
    form_errors = form.errors.as_data()
    custom_error = custom_error_service(form_errors)
    return custom_error