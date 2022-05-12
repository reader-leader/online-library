# Generated by Django 3.2.13 on 2022-05-09 09:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_rename_user_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='fanfics',
            name='favorites',
            field=models.ManyToManyField(related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
