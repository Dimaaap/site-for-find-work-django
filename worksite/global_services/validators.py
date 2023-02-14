def is_valid_password_symbols(password: str):
    if all([symbol.isdigit() for symbol in password]) or all([symbol.isalpha() for symbol in password]):
        return False
    return True