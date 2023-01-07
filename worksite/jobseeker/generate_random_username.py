import random
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'worksite.settings')
django.setup()

from services.db_functions import select_all_fields_from_model
from models import JobseekerUsernames


def generate_random_username(user_email: str):
    """
    A function that generates a random username based on the first part of the
    user's email address and a pseudo-random number in the range 1 - 10 000.
    Checks whether such a name has already been
    created in the usernames database, and if someone already has such a
    name, generates again until a unique name is generated
    :param user_email:
    :return:
    """
    random_number = str(random.randint(1, 10_000))
    user_email_without_domain = user_email.split('@')[0]
    username = user_email_without_domain + random_number
    return username


def save_username_in_db(username: str):
    all_usernames = select_all_fields_from_model(JobseekerUsernames)
    if username not in all_usernames:
        new_username = JobseekerUsernames(username=username)
        new_username.save()


def main():
    username = generate_random_username('dimaproc49@gmail.com')
    save_username_in_db(username)


main()
