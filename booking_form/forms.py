from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    course_length = forms.ChoiceField(choices=[(number, number)
                                      for number in range(1, 52)])

    class Meta:
        model = Booking
        widgets = {
            'course_start_date': forms.DateInput(
                                  attrs={'type': 'date',
                                         'class': 'myDateClass'}),
            }
        fields = ('full_name', 'email', 'phone_number',
                  'country', 'nationality',
                  'first_language', 'age',
                  'course_length',
                  'course_start_date', 'course_level',
                  'course_level', 'course', 'course_friendly_name',
                  'course_timetable', 'course_cost_per_week',
                  'total_course_cost',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and stripe class, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'nationality': 'Nationality',
            'first_language': 'First Language',
            'age': 'Age',
            'course_length': "Course Length",
            'course_start_date': 'Course Start Date',
            'course_level': 'Course Level',
            'course': 'Course',
            'course_friendly_name': 'Course Name',
            'course_timetable': 'Course Timetable',
            'course_cost_per_week': 'Course Cost Per Week',
            'total_course_cost': 'Total Course Cost',
        }

        self.fields['course_length'].widget.attrs['autofocus'] = True
        self.fields['course_length'].widget.attrs['min'] = 1
        self.fields['age'].widget.attrs['min'] = 5
        for field in self.fields:
            if field != 'age':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
