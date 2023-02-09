import os


def validate_file_extension(file):
    file_extension = os.path.splitext(file)[-1]
    allowed_extensions = ['.pdf', '.docx', '.doc']
    if file_extension in allowed_extensions:
        return True
    return False


def validate_image_extension(image):
    image_extension = os.path.splitext(image)[-1]
    allowed_extensions = ['.jpg', 'jpeg', 'pdf']
    if image_extension in allowed_extensions:
        return True
    return False


def validate_file_size(file: open):
    file_size = os.path.getsize(file)
    if file_size <= 1024 + (1024 / 2):
        return True
    return False
