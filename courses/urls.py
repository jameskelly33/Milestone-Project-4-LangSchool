from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses, name='courses'),
    path('course_library/', views.course_library, name='course_library')
]
