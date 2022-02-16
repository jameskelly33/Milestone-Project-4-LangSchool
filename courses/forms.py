from django import forms
from .models import Course, Category


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['course_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['course_category'].choices = friendly_names
        