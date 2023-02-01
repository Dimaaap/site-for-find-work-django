def check_cleaned_data(fields: list | tuple | set, cleaned_data: dict) -> dict:
    """
    A function that accepts two arguments: a list of keys and a dictionary.
    Searches the dictionary for keys whose values have the boolean value
    False and deletes them. Returns a cleared dictionary,
    that is, a dictionary without keys whose values are False-values
    """
    for field in fields:
        if not cleaned_data[field]:
            cleaned_data.pop(field)
    return cleaned_data

