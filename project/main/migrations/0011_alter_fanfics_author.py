# Generated by Django 3.2.13 on 2022-05-22 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0010_auto_20220522_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fanfics',
            name='author',
            field=models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]