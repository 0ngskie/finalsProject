import requests
from django.shortcuts import render
from .models import User

# Create your views here.

def base(request):
    templates = User.objects.all()
    return render(request, 'templates/base.html', {'templates': templates})

def viewUsers(request):
    api_url = 'https://localhost:4000/user'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        userData = response.json()
        return render(request, 'finalsProject/templates/base.html', {'data' : userData})
    else:
        return render(request, 'finalsProject/templates/error_base.html', {'error': response.text})