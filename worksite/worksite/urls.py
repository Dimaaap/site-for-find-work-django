from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('jobseeker', include('jobseeker.urls')),
    path('profile', include('personal_profile.urls')),
    path('password', include('password.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('select2/', include('django_select2.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('captcha/', include('captcha.urls'))
]

