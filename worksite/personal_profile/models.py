import os

from django.db import models
from django.core.validators import FileExtensionValidator
from django_select2 import forms

from jobseeker.models import JobseekerRegisterInfo


def validate_file_extension(filename):
    pass


class JobseekerProfileInfo(models.Model):
    jobseeker = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d',
                              blank=True,
                              null=True,
                              validators=[FileExtensionValidator(allowed_extensions=
                                                                 ['jpg', 'png', 'jpeg'])])
    expected_job = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=150, blank=True)
    linkedin = models.URLField(blank=True)
    git_hub = models.URLField(blank=True)
    cv_file = models.FileField(upload_to='cvs/%Y/%m/%d', validators=[validate_file_extension])
    active_search = models.BooleanField(default=True)

    def __str__(self):
        return self.expected_job

    def base_cv(self):
        return os.path.basename(self.cv_file.name)


class Position(models.Model):
    title = models.CharField(max_length=190)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class WorkCriteria(models.Model):
    jobseeker = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True)
    salary_expectations = models.PositiveIntegerField(default=0)
    hourly_rate = models.PositiveIntegerField(blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)
    moving_to_another_city = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    work_experience = models.TextField(blank=True)
    expectations = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    questions_to_employers = models.TextField(blank=True)

    def __str__(self):
        return f'{self.jobseeker} Profile'

