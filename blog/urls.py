from django.urls import path
from . import views

urlspatterns = [
    path('', views.post_list, name = 'post_list'),
]
