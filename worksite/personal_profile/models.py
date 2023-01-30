from django.db import models

from jobseeker.models import JobseekerRegisterInfo


class JobseekerProfileInfo(models.Model):
    jobseeker = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='avatars/%Y/%m/%d',
                              default='static/personal_profile/images/default_avatar.png')
    expected_job = models.CharField(max_length=400, blank=True)
    telegram = models.CharField(max_length=150, blank=True)
    linkedin = models.URLField(blank=True)
    git_hub = models.URLField(blank=True)
    cv = models.FileField(upload_to='cv/%Y/%m/%d')
    active_search = models.BooleanField(default=True)

    def __str__(self):
        return self.jobseeker
