from random import randint

from django.db import models
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


class JobseekerProfileInfo(models.Model):

    jobseeker = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d')
    header = models.TextField(blank=True)
    telegram = models.URLField(blank=True, max_length=200)
    linkedin = models.URLField(blank=True)
    git_hub = models.URLField(blank=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d')

    def __str__(self):
        return self.jobseeker
