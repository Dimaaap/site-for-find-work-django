from django.urls import path

from .views import *

urlpatterns = [
    path('', remind_password_view, name='remind_password')
]