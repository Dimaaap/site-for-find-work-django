import jwt
from time import time

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class JobseekerRegisterInfo(AbstractUser):
    username = first_name = last_name = None
    id = models.BigAutoField(primary_key=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=120)
    password = models.CharField(max_length=150)
    login = models.CharField(max_length=100, default=None)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'full_name', 'password']

    def __str__(self):
        return self.full_name

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'remind_password': self.pk, 'exp': time() + expires_in},
            settings.SECRET_KEY, algorithm='HS256'
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])['remind_password']
        except:
            return
        return JobseekerRegisterInfo.objects.get(pk=id)
