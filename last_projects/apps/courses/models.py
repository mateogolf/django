# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name must be over 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Description must be more than 15 characters"
        return errors


class CommentManager(models.Manager):
    def validateComment(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors["comment"] = "Can't have empty comments"
        print errors
        return errors

class Description(models.Model):
    content = models.TextField(default="no description")
    objects = CourseManager()

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
    def __repr__(self):
        return "<Course: {} Desc:{}>".format(self.name,self.desc.content)


class Comments(models.Model):
    course = models.ForeignKey(Course, related_name="comments")
    content = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
    def __repr__(self):
        return "<Comment #{} on Course: {}>".format(self.id,self.course.name)
