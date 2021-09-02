from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.user_info, name = 'userInfo'),
    path('userform/', views.user_form, name='userForm'),
]