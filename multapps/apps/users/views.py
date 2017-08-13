# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    response = "placeholder to later display all users"
    return HttpResponse(response)

def register(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)
