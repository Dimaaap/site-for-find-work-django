import os

from django.db import models
from django.core.validators import FileExtensionValidator
from PIL import Image

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
