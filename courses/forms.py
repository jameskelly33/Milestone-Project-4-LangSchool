from django import forms
from .models import Course, Category


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['course_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get category options 
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['course_category'].choices = friendly_names
        # Add custom placeholders to aid user form completion
        self.fields['name'].widget.attrs['placeholder'] = 'eg. general_english_full_time'
        self.fields['friendly_name'].widget.attrs['placeholder'] = 'eg. General English Full Time'
        self.fields['course_timetable'].widget.attrs['placeholder'] = 'eg. Mon-Fri, 9.00 - 14.00'

      
            
        