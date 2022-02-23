from django.db import models
from django.core.validators import MinValueValidator, ValidationError

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
    # Add options for course levels
    all = 'All Levels'
    b1_and_above = 'B1 and over'
    c1 = 'C1'
    
    course_level_choices= [
        (all,'All levels'),
        (b1_and_above, 'B1 (Intermediate) and over'),
        (c1,'C1 (Advanced) only')
    ]

    

    course_id = models.CharField(max_length = 10)
    course_category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length = 254)
    friendly_name = models.CharField(max_length = 254, null = True, blank= True)
    course_description = models.TextField(max_length = 500)
    course_hours = models.DecimalField(max_digits=3, decimal_places=0)
    maximum_class_size = models.DecimalField(max_digits=2, decimal_places=0)
    minimum_age = models.DecimalField(max_digits=2, decimal_places=0, validators = [MinValueValidator(5,message = "Minimum Age is 5")])
    maximum_age = models.DecimalField(max_digits =2, decimal_places=0, blank=True, null =True, validators = [MinValueValidator(5,message = "Minimum Age is 5")]) 
    cost_per_week = models.DecimalField(max_digits = 10, decimal_places = 2, default=0)
    course_levels = models.CharField(max_length=50, choices = course_level_choices)
    course_timetable = models.CharField(max_length = 30)
    
    

    


    def __str__(self):
        return self.name


    def get_friendly_name(self):
        return self.friendly_name        

    # Generate Category specific id
    def _generate_course_id(self):
        course_number = Course.objects.filter(course_category = self.course_category).count()
        course_abbreviation = str(self.course_category)[0:2]
        
        return f'{course_abbreviation}_{str(course_number + 1)}'



    def save(self, *args, **kwargs):
        """
        Override the original save method to ensure there is
        a booking number
        """
        if not self.course_id:
            self.course_id = self._generate_course_id()
        super().save(*args, **kwargs)    

