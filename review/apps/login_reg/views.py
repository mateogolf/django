# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt
# password = b"super secret password"
# Create your views here.
def index(request):
    return render(request,'login_reg/index.html')
def login(request):
    if request.method == "POST":
        context = {
            'lemail': request.POST['email']
        }
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return render(request, 'login_reg/index.html', context)
        else:
            #Check Password
            user = User.objects.get(email=request.POST['email'])
            if not bcrypt.checkpw(request.POST['password'].encode("utf8"), user.password.encode("utf8")):
                messages.error(request, "Password doesn't match email")
                return render(request, 'login_reg/index.html', context)
            else:
                user = User.objects.get(email=request.POST['email'])
                request.session['id'] = user.id
                return redirect('/success')
    else:
        return redirect('/')
def register(request):
    if request.method == "POST":
        context = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'birthday': request.POST['birthday']
        }
        #Validate
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return render(request, 'login_reg/index.html', context)
        else:
            #Check other emails
            # matchedEmails = User.objects.filter(email=request.POST['email'])
            # if len(matchedEmails) != 0:
            #     messages.error(request, "Email is already in the system")
            #     return render(request, 'login_reg/index.html',context)
            # else:
            hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            newUser = User(
                first_name=request.POST['first_name'], 
                last_name=request.POST['last_name'], 
                email=request.POST['email'],
                birthday=request.POST['birthday'],
                password=hash1)
            newUser.save()
            request.session['id'] = User.objects.get(email=request.POST['email']).id
            return redirect('/success')
    else:
        return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name
    }
    return render(request, 'login_reg/success.html',context)
