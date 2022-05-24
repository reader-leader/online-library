# Generated by Django 3.2.13 on 2022-05-22 11:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_alter_fanfics_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanfics',
            name='favorites',
            field=models.ManyToManyField(blank=True, editable=False, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
