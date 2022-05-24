import random

from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from . form import NovelForm



def index(request):
    ff = Fanfics.objects.all()
    return render(request, 'main/index.html', {'ff': ff})


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        fanfics = Fanfics.objects.filter(title__contains=searched)
        return render(request, 'main/search.html', {'searched': searched, 'fanfics': fanfics})
    else:
        return render(request, 'main/search.html')


def tag(request):
    genres = Genre.objects.all()

    context = {
         'genres': genres
     }
    return render(request, 'main/search_genre.html', context)


def tables(request):
    tables = User.objects.all()
    # novels = Novel.objects.all()
    # return render(request, 'main/table.html', {'tables': tables, 'novels': novels})


def favorites(request):
    user = request.user
    fav = user.favorites.all()
    return render(request, 'main/favorites.html', {'fav': fav})


def fanfic_detail(request, id, author=None):
    # ch = ChapterForm(request.POST or None)
    # if ch.is_valid():
    #     content = request.POST.get('content')
    #     comment = Comment.objects.create(post=post, user=request.user, content=content)
    #     comment.save()
    #     return redirect(post.get_absolute_url())
    # else:
    #     cf = CommentForm()
    #
    # context = {
    #     'comment_form': cf,
    # }
    post = get_object_or_404(Fanfics, pk=id)
    if request.user.is_authenticated:
        post.favorites.add(request.user)
        return render(request, 'main/details.html', {'post': post})
    else:
        return render(request, 'main/details.html', {'post': post})

def my_fanfics(request):
    user = request.user
    my_fan = user.my_fan.all()
    return render(request, 'main/my_fan.html', {'my_fan': my_fan})


def form(request):
    submitted = False
    if request.method == "POST":
        # user = request.user.username
        # authors = Fanfics.objects.get(author=user)
        forms = NovelForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/', 'submitted=True')
    else:
        forms = NovelForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/form.html', {'form': forms, 'submitted': submitted})


def randoms(request):
    all_story = list(Fanfics.objects.all())
    recent_story = random.choice(all_story)

    return render(request, 'main/random.html', {'recent_story': recent_story})