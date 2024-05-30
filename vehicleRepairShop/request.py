import requests

from django.conf import settings
import json
from django.http import JsonResponse

def all_users(request):
    
    response = requests.get('http://localHost:4000/user/')
    print(response.status_code)
    print(response.url)
    
    return response.json()

def register_user(first_name, last_name, email, username, password):
    url = "http://localhost:4000/user/create"

    payload = {
        'lastName': first_name,
        'firstName': last_name,
        'email': email,
        'username': username,
        'password': password,
        'userType': 'Customer'
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except ConnectionError:
        return None
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=400)

    if response.status_code == 201:
        return JsonResponse({'message': 'User registered successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Failed to register user'}, status=response.status_code)