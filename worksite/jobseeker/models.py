from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from werkzeug.security import generate_password_hash


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
