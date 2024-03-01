from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            return redirect('character_sheet_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


def logout(request):
    django_logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})