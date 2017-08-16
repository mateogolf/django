# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # Create 3 different user accounts
    User.objects.create(first_name="Matt", last_name="Rodriguez", email="matt@dojo.com")
    User.objects.create(first_name="Rob", last_name="Dahal", email='matt@dojo.com')
    User.objects.create(first_name="Nate", last_name="Moore", email="matt@dojo.com")
    # Have the first user create 2 books.
    user1 = User.objects.first()
    Book.objects.create(name="Python", desc="dictionary",uploader=user1)
    Book.objects.create(name="Django", desc="python framework", uploader=user1)
    user1.save()
    # Have the second user create 2 other books.
    user2 = User.objects.get(id=2)
    Book.objects.create(name="Java", desc="strict syntax", uploader=user2)
    Book.objects.create(name="mySQL", desc="database language", uploader=user2)
    user2.save()
    # Have the third user create 2 other books.
    user3 = User.objects.get(id=3)
    Book.objects.create(name="MEAN", desc="google's stack", uploader=user3)
    Book.objects.create(name="Angular", desc="front-end framework", uploader=user3)
    user3.save()
    # Have the first user like the last book and the first book
    User.objects.first().liked_books.add(Book.objects.last(), Book.objects.first())#Helpful for adding multiple to a table/rel.
    # Have the second user like the first book and the third book
    User.objects.get(id=2).liked_books.add(Book.objects.first(), Book.objects.get(id=3))
    # Have the third user like all books
    for book in Book.objects.all():
        User.objects.get(id=3).liked_books.add(book)
    # Display all users who like the first book
    Book.objects.first().liked_users.all()
    # Display the user who uploaded the first book
    Book.objects.first().uploader
    # Display all users who like the second book
    Book.objects.get(id=2).liked_users.all()
    # Display the user who uploaded the second book
    Book.objects.get(id=2).uploader
    
    return HttpResponse("Hello World")
