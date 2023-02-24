from django.urls import path

from .views import *

urlpatterns = [
    path('', jobseeker_login_view, name='login'),
    path('/register', jobseeker_register_view, name='register'),
    path('/logout', jobseeker_logout_view, name='logout'),
    path('/success_register', success_register_view, name='success'),
    path('/code-verification', verificate_number_view, name='code_verification'),
]
