import random

from django.db import models

from .services import generate_code_string
from jobseeker.models import JobseekerRegisterInfo


class Code(models.Model):

    number = models.CharField(max_length=5, blank=True)
    jobseeker = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    def save(self, *args, **kwargs):
        code_string = generate_code_string()
        self.number = code_string
        super().save(*args, **kwargs)
