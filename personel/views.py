from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from personel.forms import RegisterForm


def login_view(request):
    if request.user.is_authenticated():
        return redirect('home')
    error = False
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Incorrect login details."
            return render(request, 'login.html', { "error": error})
    else:
        return render(request, 'login.html', { "error": error})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    form = RegisterForm()
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            user.save()
            return render(request, 'login.html')
    return render(request, 'register.html', { 'form': form })