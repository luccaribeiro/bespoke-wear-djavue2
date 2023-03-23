# coding: utf-8
import json
from ..commons.django_views_utils import ajax_login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import Product, ShoppingCart, Coupon
from django.http import HttpResponse


@ajax_login_required
def edit_product(request, id):
    obj = Product.objects.get(id=id)
    obj.name = request.POST.get('name')
    obj.price = request.POST.get('price')
    obj.description = request.POST.get('description')
    obj.image = request.POST.get('image')
    obj.save()
    return redirect('/tasks/list')

@ajax_login_required
def delete_of_cart(request, id):
    ShoppingCart.objects.filter(id=id).delete()
    return redirect('/tasks/shopping')

@ajax_login_required
def delete_product(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('/tasks/list')

@ajax_login_required
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        ShoppingCart.objects.create(user=user, product=product)
        return redirect('/tasks/list')
    return redirect('/tasks/list')

@ajax_login_required
def get_product_id(request, id):
    product = Product.objects.filter(id=id).values()
    return JsonResponse({"product": list(product)})

@ajax_login_required
def list_products(request):
    products = Product.objects.all()
    products = [product.to_dict_json() for product in products]
    return JsonResponse({"products": products})

@ajax_login_required
def list_shopping_cart(request):
    current_user = request.user
    shopping_cart = ShoppingCart.objects.filter(user=current_user).values()
    return JsonResponse({"shoppingCart": list(shopping_cart)})

@ajax_login_required
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

@ajax_login_required
@csrf_exempt
def create_coupon(request):
    coupon = Coupon(
        name = request.POST.get("coupon_name"),
        kind_of_discount = request.POST.get("type"),
        discount_value = request.POST.get("price"),
    )
    coupon.save()
    return HttpResponse(coupon)

@ajax_login_required
@csrf_exempt
def apply_coupon(request):
    name = request.POST.get("coupon_name")
    coupon = Coupon.objects.filter(name=name).first()
    if coupon == None:
        return JsonResponse({})
    return JsonResponse(coupon.to_dict_json())