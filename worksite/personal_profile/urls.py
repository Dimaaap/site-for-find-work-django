from django.urls import path

from .views import *


urlpatterns = [
    path('profile/<str:login>/', main_profile_page_view, name='jobseeker_profile'),
    path('delete/file/<int:pk>/', delete_file_view, name='delete_file'),
    path('profile/image/<str:login>/', set_user_image_view, name='image-form'),
    path('profile/work/<str:login>/', work_criteria_view, name='work-criteria'),
]