from django.shortcuts import render
from django.contrib import messages
from courses.models import Course
from django.core.validators import MinValueValidator, ValidationError
from .forms import BookingForm
from .models import Booking



def booking_form(request, course):

    course = Course.objects.get(course_id=course)
    
   

    
    booking_form = BookingForm()
    context = {
        'booking_form': booking_form,
        
        'course':course,
        'stripe_public_key':'pk_test_51KQqgYCD6IZd0u5V3Xy6Hqc52BlEqShF0iCfY5uPzQzYhcE0JySNIKqK1MFxytupOL4t4mvrkMiaILDsE9J6uIJO00MLHHnhA5',
        'client_secret':'test_client_secret'

        
    }

    return render(request, 'booking_form/booking_form.html',context)

def checkout(request, course):
    if request.method == 'POST':
        
        course = Course.objects.get(course_id = course)
       
        

        form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone_number': request.POST['phone_number'],
                'country': request.POST['country'],
                'nationality': request.POST['nationality'],
                'first_language': request.POST['first_language'],
                'age': request.POST['age'],
                'course_length':request.POST['course_length'],
                'course_level':request.POST['course_level'],
                'course_start_date':request.POST['course_start_date'],
                'quantity':request.POST['quantity'],
                'course':course.course_id,
                'course_cost_per_week':int(course.cost_per_week),
                'total_course_cost':int(course.cost_per_week) * int(request.POST['course_length']) *int(request.POST['quantity'])
                
                }
        
        booking_form = BookingForm(form_data)
        
        if int(course.minumum_age) > int(request.POST['age']):
            messages.error(request, 'The age you entered is too young for this particular course')

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.save()
            print(form_data.get('course_cost_per_week'))
        else:
            messages.error(request, 'There was an error with your form. \
                    Please double check your information.')

        context={
            'booking_form':booking_form,
            'form_data': form_data,
            'course':course,
            
        }
    return render(request,'booking_form/booking_form.html', context )