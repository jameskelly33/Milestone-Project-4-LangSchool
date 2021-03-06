# Generated by Django 3.2 on 2022-01-20 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=8)),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
                ('course_description', models.CharField(max_length=500)),
                ('course_hours', models.DecimalField(decimal_places=0, max_digits=3)),
                ('maximum_class_size', models.DecimalField(decimal_places=0, max_digits=2)),
                ('minumum_age', models.DecimalField(decimal_places=0, max_digits=2)),
                ('course_timetable', models.CharField(max_length=30)),
                ('course_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.category')),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
