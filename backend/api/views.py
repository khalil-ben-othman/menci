from rest_framework.response import Response
from .serializers import ProductSerializer, ItemSerializer, MessageSerializer
from rest_framework.decorators import api_view
from backend.models import Product, Client, Item, Order, Subscriber
from rest_framework import status
from .utils import send_email_with_order
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.middleware.csrf import get_token



@api_view(['GET'])
def getProducts(request):
    products = reversed(Product.objects.all())
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def validateBag(request):
    name = request.data.get('name')
    email = request.data.get('email')
    address = request.data.get('address')
    phone = request.data.get('phone')
    city = request.data.get('city')
    client = Client.objects.create(name=name, email=email, address=address, phone=phone, city=city)
    client.save()
    total = request.data.get('total')
    order = Order.objects.create(client=client, total=total)
    items = request.data.get('items')
    for item in items:
        product = Product.objects.get(id=item['id'])
        size = item['size']
        quantity = item['quantity']
        price = product.price * int(quantity)
        order_item = Item.objects.create(product=product, price=price, size=size, quantity=quantity)
        order_item.save()
        order.items.add(order_item)
    order.save()
    send_email_with_order(order.id)
    return Response({'success': 'order passed successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def subscribe(request):
    email = request.data.get('email')
    subscriber = Subscriber.objects.create(email=email)
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def contact(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])    
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})
    



