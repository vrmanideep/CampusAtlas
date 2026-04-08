import json
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Location

@login_required(login_url='login')
def profile_view(request):
    return render(request, 'main/profile.html')

def home(request):
    # If the user is logged in, send them straight to the map
    if request.user.is_authenticated:
        return redirect('dashboard')
    # If not logged in, send them to login (or you can keep it rendering index.html)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Creates the user and hashes the password securely
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request, 'main/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'main/login.html', {'error': 'Invalid Credentials.'})
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard_view(request):
    # This must be indented exactly 4 spaces
    locations = list(Location.objects.values('name', 'description', 'latitude', 'longitude', 'is_landmark'))
    
    # This must also be indented exactly 4 spaces, perfectly aligned with the line above
    return render(request, 'main/dashboard.html', {
        'locations_json': locations
    })

@login_required(login_url='login')
def search_location_api(request):
    query = request.GET.get('q', '')
    location = Location.objects.filter(name__icontains=query).first()
    if location:
        return JsonResponse({
            'success': True,
            'lat': location.latitude,
            'lng': location.longitude,
            'name': location.name,
            'desc': location.description or ""
        })
    return JsonResponse({'success': False, 'message': 'Location not found'})