from django.http import JsonResponse
from rest_framework import viewsets, permissions ,AllowAny, status
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
import re
import random
# Create your views here.
def generate_session_token(length=10):

    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)]+[str(i) for i in range(0,10)])  for _ in range(length))
@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    username = request.POST['email']
    password = request.POST['password']

    if not  re.match("/\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b/gi",username):
        return JsonResponse({'error': 'Invalid email format'}, status=400)
    if len(password) < 8:
        return JsonResponse({'error': 'Password must be at least 8 characters long'}, status=400)
    
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password')
            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error': 'User already logged in'}, status=400)
            session_token = generate_session_token()
            user.session_token = session_token
            user.save()
            login(request, user)
            return JsonResponse({'session_token': session_token , 'user' : usr_dict }, status=200)
        else:
            return JsonResponse({'error': 'Invalid password'}, status=400)
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)