# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from django.core import serializers
import json
def index(request):
    return render(request, 'users/index.html')
# Create your views here.
def all_json(request):
    users = Users.objects.all()
    print users
    return HttpResponse(serializers.serialize("json", users), content_type='application/json')
def all_html(request):
    context = {"users": Users.objects.all()}
    return render(request, 'users/all.html', context)
def find(request):
    return render(request, 'users/all.html',
        { "users":    Users.objects.filter(first_name__startswith=request.POST['first_name_starts_with']) }
    )
def create(request):
    Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],age=request.POST['age'])
    return render(request, 'users/all.html',{ "users": Users.objects.order_by("-id") })
