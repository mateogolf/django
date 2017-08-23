# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import bcrypt
# the index function is called when root is visited

#Showing a List of Objects in html 
def index(request):
    #create a list in sessions if not already created
    # if '[class_name]s' not in request.session:
        # request.session['[class_name]'] = []
    #Query to variable [class_name]s =  [Class_name].objects.all()
    #for [class_name] in [class_name]s:
        # session['[class_name]'.append([class_name])
    #return render(request, '[app_name]/index.html')
#GET goes to the html that has a form without taking a variable
def new(request):
    # return render(request, '[app_name]/edit.html')
#GET to edit an entry, takes [class_name]_id
def edit(request, user_id):
    # Set a variable [class_name] = [class_name].objects.get(id=[class_name]_id)
    #context dictionary relevant information that will be edited
    #context ={'key': [class_name].[column_name],}
    # context = {'id': user.id}
    # return render(request, '[app_name]/edit.html', context)

#POST for using the edit.html's form
def create(request):
    if request.method == "POST":
        #Validate
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
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


def show(request, user_id):
    if request.method == "POST":
        #go to the post method
        update(request, user_id)

        return redirect('/users')
    else:
        user = User.objects.get(id=user_id)
        context = {'id': user.id,
                   'first_name': user.first_name,
                   'last_name': user.last_name,
                   'email': user.email,
                   'created_at': user.created_at
                   }
        return render(request, 'users/view.html', context)





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
