from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('jobseeker', include('jobseeker.urls')),
    path('profile', include('personal_profile.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('captcha/', include('captcha.urls'))
]

