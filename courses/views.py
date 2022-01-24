from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Category, Course


def courses(request):

    categories = Category.objects.all()
    course_list = None
    query = None

    if request.GET:
        course_list = Course.objects.all()
        if 'category' in request.GET:
            current_category = request.GET['category'].split()
            course_list = course_list.filter(course_category__name__in= current_category)
            

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term")
                return redirect(reverse('courses'))
            
            queries = Q(friendly_name__icontains=query) | Q(course_description__icontains=query)
            course_list = course_list.filter(queries)
            
            context = {
                'search_term': query,
                'course_list': course_list,
            }
            return render(request, 'courses/course_library.html', context)
            
    context = {
        'categories': categories,
        'search_term': query,
        'course_list': course_list,
        'current_category': categories,
    }
    

    return render(request, 'courses/courses.html', context)

def course_library(request):
    categories = Category.objects.all()
    course_list = None
    query = None
    
    if request.GET:
        course_list = Course.objects.all()
        if 'category' in request.GET:
            current_category = request.GET['category'].split()
            course_list = course_list.filter(course_category__name__in= current_category)
            categories = categories.filter(name__in=current_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term")
                return redirect(reverse('courses'))
            
            queries = Q(friendly_name__icontains=query) | Q(course_description__icontains=query)
            course_list = course_list.filter(queries)
            
    context = {
        'categories': categories,
        'search_term': query,
        'course_list': course_list,
        'current_category': categories,
    }
    

    return render(request, 'courses/course_library.html', context)
