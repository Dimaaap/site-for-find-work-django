from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class JobseekerUsernames(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.username


class JobseekerRegisterInfo(AbstractUser):
    id = models.IntegerField(primary_key=True)
    phone_number = PhoneNumberField()
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=120)
    hashed_password = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name
