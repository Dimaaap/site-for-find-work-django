from django.urls import path

from .views import *

urlpatterns = [
    path('form/<str:login>/', remind_password_view, name='remind_password')
]