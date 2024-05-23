import requests
from django.shortcuts import render
from .models import User

# define in which HTML file a certain method goes to
mainPage = 'index.html'

# Create your views here.

#DEFAULT

def testing(request):
    return render(request, mainPage)

# Users
def all_users(request):
    response = requests.get('http://localHost:4000/user/')
    if response.status_code == 200:
        users = response.json()
    else:
        users = []
    
    return render(request, mainPage, {'users': users})

def add_user(request):
    response = requests. get()