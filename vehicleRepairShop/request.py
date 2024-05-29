import requests

from django.conf import settings

def all_users(request):
    
    response = requests.get('http://localHost:4000/user/')
    print(response.status_code)
    print(response.url)
    
    return response.json()

def register_user(request):
    
    response = requests.post('http://localHost:4000/create')

    return response.json()