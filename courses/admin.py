from django.contrib import admin
from .models import Category, Course

# Register your models here.

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
        'minumum_age',
        'course_timetable',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)