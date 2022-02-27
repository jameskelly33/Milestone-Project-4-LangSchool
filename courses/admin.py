from django.contrib import admin
from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'category_description',
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'course_description',
        'course_category',
        'course_hours',
        'maximum_class_size',
        'minimum_age',
        'course_timetable',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
