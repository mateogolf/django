# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, HttpResponse, redirect


def removeWarning(request, warning):
    if warning in request.session:
        del request.session[warning]

# Create your views here.
def index(request):
    if 'courses' not in request.session:
        request.session['courses'] = []
    courses = Course.objects.all()
    for course in courses:
        request.session['courses'].append(course)
    return render(request, 'courses/index.html')
# POST method
def create(request):
    if request.method == "POST":
        #Validate
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            removeWarning(request, 'errorname')
            removeWarning(request, 'errordesc')
            removeWarning(request, 'name')
            removeWarning(request, 'desc')
            for tag, error in errors.iteritems():
                request.session["error" + tag] = error
                print request.session["error" + tag]
            request.session['name'] = request.POST['name']
            request.session['desc'] = request.POST['desc']
            return redirect('/courses')
        else:
            #Remove past errors
            removeWarning(request, 'errorname')
            removeWarning(request, 'errordesc')
            removeWarning(request, 'name')
            removeWarning(request, 'desc')
            
            newCourse = Course(
                name=request.POST['name'], desc=Description.objects.create(
                content=request.POST['desc']))
            newCourse.save()
            return redirect('/courses')
    else:
        return redirect('/courses')
# Open Destroy Page
def show(request,course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'id': course.id,
        'name': course.name,
        'description': course.desc.content
    }
    return render(request, 'courses/destroy.html',context)
#Actually Destroys
def destroy(request, course_id):
    tempCourse = Course.objects.get(id=course_id)
    tempDesc = Description.objects.get(id=course_id)
    tempDesc.delete()
    tempCourse.delete()
    return redirect('/courses')
#Comments Table
def comments(request,course_id):
    course = Course.objects.get(id=course_id)
    context = {'id': course.id,
            'name': course.name,
    }
    if 'comments' not in request.session:
        request.session['comments'] = []
    comments = Comments.objects.all()
    for comment in comments:
        request.session['comments'].append(comment)
    return render(request, 'courses/comments.html',context)


def createComment(request, course_id):
    print "Create Started"
    if request.method == "POST":
        removeWarning(request, 'errorcomment')
        removeWarning(request, 'comment')
        #Validate
        errors = Comments.objects.validateComment(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                request.session["error" + tag] = error
                request.session['comment'] = request.POST['comment']
                print tag + ": " + error
            return redirect('/courses/' + course_id + '/comments')
        else:
            #Remove past errors
            removeWarning(request, 'errorcomment')
            removeWarning(request, 'comment')

            #Add course and comment
            # tempdesc = Description(content=request.POST['desc'])
            tempCourse = Course.objects.get(id=course_id)
            newComment = Comments(course = tempCourse, content = request.POST['comment'])

            print newComment
            newComment.save()
            return redirect('/courses/' + course_id + '/comments')
    else:
        return redirect('/courses/' + course_id + '/comments')

def delComment(request,course_id,comment_id):
    tempComment = Comments.objects.get(id=comment_id)
    tempComment.delete()
    return redirect('/courses/'+course_id+'/comments')
