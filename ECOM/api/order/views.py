from django.shortcuts import render

from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Order
from django.views.decorators.csrf import csrf_exempt
from api.order.serlializers import OrderSerializer

# Create your views here.
def validate_user_session(id , token):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        else:
            return False
    except UserModel.DoesNotExist:
        return False
    
@csrf_exempt
def add(request , id , token):
    if not validate_user_session(id, token):
        return JsonResponse({'error': 'User not logged in '}, status=403)
    if request.method == 'POST':
        user_id = id 
        transaction_id = request.POST.get['transaction_id']
        amount = request.POST.get['amount']
        products= request.POST.get('products')
        total_pro = len(products.split(',')[:-1])

        Usermodel = get_user_model()
        try:
            user = Usermodel.objects.get(pk=user_id)

        except Usermodel.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=404) 
        order = Order(user = user , product_names = products , total_products = total_pro , transaction_id = transaction_id , total_amount = amount)
        order.save()
        return JsonResponse({'success': True , 'error': False , 'message': 'Order added successfully'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
 