
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('<course>', views.booking_form, name='booking_form'),
    path('checkout/<booking>', views.checkout, name='checkout'),
    path('checkout_success/<booking>', views.checkout_success, name='checkout_success')

]
