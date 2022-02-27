
from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses, name='courses'),
    path('course_library/', views.course_library, name='course_library'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<course_id>', views.edit_course, name='edit_course'),
    path('delete/<course_id>', views.delete_course, name='delete_course'),

]
