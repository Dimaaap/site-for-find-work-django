from django.urls import path

from .views import *


urlpatterns = [
    path('profile/<str:login>>', main_profile_page_view, name='jobseeker_profile')
]