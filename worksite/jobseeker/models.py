import random

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from werkzeug.security import generate_password_hash


def generate_random_code():
    number_list = tuple(range(10))
    code_items = []
    for i in range(5):
        random_number = random.choice(number_list)
        code_items.append(random_number)
    code_string = ''.join(str(item) for item in code_items)
    return code_string


class JobseekerRegisterInfo(AbstractUser):
    username = first_name = last_name = None
    id = models.BigAutoField(primary_key=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=120)
    hashed_password = models.CharField(max_length=200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'full_name', 'hashed_password']

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        try:
            self.hashed_password = generate_password_hash(self.password)
        except Exception as exp:
            print(exp)
            raise ValueError('Помилка додавання запису в БД')
        super(JobseekerRegisterInfo, self).save(*args, **kwargs)


class Code(models.Model):
    code = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        code_string = generate_random_code()
        self.code = code_string
        super().save(*args, **kwargs)
