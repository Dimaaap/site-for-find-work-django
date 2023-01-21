# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from jobseeker.models import JobseekerRegisterInfo
# from .models import Code
#
#
# @receiver(post_save, sender=JobseekerRegisterInfo)
# def post_save_generate_code(sender, instance, created, *args, **kwargs):
#     """
#     При створенні нового запису в таблиці JobseekerRegisterInfo створювати новий запис у таблиці
#     Code
#     """
#     if created:
#         Code.objects.create(jobseeker=instance)

