from django.db import models

# Create your models here.
import uuid

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, ValidationError
import datetime
from django_countries.fields import CountryField


from courses.models import Course
from profiles.models import UserProfile


class Booking(models.Model):
    # Add level options for course bookings
    a1 = 'A1'
    a2 = 'A2'
    a2h = 'A2H'
    b1 = 'B1'
    b2 = 'B2'
    b2h = 'B2H'
    c1 ='C1'
    level_choices= [
        (a1,'A1 - Beginner'),
        (a2, 'A2- Elementary'),
        (a2h, 'A2H- Pre-Intermediate'),
        (b1, 'B1- Intermediate'),
        (b2h, 'B2H- Upper-Intermediate'),
        (c1, 'C1- Advanced'),
        
    ]
    # Validator to prevent users from booking a course in the past
    def no_past_dates(value):
        today = datetime.datetime.now().date()
        if value < today:
            raise ValidationError('Booking date cannot be in the past.')
   
    booking_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='bookings')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    nationality = models.CharField(max_length=40, null=False, blank=False)
    first_language = models.CharField(max_length=40, null=False, blank=False)
    age = models.DecimalField(max_digits=3, decimal_places=0, null=False, blank=False)
    date_booked = models.DateField(auto_now_add=True)
    course_length = models.DecimalField(max_digits=2, decimal_places=0, blank=False, default=1, validators = [MinValueValidator(1,message = "Minimum Course Length is 1 week")])
    course_start_date = models.DateField(blank=False, null=True, validators =[no_past_dates])
    course_level = models.CharField(max_length=15,choices = level_choices, )
    course_cost_per_week = models.DecimalField(max_digits=6, decimal_places=2, null=False, default =0)
    total_course_cost = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    course = models.CharField(max_length=20,null=True)
    course_friendly_name =  models.CharField(max_length = 254, null = True, blank= True)
    course_timetable = models.CharField(max_length = 30, null= True, blank = True)
  
    


    def _generate_booking_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

   
        

    def save(self, *args, **kwargs):
        """
        Override the original save method to ensure there is
        a booking number
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number        
    



    