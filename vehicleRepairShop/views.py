import requests
from django.shortcuts import render
from .models import User

# Create your views here.

# def all_users(request):
#     response = requests.get('http://localHost:4000/user/')
#     if response.status_code == 200:
#         users = response.json()
#     else:
#         users = []
    
#     return render(request, mainPage, {'users': users})

def login_page(request):
    return render(request, 'loginManagerAccount.html')

def home_page(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about.html')

def create_account(request):
    return render(request, 'createManagerAccount.html')


def manager_portal(request):
    return render(request, 'managerPortal.html')

def register_employee(request):
    return render(request, 'registerEmployee.html')

def services_offered(request):
    return render(request, 'services.html')