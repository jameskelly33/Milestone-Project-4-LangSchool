from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from courses.models import Course
from django.core.validators import MinValueValidator, ValidationError
from .forms import BookingForm
from .models import Booking
from profiles.models import UserProfile
from django.conf import settings
import stripe 
import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string



def booking_form(request, course):

    
    course = Course.objects.get(course_id=course)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    booking_form = BookingForm
    
    if request.method == 'POST':
        
        form_data={
                
                'course_length':request.POST['course_length'],
                'course_level':request.POST['course_level'],
                'course_start_date':request.POST['course_start_date'],
                'age': request.POST['age'],
                'course_cost_per_week':course.cost_per_week,
                'total_course_cost':int(course.cost_per_week) * int(request.POST['course_length']),
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'phone_number': request.POST['phone_number'],
                'country': request.POST['country'],
                'nationality': request.POST['nationality'],
                'first_language': request.POST['first_language'],
                'course':course.course_id,
                'course_friendly_name':course.friendly_name,
                'course_timetable':course.course_timetable,
        }
        # Age Verification
        if int(form_data.get('age')) < course.minimum_age:
            messages.error(request, f'Sorry, the minimum age for this course is {course.minimum_age}.Please find another course')
            return redirect(reverse('courses'))
        elif course.maximum_age:
            if int(form_data.get('age')) > course.maximum_age:
                messages.error(request, f'Sorry, the maximum age for this course is {course.maximum_age}.Please find another course')
                return redirect(reverse('courses'))
        # Level Verification for B1+ classes
        if form_data.get('course_level') in ['A1','A2','A2H']:
            print('test')
            if course.course_levels != "all":
                messages.error(request, f'Sorry, the minimum level for this course  {course.course_levels}.Please find another course')
                return redirect(reverse('courses'))
        # Level Verification for C1 only classes 
        elif form_data.get('course_level') != 'C1':
            if course.course_levels == "C1":
                print('c1')
                messages.error(request, f'Sorry, the minimum level for this course  {course.course_levels}.Please find another course')
                return redirect(reverse('courses'))        
                
        else:
            booking_form = BookingForm(form_data)
            if booking_form.is_valid():
                booking = booking_form.save()
                return redirect(reverse('checkout', args=[booking]))
            else:
                messages.error(request, f'There was an error with your form. \
                    Please double check your information.')
                   

            
            context = {
               
                'booking_form': booking_form,
                'course':course,
                'form_data':form_data,
                'stripe_public_key':stripe_public_key,
            }

            return render(request, 'booking_form/booking_form.html', context)
            

    else:
        
        context={
            'booking_form': booking_form,
            'course':course,
            
        }
        return render(request, 'booking_form/booking_form.html',context)

def checkout(request, booking):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    booking = Booking.objects.get(booking_number = booking)
    course = Course.objects.get(course_id = booking.course)
    course_start_date = booking.course_start_date
    end_date = course_start_date + datetime.timedelta(weeks=int(booking.course_length))
    
    if request.method == 'POST':
        
        # Send Confirmation email
        cust_email = booking.email
        subject = render_to_string(
        'booking_form/confirmation_emails/email_subject.txt',
        {'booking': booking})
        body = render_to_string(
        'booking_form/confirmation_emails/email_body.txt',
        {'booking': booking,})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )        

        
        context={
            'booking':booking,
            'stripe_public_key':stripe_public_key,
            'course':course,
        }
        
        return redirect(reverse('checkout_success', args=[booking]))
    else:
        total = booking.total_course_cost
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        )
        
    if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')
    context={
        'booking':booking,
        'stripe_public_key':stripe_public_key,
        'total':total,   
        'client_secret':intent.client_secret,         
        'course':course,
        'end_date':end_date
    }        
    return render(request, 'booking_form/checkout.html',context )

def checkout_success(request, booking):
    

    booking = Booking.objects.get(booking_number = booking)
    course = Course.objects.get(course_id = booking.course)
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user = request.user)
        booking.user_profile = profile
        booking.save()      
    messages.success(request, 'Booking successfully processed!' )
    

    

    template = 'booking_form/checkout_success.html'
    context = {
        'booking': booking,
        'course':course
    }

    return render(request, template, context)