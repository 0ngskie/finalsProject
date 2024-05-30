import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from .request import *
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            try:
                # Assuming the User model is related to Employee model via a one-to-one or foreign key relationship
                employee = Employee.objects.get(user=user)

                if employee.specialty == 'Manager' and employee.manager_id is None:
                    return redirect('manager_portal')  # Replace with the actual URL name for the manager portal
                elif employee.specialty in ['Mechanic', 'Electrician']:
                    return redirect('employee_portal')  # Replace with the actual URL name for the employee portal
                else:
                    return HttpResponse('Invalid role.')
            except Employee.DoesNotExist:
                return HttpResponse('User does not have employee details.')
        else:
            return HttpResponse('Invalid login credentials.')
    else:
        return render(request, 'login.html')

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

            #TODO Add Error Handling for when the API is offline when user tries to regiter.
            #TODO Add a Check for Email and Username if it already exists in the DB
            #TODO User cannot leave any fields empty

            if 200 <= response.status_code < 300:
                messages.success(request, 'Registration successful.')
            else:
                messages.error(request, 'Registration failed.')
        
        else:
            messages.error(request, 'Fields cannot be empty.')

    else:

        form = UserRegistrationForm()
    
    return render(request, 'createManagerAccount.html')


def manager_portal(request):
    return render(request, 'managerPortal.html')

def register_employee(request):
    return render(request, 'registerEmployee.html')

def services_offered(request):
    return render(request, 'services.html')
