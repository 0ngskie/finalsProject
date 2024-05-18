from django.shortcuts import render
from .models import User

# Create your views here.

def base(request):
    templates = User.objects.all()
    return render(request, 'templates/base.html', {'templates': templates})