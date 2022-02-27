from django.contrib import admin
from .models import UserProfile


class ProfilesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'default_name',
        'default_email',
        'default_phone_number',
        'default_nationality',
        'default_first_language',
        'default_country',
        'default_current_english_level'
    )


admin.site.register(UserProfile, ProfilesAdmin)
