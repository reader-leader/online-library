# Generated by Django 3.2.13 on 2022-05-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_genre_alter_fanfics_options_alter_fanfics_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(choices=[('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Humor', 'Humor'), ('Fantasy', 'Fantasy'), ('Thriller', 'Thriller'), ('Detective', 'Detective'), ('Drama', 'Drama'), ('Adventure', 'Adventure'), ('Historical', 'Historical'), ('Tragedy', 'Tragedy')], max_length=50),
        ),
    ]
