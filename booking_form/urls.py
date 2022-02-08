
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<course>', views.booking_form, name='booking_form'),
    path('checkout/<course>', views.checkout, name='checkout'),

]
