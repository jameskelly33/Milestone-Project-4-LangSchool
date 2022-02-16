from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm
from booking_form.models import Booking
from courses.models import Course
import datetime

# Create your views here.
def profiles(request):

    profile = get_object_or_404(UserProfile, user = request.user)

    if request.method == "POST":
        form= UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    
    bookings = profile.bookings.all()
    
    
    
    context ={
        'form':form,
        'bookings':bookings,
        'profile':profile,
       
    }

    return render(request, 'profiles/profiles.html', context)