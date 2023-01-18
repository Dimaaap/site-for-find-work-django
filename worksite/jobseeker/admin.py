from django.contrib import admin
from .models import JobseekerRegisterInfo


@admin.register(JobseekerRegisterInfo)
class JobseekerRegisterInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone_number')

    class CodeAdmin(admin.ModelAdmin):
        list_display = ('code', 'user')
        search_fields = list_display_links = list_display
        actions_on_top = True
