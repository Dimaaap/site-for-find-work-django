from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('jobseeker', include('jobseeker.urls')),
]
urlpatterns += [
    path('captcha/', include('captcha.urls'))
]
