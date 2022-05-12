from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import NewUserForm, UpdateProfileForm
from .models import Profile


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "There was an error")
            return redirect('login')
    return render(request, 'authenticate/login.html')


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/')
        else:
            messages.success(request, "Unsuccessful registration. Invalid information.")
            return redirect('register')
    form = NewUserForm()
    return render(request, 'authenticate/register.html', {'register_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')


def add_profile(request):
    submitted = False
    if request.method == "POST":
        forms = UpdateProfileForm(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
        return redirect('/', 'submitted=True')
    else:
        forms = Profile()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'authenticate/add_profile.html', {'form': forms, 'submitted': submitted})


def user_profile(request):
    profile = Profile.objects.all()
    return render(request, 'authenticate/profile.html', {'profile': profile})

def contact_us(request):
    return render(request, 'authenticate/contact_us.html')

