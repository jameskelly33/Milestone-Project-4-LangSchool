from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.level_test, name='level_test'),
    path('<int:question_counter> <int:total>', views.check_answer, name='check_answer'),
 

    
]
