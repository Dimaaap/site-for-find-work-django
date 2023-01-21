# from django.db import models
#
# from .services.sms_codes import generate_code
# from jobseeker.models import JobseekerRegisterInfo
#
#
# class Code(models.Model):
#     """
#     Модель, у якій будуть зберігатись коди, які будуть надсилатись користувачу для підтвердження
#     акаунту. Містить поля number, яке зберігає власне надісланий код і посилання на користувача,
#     якому був надісланий цей код
#     """
#     number = models.CharField(max_length=5, blank=True)
#     jobseeker = models.OneToOneField(JobseekerRegisterInfo, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.number
#
#     def save(self, *args, **kwargs):
#         code_string = generate_code()
#         self.number = code_string
#         super().save(*args, **kwargs)
