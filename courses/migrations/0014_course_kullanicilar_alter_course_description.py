# Generated by Django 4.2.5 on 2023-10-27 16:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0013_course_subtitle_alter_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='kullanicilar',
            field=models.ManyToManyField(related_name='kurslar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(),
        ),
    ]
