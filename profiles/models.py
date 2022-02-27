from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    # Add level options for current English Level
    a1 = 'A1'
    a2 = 'A2'
    a2h = 'A2H'
    b1 = 'B1'
    b2 = 'B2'
    c1 = 'C1'
    level_choices = [
        (a1, 'A1 - Beginner'),
        (a2, 'A2- Elementary'),
        (a2h, 'A2H- Pre-Intermediate'),
        (b1, 'B1- Intermediate'),
        (b2, 'B2 - Upper Intermediate'),
        (c1, 'C1- Advanced'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_name = models.CharField(max_length=40, null=True, blank=True)
    default_email = models.EmailField(max_length=254,
                                      null=True, blank=True)
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)
    default_nationality = models.CharField(max_length=40,
                                           null=True, blank=True)
    default_first_language = models.CharField(max_length=40,
                                              null=True, blank=True)
    default_age = models.DecimalField(max_digits=3, decimal_places=0,
                                      null=True, blank=True)
    default_current_english_level = models.CharField(max_length=15,
                                                     choices=level_choices,
                                                     null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
