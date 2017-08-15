# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # Create 3 different user accounts
    # Have the first user create 2 books.
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
