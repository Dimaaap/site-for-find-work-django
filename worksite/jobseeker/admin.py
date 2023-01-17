from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import JobseekerRegisterInfo, Code


@admin.register(JobseekerRegisterInfo)
class JobseekerRegisterInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'phone_number')

    class CodeAdmin(admin.ModelAdmin):
        list_display = ('code', 'user')
        search_fields = list_display_links = list_display
        actions_on_top = True

    # admin.site.register(JobseekerRegisterInfo)
    admin.site.register(Code, CodeAdmin)
