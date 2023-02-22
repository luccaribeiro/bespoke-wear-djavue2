# coding: utf-8
from django.http import JsonResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        # Obtém as informações de registro enviadas pelo front-end
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Salva as informações de registro do usuário no banco de dados
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Redireciona o usuário para a página de login
        return redirect('/accounts/login')

    return redirect('/accounts/register')



@csrf_exempt
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != "post":
        raise Exception("Logout only via post")
    auth.logout(request)
    return JsonResponse({})


def whoami(request):
    i_am = (
        {
            "user": _user2dict(request.user),
            "authenticated": True,
        }
        if request.user.is_authenticated
        else {"authenticated": False}
    )
    return JsonResponse(i_am)


def _user2dict(user):
    d = {
        "id": user.id,
        "name": user.get_full_name(),
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "permissions": {
            "ADMIN": user.is_superuser,
            "STAFF": user.is_staff,
        },
    }
    return d
