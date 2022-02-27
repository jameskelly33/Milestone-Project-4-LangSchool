from django import forms
from .models import Post


class BlogForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['date_posted', 'author', 'likes']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Post Title',
            'post_description': 'A short description of the post content',
            'post_content': 'Enter post content here. Please start a new line\
                 between paragraphs'}

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
