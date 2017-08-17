# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #First name
        if not postData['first_name'].isalpha():
            errors["first_name"] = "First name: letters only"
        if len(postData['first_name']) < 2:
            errors["first_nameC"] = "First name: No fewer than 2 characters"
        #last name
        if not postData['last_name'].isalpha():
            errors["last_name"] = "Last name: letters only"
        if len(postData['last_name']) < 2:
            errors["last_nameC"] = "Last name: No fewer than 2 characters"
        #Email
        if not EMAIL_REGEX.match(postData['email']) and len(postData['email']) > 7:
            errors["email"] = "Please enter a valid email"
        else:
            findUsers = User.objects.filter(email=postData['email'])
            if len(findUsers) != 0:
                errors["email"] = "Email is already in the system"
        #If email in table, return error
        if len(postData['password']) < 8:
            errors["password"] = "Password min. 8 chars"
        elif postData['pw_confirm'] != postData['password']:
            errors["pw_confirm"] = "Password must match"
        #birthday validation before today
        ##IF NO ENTRY: return error
        # print str(postData['birthday'])
        try:
            birthday = datetime.strptime(postData['birthday'], '%Y-%m-%d')
            if birthday >= datetime.now():
                errors["birthday"] = "Not a valid birthday"
        except ValueError:
            errors["birthday"] = "Input Valid Date"
        return errors

    def login_validator(self, postData):
        errors = {}
        #Valid Email
        if not EMAIL_REGEX.match(postData['email']) and len(postData['email']) > 7:
            errors["email"] = "Please enter a valid email"
        else:#Matched Email
            findUsers = User.objects.filter(email=postData['email'])
            if len(findUsers) == 0:
                errors["email"] = "Email not registered"
            else:
                #Check Password
                # user = User.objects.get(email=postData['email'])
                if not bcrypt.checkpw(postData['password'].encode("utf8"), findUsers[0].password.encode("utf8")):
                    errors["password"] = "Password min. 8 chars"
            #     if postData['password'] != findUsers[0].password:
            #         errors["password"] = "Incorrect Password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {},email: {}>".format(self.first_name, self.last_name, self.email)
