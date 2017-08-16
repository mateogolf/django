# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# the index function is called when root is visited
def index(request):
    if 'users' not in request.session:
        request.session['users'] = []
    users = User.objects.all()
    print users
    for user in users:
        request.session['users'].append(user)
    return render(request,'users/index.html')

def new(request):
    context={'new':True}
    return render(request,'users/edit.html',context)

def create(request):
    if request.method == "POST":
        #Validate
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                # messages.error(request, error, extra_tags=tag)
                print tag + ": " + error
            return redirect('/users/new')
        else:
            newUser = User(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            print newUser
            newUser.save()
            return redirect('/users')
    else:
        return redirect('/users')


def show(request,user_id):
    if request.method == "POST":
        update(request,user_id)
        return redirect('/users')
    else:
        user = User.objects.get(id=user_id)
        context = {'id': user.id,
                   'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   'created_at': user.created_at
        }
        return render(request,'users/view.html',context)

def edit(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'new': False,
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
                }
    return render(request, 'users/edit.html', context)

def update(request, user_id):
    if request.method == "POST":
        #Validate
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                # messages.error(request, error, extra_tags=tag)
                print tag + ": " + error
            return redirect('/users/new')
        else:
            user = User.objects.get(id=user_id)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.updated_at = datetime.today()
            user.save()
            return redirect('/users')
    else:
        return redirect('/users')



def destroy(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/users')
