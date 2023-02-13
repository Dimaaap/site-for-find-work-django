import os

from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile


def validate_file_extension(file):
    file_extension = os.path.splitext(file)[-1]
    allowed_extensions = ['.pdf', '.docx', '.doc']
    if file_extension in allowed_extensions or not file_extension:
        return True
    return False


def validate_image_extension(image: InMemoryUploadedFile):
    allowed_formats = ('png', 'jpg', 'jpeg')
    image_full_type = image.content_type
    image_type = str(image_full_type).split('/')[-1]
    if image_type in allowed_formats:
        return True
    return False


def validate_file_size(file: InMemoryUploadedFile):
    size = file.size
    if size <= settings.KILOBYTES_IN_MB + (settings.KILOBYTES_IN_MB / 2):
        return True
    return False

