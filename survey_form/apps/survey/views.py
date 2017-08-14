# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def removeWarning(request, warning):
    if warning in request.session:
        # try:
        del request.session[warning]
        #     break
        # except KeyError:
        #     print warning + " NOT DELETED!"

def index(request):
    request.session.clear()
    return render(request,"survey/index.html")

# def index(request):
#     request.session
#     return render(request,"survey/index.html")

def process(request):
    if request.method == "POST":
        #rest of assigned values
        request.session['location'] = request.POST['location']
        request.session['fav_lang'] = request.POST['favorite']
        nameMessage = "Name cannot be empty!"
        emptyComment = "Comments cannot be empty!"
        bigComments = "Comments is too long!"
        flag = False
        #validation conditionals
        if len(request.POST['name']) < 1:
            flag = True
            request.session['noName'] = nameMessage
        else:
            removeWarning(request, 'noName')
        if len(request.POST['comments']) < 1:
            flag = True
            request.session['noComments'] = emptyComment
        elif len(request.POST['comments']) >120:
            flag = True
            request.session['noComments'] = bigComments
        else:
            removeWarning(request,'noComments')

        if flag:
            return redirect('/')
        else:
            request.session['name'] = request.POST["name"]
            request.session['comments'] = request.POST['comments']
            removeWarning(request,'noName')
            removeWarning(request,'noComments')
            return redirect("/result")
        
        # if len(request.POST['name']) < 1 and (len(request.POST['comments']) < 1 or len(request.POST['comments']) > 120):
        #     request.session['name'] = ""
        #     request.session['comments'] = ""
        #     request.session['noName'] = nameMessage
        #     if len(request.POST['comments']) < 1:
        #         request.session['noComments'] = emptyComment
        #     else:
        #         request.session['noComments'] = bigComments
        #     return redirect('/')
        # elif len(request.POST['name']) < 1:
        #     request.session['noName'] = nameMessage
        #     request.session['name'] = ""
        #     request.session['comments'] = request.POST['comments']
        #     return redirect('/')
        # elif len(request.POST['comments']) < 1:
        #     request.session['noComments'] = emptyComment
        #     request.session['comments'] = ""
        #     request.session['name'] = request.POST["name"]
        #     return redirect('/')
        # elif len(request.POST['comments']) > 120:
        #     request.session['noComments'] = bigComments
        #     request.session['comments'] = request.POST['comments']
        #     request.session['name'] = request.POST["name"]
        #     return redirect('/')
        # else:
        #     request.session['name'] = request.POST["name"]
        #     request.session['comments'] = request.POST['comments']
        #     request.session['noName'] = None
        #     request.session['noComments'] = None
        #     return redirect("/result")
    else:
        return redirect("/")

def result(request):
    return render(request,"survey/result.html")
