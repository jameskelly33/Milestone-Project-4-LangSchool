from django.contrib import admin
from .models import Booking
from courses.models import Course
# Register your models here.




class BookingAdmin(admin.ModelAdmin):

    readonly_fields =(
        'booking_number', 'date_booked',"total_course_cost"
    )

    fields =(
        'booking_number',
       
        'full_name',
        'email',
        'phone_number',
        'country',
        'nationality',
        'first_language',
        'age',
        'date_booked',
        'course_length',
        'course_start_date',
        'course_level',
        'quantity',
        'course_cost_per_week',
        'total_course_cost',
        'course'
    )

    list_display=(
        'booking_number', 'date_booked', 'total_course_cost',
    )


admin.site.register(Booking, BookingAdmin)