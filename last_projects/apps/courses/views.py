# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HTTPResponse, redirect

# Create your views here.
def index(request):
    if 'courses' not in request.session:
        request.session['courses'] = []
    courses = User.objects.all()
    print courses
    for user in courses:
        request.session['courses'].append(user)
    return render(request, 'courses/index.html')
# POST method
def create(request):
    
    return HTTPResponse("Placeholder")
# Open Destroy Page
def confirm(request):
    
    return HTTPResponse("Placeholder")
#Actually Destroys
def confirm(request):
    return HTTPResponse("Placeholder")
