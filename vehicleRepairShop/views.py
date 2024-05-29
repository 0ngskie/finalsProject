import requests
from django.shortcuts import render
from .models import *
from .forms import *
from .request import *
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            response = register_user(first_name, last_name, email, username, password)            

            if 200 <= response.status_code < 300:
                return HttpResponseRedirect(reverse('home_page'))
            else:
                return render(request, 'index.html', {'message': 'User registration failed'})

    else:

        form = UserRegistrationForm()
    
    return render(request, 'createManagerAccount.html')



def manager_portal(request):
    return render(request, 'managerPortal.html')

def register_employee(request):
    return render(request, 'registerEmployee.html')

def services_offered(request):
    return render(request, 'services.html')