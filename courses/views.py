from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Category, Course
from .forms import CourseForm


def courses(request):

    categories = Category.objects.all()
    course_list = None
    query = None

    if request.GET:
        course_list = Course.objects.all()
        if 'category' in request.GET:
            current_category = request.GET['category'].split()
            course_list = course_list.filter(
                course_category__name__in=current_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term")
                return redirect(reverse('courses'))
            queries = Q(friendly_name__icontains=query) | Q(
                course_description__icontains=query)
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
            course_list = course_list.filter(
                course_category__name__in=current_category)
            categories = categories.filter(name__in=current_category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term")
                return redirect(reverse('courses'))
            queries = Q(friendly_name__icontains=query) | Q(
                course_description__icontains=query)
            course_list = course_list.filter(queries)
    context = {
        'categories': categories,
        'search_term': query,
        'course_list': course_list,
        'current_category': categories,
    }

    return render(request, 'courses/course_library.html', context)


@login_required
def add_course(request):

    """ Add a course to the course library """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added new course!')
            return redirect(reverse('courses'))
        else:
            messages.error(request, 'Failed to add course. Please ensure the\
                 form is valid.')
    else:
        form = CourseForm()
    template = 'courses/add_course.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_course(request, course_id):
    """ Edit course in course library """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))
    course = get_object_or_404(Course, course_id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated course.')
            return redirect(reverse('courses'))
        else:
            messages.error(request, 'Failed to update course. Please ensure\
                 the form is valid.')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.friendly_name}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


@login_required
def delete_course(request, course_id):
    """ Delete a course from the course library """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin users can do that.')
        return redirect(reverse('home'))
    course = get_object_or_404(Course, course_id=course_id)
    course.delete()
    messages.success(request, 'Course deleted.')
    return redirect(reverse('courses'))
