from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length = 254)
    friendly_name = models.CharField(max_length = 254, null = True, blank= True)
    category_description = models.CharField(max_length = 500)


    def __str__(self):
        return self.name


    def get_friendly_name(self):
        return self.friendly_name

class Course(models.Model):
    
    class Meta:
        verbose_name_plural = 'Courses'
    
    course_id = models.CharField(max_length = 8)
    name = models.CharField(max_length = 254)
    friendly_name = models.CharField(max_length = 254, null = True, blank= True)
    course_description = models.CharField(max_length = 500)
    course_category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    course_hours = models.DecimalField(max_digits=3, decimal_places=0)
    maximum_class_size = models.DecimalField(max_digits=2, decimal_places=0)
    minumum_age = models.DecimalField(max_digits=2, decimal_places=0)
    maximum_age = models.DecimalField(max_digits =2, decimal_places=0, blank=True, null =True)
    cost_per_week = models.DecimalField(max_digits = 10, decimal_places = 2, default=0)
    course_levels = models.CharField(max_length=50, null=False, blank=True)
    course_timetable = models.CharField(max_length = 30)
    

    


    def __str__(self):
        return self.name


    def get_friendly_name(self):
        return self.friendly_name        


