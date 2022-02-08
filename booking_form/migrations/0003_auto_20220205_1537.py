# Generated by Django 3.2 on 2022-02-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_form', '0002_auto_20220203_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='course_id',
            field=models.CharField(default='Course_id', max_length=8),
        ),
        migrations.AlterField(
            model_name='booking',
            name='course_level',
            field=models.CharField(choices=[('A1', 'A1 - Beginner'), ('A2', 'A2- Elementary'), ('A2H', 'A2H- Pre-Intermediate'), ('B1', 'B1- Intermediate'), ('B2H', 'B2H- Upper-Intermediate'), ('C1', 'C1- Advanced')], max_length=15),
        ),
    ]
