from django.contrib import admin
from .models import Post

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'post_description',
        'post_content',
        'author',
        'date_posted',
    )


admin.site.register(Post, BlogAdmin)
