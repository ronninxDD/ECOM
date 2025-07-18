from django.http import JsonResponse
from rest_framework import viewsets, permissions , status
from rest_framework.permissions import AllowAny
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
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    if not  re.match(email_pattern, username, re.IGNORECASE):
        return JsonResponse({'error': 'Invalid email format'}, status=400)
    if len(password) < 3:
        return JsonResponse({'error': 'Password must be at least 3 characters long'}, status=400)
    
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
            usr_dict['session_token'] = session_token
            login(request, user)
            return JsonResponse({'session_token': session_token , 'user' : usr_dict }, status=200)
        else:
            return JsonResponse({'error': 'Invalid password'}, status=400)
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'}, status=400)

def signout(request , id):
    logout(request)
    
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})
    
    return JsonResponse({'success':'Logout success'})

class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create':[AllowAny]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]