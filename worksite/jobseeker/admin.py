from django.contrib import admin
from .models import JobseekerRegisterInfo


class JobseekerRegisterInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone_number')


admin.site.register(JobseekerRegisterInfo)
