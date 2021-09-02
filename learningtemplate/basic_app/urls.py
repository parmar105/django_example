from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('others/', views.others, name="others"),
]