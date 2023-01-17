import random

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.hashers import make_password


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
    password = models.CharField(max_length=150)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'full_name', 'password']

    def __str__(self):
        return self.full_name

    # def save(self, *args, **kwargs):
    #     try:
    #         self.hashed_password = self.password
    #     except Exception as exp:
    #         print(exp)
    #         raise ValueError('Помилка додавання запису в БД')
    #     super(JobseekerRegisterInfo, self).save(*args, **kwargs)


class Code(models.Model):
    code = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)

    # qwsc123@gmail.com

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        code_string = generate_random_code()
        self.code = code_string
        super().save(*args, **kwargs)
