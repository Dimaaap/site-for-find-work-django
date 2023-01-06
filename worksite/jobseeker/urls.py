from django.urls import path

from .views import *

urlpatterns = [
    path('', jobseeker_login_view, name='login'),
    path('/register', jobseeker_register_view, name='register')
]
