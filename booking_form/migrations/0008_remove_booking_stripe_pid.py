# Generated by Django 3.2 on 2022-02-12 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_form', '0007_booking_stripe_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='stripe_pid',
        ),
    ]
