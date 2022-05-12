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


def fanfic_detail(request, id):
    post = get_object_or_404(Fanfics, pk=id)
    post.favorites.add(request.user)
    return render(request, 'main/details.html', {'post': post})


def form(request):
    submitted = False
    if request.method == "POST":
        forms = NovelForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect('/', 'submitted=True')
    else:
        forms = NovelForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/form.html', {'form': forms, 'submitted': submitted})
