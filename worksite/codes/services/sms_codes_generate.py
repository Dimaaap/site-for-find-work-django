from random import choice


def generate_code():
    number_tuple = tuple(range(10))
    code_items = [choice(number_tuple) for i in range(5)]
    code_string = ''.join(str(i) for i in code_items)
    return code_string