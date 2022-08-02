from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_item':0 }
        cartItems = order['get_cart_item']

    products = Product.objects.all()
    contexe={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',contexe)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_item':0 }
        cartItems = order['get_cart_item']
    contexe={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',contexe)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created=Order.objects.get_or_create(customer=customer,complete=False)
        items= order.orderitem_set.all()
        cartItems = order.get_cart_item
    else:
        items=[]
        order={'get_cart_total':0,'get_cart_item':0 }
        cartItems = order['get_cart_item']
    contexe={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/checkout.html',contexe)

def updateItem(request):
    data = json.loads(request.body)
    productid = data['productid']
    action = data['action']
    print('action',action)
    print('productid',productid)

    customer = request.user.customer
    product = Product.objects.get(id=productid)
    order,created=Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)

    if action =='add':
        orderItem.quantity = orderItem.quantity+ 1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity-1

    orderItem.save()

    if orderItem.quantity<=0:
        orderItem.delete()

    
    return JsonResponse('item was added',safe=False)