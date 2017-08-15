# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import * #from this folder(.) and the models.py file, import all classes
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # Create 5 books with the following names: 
    # C sharp, Java, Python, PHP, Ruby
    Book.objects.create(name="C sharp", desc="older language")
    Book.objects.create(name="Java", desc="strict syntax")
    Book.objects.create(name="Python", desc="indentation is king")
    Book.objects.create(name="PHP", desc="ancient language")
    Book.objects.create(name="Ruby", desc="It's Red")
    print Book.objects.all()
    # Create 5 different authors: 
    # Mike, Speros, John, Jadee, Jay
    Author.objects.create(first_name="Mike", last_name="",email="mike@dojo.com")
    Author.objects.create(first_name="Speros", last_name="",email="Speros@dojo.com")
    Author.objects.create(first_name="John", last_name="",email="John@dojo.com")
    Author.objects.create(first_name="Jadee", last_name="",email="Jadee@dojo.com")
    Author.objects.create(first_name="Jay", last_name="",email="Jay@dojo.com")
    print Author.objects.all()

    # Add a new field in the authors table called 'notes'.Make this a TextField.
    #notes = models.TextField()
    #   Successfully create and run the migration files.

    # Change the name of the 5th book to C#
    book = Book.objects.last()
    book.name = "C#"
    book.save()
    # Change the first_name of the 5th author to Ketul
    author = Author.objects.last()
    author.first_name = "Ketul"
    author.save()
    # Assign the first author to the first 2 books
    author1 = Author.objects.first()
    books1 = Book.objects.get(id=1)
    author1.books.add(Book.objects.get(id=1))
    author1.books.add(Book.objects.get(id=2))
    author1.save()
    print Author.objects.first().books.all()
    # Assign the second author to the first 3 books
    author2 = Author.objects.get(id=2)
    author2.books.add(Book.objects.get(id=1))
    author2.books.add(Book.objects.get(id=2))
    author2.books.add(Book.objects.get(id=3))
    author2.save()
    print Author.objects.get(id=2).books.all()
    # Assign the third author to the first 4 books
    author3 = Author.objects.get(id=3)
    author3.books.add(Book.objects.get(id=1))
    author3.books.add(Book.objects.get(id=2))
    author3.books.add(Book.objects.get(id=3))
    author3.books.add(Book.objects.get(id=4))
    author3.save()
    print Author.objects.get(id=3).books.all()
    # Assign the fourth author to the first 5 books (or in other words, all the books)
    for book in Book.objects.all():
        Author.objects.get(id=4).books.add(book)
    # For the 3rd book, retrieve all the authors
    Book.objects.get(id=3).authors.all()
    # For the 3rd book, remove the first author
    temp = Book.objects.get(id=3).authors.last()
    Book.objects.get(id=3).authors.remove(temp)
    # For the 2nd book, add the 5th author as one of the authors
    Book.objects.get(id=2).authors.add(Author.objects.get(id=5))
    # Find all the books that the 3rd author is part of
    Author.objects.get(id=3).books.all()
    # Find all the books that the 2nd author is part of
    Author.objects.get(id=2).books.all()

    return HttpResponse("Hello World")
