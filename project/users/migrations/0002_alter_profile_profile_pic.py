# Generated by Django 3.2.13 on 2022-05-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='https://cdn4.iconfinder.com/data/icons/minimal-8/24/profile-512.png', null=True, upload_to='profile_image'),
        ),
    ]
