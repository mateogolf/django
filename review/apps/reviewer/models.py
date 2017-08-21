# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from ..apps.login_reg.models import User
# Create your models here.

class User(models.Model):
    alias = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = UserManager()
    def __repr__(self):
        return "<User object: {}>".format(self.alias)

class Author(models.Model):
    name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Author object: {} {},email: {}>".format(self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="books")
    # uploader = models.ForeignKey(User, related_name="uploaded_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book object: {}: {}>".format(self.name, self.desc)

class Review(models.Model):
    user = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    content = models.TextField()
    rating = models.IntegerField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Review by {}: {}stars>".format(self.user.name, self.stars)
