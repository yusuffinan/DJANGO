# Generated by Django 4.2.5 on 2023-10-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default=' ', editable=False, unique=True),
        ),
    ]
