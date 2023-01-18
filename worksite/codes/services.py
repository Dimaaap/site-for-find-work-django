from random import choice


def generate_code_string():
    number_tuple = tuple(range(10))
    num_items = []
    for i in range(5):
        random_number = choice(number_tuple)
        num_items.append(random_number)
    code_string = ''.join(str(item) for item in num_items)
    return code_string

