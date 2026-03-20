
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main/index.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'main/signup.html', {'error': 'Username already exists. Please choose another.'})

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')

    return render(request, 'main/signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid Credentials. Please try again.'})

    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'main/dashboard.html')

@login_required(login_url='login')
def search(request):
    return render(request, 'main/search.html')
