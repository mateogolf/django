# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # Create 3 different user accounts
# User.objects.create(first_name="Matt", last_name="Rodriguez", email="matt@dojo.com")
# User.objects.create(first_name="Rob", last_name="Dahal", email='matt@dojo.com')
# User.objects.create(first_name="Nate", last_name="Moore", email="matt@dojo.com")
#     # Have the first user create 2 books.
#     user1 = User.objects.first()
# Book.objects.create(name="Python", desc="dictionary",uploader=user1)
# Book.objects.create(name="Django", desc="python framework", uploader=user1)
    # Have the second user create 2 other books.
    # Have the third user create 2 other books.
    # Have the first user like the last book and the first book
    # Have the second user like the first book and the third book
    # Have the third user like all books
    # Display all users who like the first book
    # Display the user who uploaded the first book
    # Display all users who like the second book
    # Display the user who uploaded the second book

    return HttpResponse("Hello World")
