from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
#Sample Validation Class
class Class_nameManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #First name
        if not postData['first_name'].isalpha():#letters only
            errors["first_name"] = "First name: letters only"
        if len(postData['first_name']) < 2:#name size
            errors["first_nameC"] = "First name: No fewer than 2 characters"
        #last name
        if not postData['last_name'].isalpha():  # letters only
            errors["last_name"] = "Last name: letters only"
        if len(postData['last_name']) < 2:  # name size
            errors["last_nameC"] = "Last name: No fewer than 2 characters"
        #Email
        if not EMAIL_REGEX.match(postData['email']) and len(postData['email']) > 7:
            errors["email"] = "Please enter a valid email"
        else:
            findclass_names = Class_name.objects.filter(email=postData['email'])
            if len(findclass_names) != 0:
                errors["email"] = "Email is already in the system"
        #Password Validation length then compare w/ pw_confirm
        if len(postData['password']) < 8:
            errors["password"] = "Password min. 8 chars"
        elif postData['pw_confirm'] != postData['password']:
            errors["pw_confirm"] = "Password must match"
        #First, test whether it can become a datetime class
        try:
            birthday = datetime.strptime(postData['birthday'], '%Y-%m-%d')
            #Validate Date's accuracy based on case
            if birthday >= datetime.now():
                errors["birthday"] = "Not a valid birthday"
        except ValueError:#input is not a date
            errors["birthday"] = "Input Valid Date"
        return errors

    
    #Login Validation for email and password match
    def login_validator(self, postData):
        errors = {}
        #Valid Email
        if not EMAIL_REGEX.match(postData['email']) and len(postData['email']) > 7:
            errors["email"] = "Please enter a valid email"
        else:#Matched Email
            findClass_names = Class_name.objects.filter(email=postData['email'])
            if len(findClass_names) == 0:
                errors["email"] = "Email not registered"
            else:
                #Check Password using bcrypt
                if not bcrypt.checkpw(postData['password'].encode("utf8"), findClass_names[0].password.encode("utf8")):
                    errors["password"] = "Password min. 8 chars"
            #     if postData['password'] != findClass_names[0].password:
            #         errors["password"] = "Incorrect Password"
        return errors
#Sample OneToOne Relationship with class_name
class OnetoOne(models.Model):
    content = models.TextField(default="no info")

class Class_name(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)#make long enough for hash
    birthday = models.DateField()
    #Sample OneToOne Relationship field
    OnetoOne = models.OneToOneField(OnetoOne, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Class_nameManager()
    def __repr__(self): #Viewable on command line
        return "<Class_name object: {} {},email: {}>".format(self.first_name, self.last_name, self.email)

#Sample One to Many Relationship with many of this class for every class_name
class ManytoOne(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #Example OnetoMany: One(class_name) to Many(ManytoOne)
    class_name = models.ForeignKey(Class_name, related_name="ManytoOnes")
    def __repr__(self):
        return "<ManytoOne object: {}: {}>".format(self.name, self.desc)

#sample Many to Many relationship with this class and class_name
# field always goes into the second class
class ManyToMany(models.Model):
    class_names = models.ManyToManyField(Class_name, related_name="manyToManys")
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)