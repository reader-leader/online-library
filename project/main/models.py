from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Users(models.Model):

    objects = models.Manager()
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Novel(models.Model):
    objects = models.Manager()

    CATEGORY = (
        ('Mystery', 'Mystery'),
        ('Fantastic', 'Fantastic'),
        ('Detective', 'Detective'),
        ('Romantic', 'Romantic'))

    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)


    def __str__(self):
        return self.title


class Genre(models.Model):
    objects = models.Manager()
    GENRE = (
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Horror', 'Horror'),
        ('Humor', 'Humor'),
        ('Fantasy', 'Fantasy'),
        ('Thriller', 'Thriller'),
        ('Detective', 'Detective'),
        ('Drama', 'Drama'),
        ('Adventure', 'Adventure'),
        ('Historical', 'Historical'),
        ('Tragedy', 'Tragedy')
    )

    genre = models.CharField(max_length=50, choices=GENRE)

    class Meta:
        ordering = ['genre']

    def __str__(self):
        return self.genre

#
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     def __str__(self):
#         return self.name



class Fanfics(models.Model):
    objects = models.Manager()
    CATEGORY = (
        ('min', 'min'),
        ('mid', 'mid'),
        ('max', 'max'),
    )
    STATUS = (
        ('Continue', 'Continue'),
        ('Сompleted', 'Сompleted'),
        ('Frozen', 'Frozen'),
        ('No chapter', 'No chapter'),
    )


    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    # author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    genre = models.ManyToManyField(Genre, blank=True)
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True, auto_created=True)

    #slug = models.SlugField(max_length=250, unique_for_date='publish')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fanfic_detail', args=[str(self.title)])

