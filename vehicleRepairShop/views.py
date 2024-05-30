import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, loginManagerAccount
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
            loginManagerAccount(request, user)
            
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

def employee_portal (request):
    return render(request, 'employeePortal.html')
def manager_portal(request):
    return render(request, 'managerPortal.html')

def register_employee(request):
    return render(request, 'registerEmployee.html')

def services_offered(request):
    return render(request, 'services.html')
