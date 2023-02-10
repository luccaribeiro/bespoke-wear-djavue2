# coding: utf-8
import json
# from ..commons.django_views_utils import ajax_login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import Product, ShoppingCart
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def edit_product(request, id):
    obj = Product.objects.get(id=id)
    obj.name = request.POST.get('name')
    obj.price = request.POST.get('price')
    obj.description = request.POST.get('description')
    obj.image = request.POST.get('image')
    obj.save()
    return redirect('/tasks/list')

def delete_of_cart(request, id):
    ShoppingCart.objects.filter(id=id).delete()
    return redirect('/tasks/shopping')

def delete_product(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('/tasks/list')

def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        ShoppingCart.objects.create(user=user, product=product)
        return redirect('/tasks/list')
    return redirect('/tasks/list')

def get_product_id(request, id):
    product = Product.objects.filter(id=id).values()
    return JsonResponse({"product": list(product)})

def list_products(request):
    products = Product.objects.all()
    products = [product.to_dict_json() for product in products]
    return JsonResponse({"products": products})

def list_shopping_cart(request):
    current_user = request.user
    shopping_cart = ShoppingCart.objects.filter(user=current_user).values()
    return JsonResponse({"shoppingCart": list(shopping_cart)})

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image')
        product = Product(name=name, description=description, price=price, image=image)
        product.save()
        return redirect('/tasks/list')
    return redirect('/api/produtos/listd')


# @ajax_login_required
# def list_todos(request):
#     todos = todo_svc.list_todos()
#     return JsonResponse({"todos": todos})
