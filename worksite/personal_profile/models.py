import os

from django.db import models
from PIL import Image

from jobseeker.models import JobseekerRegisterInfo


def validate_file_extension(filename):
    pass


class JobseekerProfileInfo(models.Model):
    jobseeker = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d',
                              blank=True,
                              null=True,
                              # default='static/personal_profile/images/default_avatar.png')
                              )
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

    def save(self, *args, **kwargs):
        super(JobseekerProfileInfo).save(*args, **kwargs)
        image = Image.open(self.photo)
        if image.width > 400 or image.height > 300:
            output_size = (400, 300)
            image.thumbnail(output_size)
            image.save(self.photo)
