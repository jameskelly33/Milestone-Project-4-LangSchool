from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from booking_form.models import Booking
from courses.models import Course
import datetime
from blog.models import Post

@login_required
def profiles(request):

    profile = get_object_or_404(UserProfile, user = request.user)

    if request.method == "POST":
        form= UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    
    bookings = profile.bookings.all()
    posts = Post.objects.all()
    liked_posts={}

    for post in posts:
        if request.user in post.likes.all():
            liked_posts.update({post.pk:post.title})
           
    print(liked_posts)        
    
    
    
    context ={
        'form':form,
        'bookings':bookings,
        'profile':profile,
        'liked_posts':liked_posts,
        
       
    }

    return render(request, 'profiles/profiles.html', context)