# Generated by Django 3.2 on 2022-02-05 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_form', '0003_auto_20220205_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='course_id',
        ),
    ]
