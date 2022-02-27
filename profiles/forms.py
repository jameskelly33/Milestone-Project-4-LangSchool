from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_name': 'Name',
            'default_email': 'Email',
            'default_phone_number': 'Phone Number',
            'default_country': 'Country of Residence',
            'default_nationality': 'Nationality',
            'default_first_language': 'First Language',
            'default_age': 'Age',
            'default_current_english_level': 'Current English Level',
        }

        self.fields['default_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
