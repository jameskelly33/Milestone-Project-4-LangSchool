from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.level_test, name='level_test'),
    
]
