from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from courses.models import Course
from django.core.validators import MinValueValidator, ValidationError
from .forms import BookingForm
from .models import Booking
from django.conf import settings
import stripe 


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
                'course':course.course_id
        }

        
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save()
        else:
            print(booking_form.errors)
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

        
        context = {
            'booking':booking,
            'booking_form': booking_form,
            'course':course,
            'form_data':form_data,
            'stripe_public_key':stripe_public_key,
        }

        return redirect(reverse('checkout', args=[booking]))

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
    
    if request.method == 'POST':
        
       
        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')
        context={
            'booking':booking,
            'stripe_public_key':stripe_public_key,
            
            
             
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
    }        
    return render(request, 'booking_form/checkout.html',context )

def checkout_success(request, booking):
    

    booking = Booking.objects.get(booking_number = booking)

    
    messages.success(request, f'Order successfully processed! \
        Your order number is {booking.booking_number}. A confirmation \
        email will be sent to {booking.email} .')

    

    template = 'booking_form/checkout_success.html'
    context = {
        'booking': booking,
    }

    return render(request, template, context)