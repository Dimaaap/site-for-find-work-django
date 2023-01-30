def custom_error_service(errors: dict):
    """
    The function that receives error messages im form fields takes only
    the first value in this dictionary and returns it as a string
    """
    first_error_form_list = list(errors.values())[0]
    string_error_message = ''.join(first_error_form_list[0])
    return string_error_message

