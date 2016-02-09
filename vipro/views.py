#!/usr/bin/python --2.7
# -*- coding: utf-8 -*-

### auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
# from django.contrib.auth.forms import UserCreationForm
from .forms import MyRegistrationForm
from django.contrib.auth.views import login as original_login


def login(request):
    context_dict = {}
    context_dict.update(csrf(request))
    return render(request, 'login.html', context_dict)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return HttpResponseRedirect('/vicat/catalog/')
    # return render(request, 'loggedin.html',
    #                         {'full_name': request.user.username})

def invalid_login(request):
    return render(request, 'invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/vicat/catalog/')
    # return render(request, 'logout.html')

def register_user(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')


    context_dict = {}
    context_dict.update(csrf(request))

    context_dict['form'] = MyRegistrationForm()
    return render(request, 'register.html', context_dict)

def register_success(request):
    return render(request, 'register_success.html')


