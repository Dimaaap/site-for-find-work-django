from django.urls import path, include

from .views import *

urlpatterns = [
    path('', main_page_view, name='index_page')
]
