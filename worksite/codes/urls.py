from django.urls import path

from .views import *

urlpatterns = [
    path('', verificate_number_view, name='code_verification')
]