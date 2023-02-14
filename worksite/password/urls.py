from django.urls import path

from .views import *

urlpatterns = [
    path('form/<str:login>/', remind_password_view, name='remind_password'),
    path('/change/<str:token>/', change_password_page, name='change_password'),
]