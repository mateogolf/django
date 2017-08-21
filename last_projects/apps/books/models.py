# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..users.models import User
# Create your models here.


class ReviewManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #Book Val
        if len(postData['title']) < 1:
            errors["title"] = "Title: can't be empty"
        else:
            findBook = Book.objects.filter(title=postData['title'])
            if len(findBook) != 0:
                errors["title"] = "A book already has that title"
        #Either author or author_name must exist
        if not postData['author_id'] and len(postData['author_name']) < 1:
            errors["author"] = "There must be an author for the book"
        #If author_name found in Author, then
        if postData['author_id'] and len(postData['author_name']) > 1:
            errors["author"] = "Author: Select from list OR add new author, not BOTH"
        if not postData['author_id'] and len(postData['author_name']) > 1:
            findAuthor = Author.objects.filter(name=postData['author_name'])
            if len(findAuthor) != 0:  # author's name is found
                errors["no_author"] = "The new author's name matches a previous author, please delete"
        
        #Review can't be blank
        if len(postData['content']) < 1:
            errors["content"] = "You must have a review to add a book"
              
        #Must be an int for checking hackers
        try:
            int(postData['rating'])
            if not postData['rating'] or int(postData['rating']) < 1:
                errors["rating"] = "You must rate the book"
            if int(postData['rating']) > 5:
                errors["rating"] = "Rating >5, BREAK attempt fail!"
        except ValueError:
            errors["rating"] = "This is not an int, nice try breaking it, DICK!"
        return errors

    def review_validator(self, postData):
        errors = {}
        #Must be an int for checking hackers
        try:
            int(postData['rating'])
            if not postData['rating'] or int(postData['rating']) < 1:
                errors["rating"] = "You must rate the book"
            if int(postData['rating']) > 5:
                errors["rating"] = "Rating >5, BREAK attempt fail!"
        except ValueError:
            errors["rating"] = "This is not an int, nice try breaking it, DICK!"
        return errors

class Author(models.Model):
    name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    def __repr__(self):
        return "<Author: {}>".format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    # uploader = models.ForeignKey(User, related_name="uploaded_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    def __repr__(self):
        return "<Book object: {}: {}>".format(self.title, self.author.name)

class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()
    def __repr__(self):
        return "<Review object: by {} {}stars>".format(self.user.name, self.rating)
